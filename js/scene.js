/* ═══════════════════════════════════════════════════
   scene.js — Premium Three.js Hero: Frosted Glass Crystal
   + Orbital Rings + Floating Particles + Mouse Parallax
   ═══════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ─── Guard: reduced motion ───────────────────────────────────────────
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canvas = document.getElementById('hero-canvas');
  if (!canvas || prefersReduced || typeof THREE === 'undefined') return;

  // ─── Renderer ───────────────────────────────────────────────────────
  const renderer = new THREE.WebGLRenderer({
    canvas,
    antialias: true,
    alpha: true,
    powerPreference: 'high-performance',
  });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  renderer.setClearColor(0x000000, 0);
  renderer.shadowMap.enabled = false;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.2;

  // ─── Scene / Camera ─────────────────────────────────────────────────
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(40, canvas.clientWidth / canvas.clientHeight, 0.1, 100);
  camera.position.set(0, 0, 7);

  // ─── Lights ─────────────────────────────────────────────────────────
  const ambLight = new THREE.AmbientLight(0xffffff, 0.3);
  scene.add(ambLight);

  const keyLight = new THREE.PointLight(0x8877ff, 3, 20);
  keyLight.position.set(3, 4, 4);
  scene.add(keyLight);

  const fillLight = new THREE.PointLight(0x55d6ff, 1.5, 20);
  fillLight.position.set(-4, -2, 3);
  scene.add(fillLight);

  const rimLight = new THREE.PointLight(0x6d5df6, 2, 18);
  rimLight.position.set(0, -5, -4);
  scene.add(rimLight);

  // ─── Crystal (smooth icosahedron) ───────────────────────────────────
  const icoGeo = new THREE.IcosahedronGeometry(1.15, 2);

  // Slightly distort vertices for organic feel
  const posAttr = icoGeo.attributes.position;
  for (let i = 0; i < posAttr.count; i++) {
    const noise = (Math.random() - 0.5) * 0.06;
    posAttr.setXYZ(i, posAttr.getX(i) + noise, posAttr.getY(i) + noise, posAttr.getZ(i) + noise);
  }
  icoGeo.computeVertexNormals();

  const crystalMat = new THREE.MeshPhysicalMaterial({
    color: 0xffffff,
    metalness: 0.05,
    roughness: 0.0,
    transmission: 0.92,
    thickness: 1.6,
    ior: 1.55,
    clearcoat: 1.0,
    clearcoatRoughness: 0.05,
    reflectivity: 0.85,
    envMapIntensity: 1.0,
    transparent: true,
    opacity: 0.88,
  });

  const crystal = new THREE.Mesh(icoGeo, crystalMat);
  scene.add(crystal);

  // Inner glow sphere
  const glowGeo = new THREE.SphereGeometry(0.75, 32, 32);
  const glowMat = new THREE.MeshBasicMaterial({
    color: 0x6d5df6,
    transparent: true,
    opacity: 0.06,
  });
  const innerGlow = new THREE.Mesh(glowGeo, glowMat);
  scene.add(innerGlow);

  // ─── Orbital Rings ──────────────────────────────────────────────────
  const ringGroup = new THREE.Group();
  scene.add(ringGroup);

  function makeRing(radius, tube, color, opacity, rotX, rotZ) {
    const geo = new THREE.TorusGeometry(radius, tube, 6, 128);
    const mat = new THREE.MeshBasicMaterial({ color, transparent: true, opacity });
    const mesh = new THREE.Mesh(geo, mat);
    mesh.rotation.x = rotX;
    mesh.rotation.z = rotZ;
    return mesh;
  }

  const ring1 = makeRing(2.2, 0.012, 0x6d5df6, 0.55, Math.PI / 2.5, 0.4);
  const ring2 = makeRing(2.7, 0.008, 0x55d6ff, 0.35, Math.PI / 1.4, -0.5);
  const ring3 = makeRing(1.85, 0.018, 0xa896ff, 0.4,  0.5, Math.PI / 3);
  ringGroup.add(ring1, ring2, ring3);

  // ─── Floating Particles ─────────────────────────────────────────────
  const isMobile = window.innerWidth < 768;
  const particleCount = isMobile ? 60 : 160;
  const pPositions = new Float32Array(particleCount * 3);
  const pSizes = new Float32Array(particleCount);
  const pColors = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount; i++) {
    const theta = Math.random() * Math.PI * 2;
    const phi   = Math.acos(2 * Math.random() - 1);
    const r     = 2.5 + Math.random() * 2.5;
    pPositions[i * 3]     = r * Math.sin(phi) * Math.cos(theta);
    pPositions[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
    pPositions[i * 3 + 2] = r * Math.cos(phi);
    pSizes[i] = Math.random() * 2.5 + 0.8;
    // Color: mix accent purple and cyan
    const t = Math.random();
    pColors[i * 3]     = 0.43 * (1 - t) + 0.33 * t; // r
    pColors[i * 3 + 1] = 0.36 * (1 - t) + 0.84 * t; // g
    pColors[i * 3 + 2] = 0.96 * (1 - t) + 1.0  * t; // b
  }

  const pGeo = new THREE.BufferGeometry();
  pGeo.setAttribute('position', new THREE.BufferAttribute(pPositions, 3));
  pGeo.setAttribute('size', new THREE.BufferAttribute(pSizes, 1));
  pGeo.setAttribute('color', new THREE.BufferAttribute(pColors, 3));

  const pMat = new THREE.PointsMaterial({
    size: isMobile ? 0.025 : 0.018,
    transparent: true,
    opacity: 0.65,
    vertexColors: true,
    sizeAttenuation: true,
    depthWrite: false,
  });

  const particles = new THREE.Points(pGeo, pMat);
  scene.add(particles);

  // ─── Mouse parallax ─────────────────────────────────────────────────
  let targetX = 0, targetY = 0;
  let currentX = 0, currentY = 0;

  if (!isMobile) {
    window.addEventListener('mousemove', (e) => {
      targetX = (e.clientX / window.innerWidth - 0.5) * 2;
      targetY = (e.clientY / window.innerHeight - 0.5) * 2;
    });
  }

  // ─── Clock / RAF ────────────────────────────────────────────────────
  const clock = new THREE.Clock();
  let animId = null;

  function animate() {
    animId = requestAnimationFrame(animate);
    if (document.hidden) return;

    const t = clock.getElapsedTime();

    // Crystal slow rotation
    crystal.rotation.y = t * 0.12;
    crystal.rotation.x = Math.sin(t * 0.07) * 0.18;
    crystal.rotation.z = Math.cos(t * 0.05) * 0.08;

    // Inner glow pulse
    innerGlow.material.opacity = 0.04 + Math.sin(t * 0.9) * 0.025;
    innerGlow.scale.setScalar(0.9 + Math.sin(t * 0.7) * 0.06);

    // Ring orbits
    ring1.rotation.y = t * 0.18;
    ring2.rotation.y = -t * 0.12;
    ring3.rotation.x = t * 0.14 + 0.5;

    // Particles drift
    particles.rotation.y = t * 0.04;
    particles.rotation.x = t * 0.02;

    // Key light orbit
    keyLight.position.x = Math.sin(t * 0.35) * 5;
    keyLight.position.z = Math.cos(t * 0.35) * 5;

    // Mouse parallax — smooth lerp
    currentX += (targetX - currentX) * 0.04;
    currentY += (targetY - currentY) * 0.04;
    camera.position.x = currentX * 0.9;
    camera.position.y = -currentY * 0.7;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
  }

  animate();

  // ─── Resize ─────────────────────────────────────────────────────────
  function onResize() {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  }
  window.addEventListener('resize', onResize);

  // ─── Visibility pause ───────────────────────────────────────────────
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) { cancelAnimationFrame(animId); }
    else { animate(); }
  });

})();
