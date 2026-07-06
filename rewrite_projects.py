import re

html_file = 'd:\\Jay_new_portfoliowebsite\\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = r'<!-- ═══════════════════════════ PROJECTS ═══════════════════════════ -->'
end_marker = r'<!-- ═══════════════════════════ EXPERIENCE ═══════════════════════════ -->'

new_projects_section = """<!-- ═══════════════════════════ PROJECTS ═══════════════════════════ -->
  <section id="projects" class="section">
    <div class="container">
      <div class="section-header" data-reveal>
        <p class="section-eyebrow">Selected Work</p>
        <h2 class="section-heading">Projects that<br/>speak for themselves.</h2>
      </div>

      <!-- Filter tabs -->
      <div class="filter-tabs" data-reveal>
        <button class="filter-btn active" data-filter="all"       id="filter-all">All</button>
        <button class="filter-btn"        data-filter="client"    id="filter-client">Client Work</button>
        <button class="filter-btn"        data-filter="hackathon" id="filter-hackathon">Hackathon</button>
        <button class="filter-btn"        data-filter="ai"        id="filter-ai">AI</button>
        <button class="filter-btn"        data-filter="tools"     id="filter-tools">Tools</button>
      </div>

      <!-- ── NEW MASONRY GRID ── -->
      <div class="projects-masonry">

        <!-- 01: Dr. Makarand Portfolio -->
        <article class="pcard pcard-featured" data-cat="client" data-reveal data-delay="80" id="proj-dr-mak">
          <div class="pcard-img">
            <img src="assets/project/dr-mak.png" alt="Dr. Makarand Jawadekar Portfolio" />
            <div class="pcard-overlay">
              <div class="pcard-overlay-inner">
                <span class="pcard-num">01</span>
                <div class="pcard-overlay-tags"><span class="ptag ptag-client">Client Work</span></div>
                <h3>Dr. Makarand Jawadekar</h3>
                <p>Modern professional portfolio — GSAP animations, fully responsive, SEO-optimized, deployed on Vercel.</p>
                <div class="pcard-stack-inline"><span>HTML</span><span>CSS</span><span>JavaScript</span><span>GSAP</span><span>Vercel</span></div>
                <a href="https://dr-makarand-portfolio.vercel.app/" target="_blank" rel="noopener" class="pcard-link" id="drmak-live-btn">View Live ↗</a>
              </div>
            </div>
          </div>
          <div class="pcard-footer">
            <div><span class="pcard-label">Client Work</span><h3 class="pcard-title">Dr. Makarand — Portfolio</h3></div>
            <a href="https://dr-makarand-portfolio.vercel.app/" target="_blank" rel="noopener" class="pcard-arrow">↗</a>
          </div>
        </article>

        <!-- 02: Luminous Civic -->
        <article class="pcard" data-cat="ai hackathon" data-reveal id="proj-luminous-civic">
          <div class="pcard-img">
            <img src="assets/project/Luminous_civic.png" alt="Luminous Civic" />
            <div class="pcard-overlay">
              <div class="pcard-overlay-inner">
                <span class="pcard-num">02</span>
                <div class="pcard-overlay-tags"><span class="ptag ptag-ai">AI</span><span class="ptag ptag-hackathon">Hackathon</span></div>
                <h3>Luminous Civic</h3>
                <p>AI-driven civic complaint platform — auto-identifies infrastructure issues, maps authorities, and tracks resolution in real time.</p>
                <div class="pcard-stack-inline"><span>Python</span><span>FastAPI</span><span>Gemini API</span><span>CrewAI</span><span>Leaflet.js</span></div>
                <a href="https://luminous-civic.vercel.app/" target="_blank" rel="noopener" class="pcard-link" id="luminous-live-btn">View Live ↗</a>
              </div>
            </div>
          </div>
          <div class="pcard-footer">
            <div><span class="pcard-label">AI · Hackathon</span><h3 class="pcard-title">Luminous Civic</h3></div>
            <a href="https://luminous-civic.vercel.app/" target="_blank" rel="noopener" class="pcard-arrow">↗</a>
          </div>
        </article>

        <!-- 03: Chourangi Group -->
        <article class="pcard" data-cat="client" data-reveal data-delay="140" id="proj-chourangi">
          <div class="pcard-img">
            <img src="assets/project/Chourangi Grp.png" alt="Chourangi Group" />
            <div class="pcard-overlay">
              <div class="pcard-overlay-inner">
                <span class="pcard-num">03</span>
                <div class="pcard-overlay-tags"><span class="ptag ptag-client">Client Work</span></div>
                <h3>Chourangi Group</h3>
                <p>Corporate website spanning real estate, infrastructure, hospitality &amp; media. WordPress + SEO optimized.</p>
                <div class="pcard-stack-inline"><span>WordPress</span><span>Elementor</span><span>CSS</span><span>SEO</span></div>
                <a href="https://chourangi.com/" target="_blank" rel="noopener" class="pcard-link" id="chourangi-live-btn">View Live ↗</a>
              </div>
            </div>
          </div>
          <div class="pcard-footer">
            <div><span class="pcard-label">Client Work</span><h3 class="pcard-title">Chourangi Group — Corporate</h3></div>
            <a href="https://chourangi.com/" target="_blank" rel="noopener" class="pcard-arrow">↗</a>
          </div>
        </article>

        <!-- 04: AI Photo Generator -->
        <article class="pcard" data-cat="tools ai" data-reveal data-delay="80" id="proj-photogen">
          <div class="pcard-img">
            <img src="assets/project/photogen.png" alt="AI Photo Generator Tool" />
            <div class="pcard-overlay">
              <div class="pcard-overlay-inner">
                <span class="pcard-num">04</span>
                <div class="pcard-overlay-tags"><span class="ptag ptag-ai">AI</span><span class="ptag ptag-tools">Tool</span></div>
                <h3>AI Photo Generator</h3>
                <p>Web-based AI image generation tool with prompt engineering, style presets, and instant gallery download.</p>
                <div class="pcard-stack-inline"><span>JavaScript</span><span>Gemini API</span><span>HTML</span><span>CSS</span></div>
                <a href="#" class="pcard-link" id="photogen-live-btn">View Project ↗</a>
              </div>
            </div>
          </div>
          <div class="pcard-footer">
            <div><span class="pcard-label">AI · Tool</span><h3 class="pcard-title">AI Photo Generator</h3></div>
            <span class="pcard-arrow">↗</span>
          </div>
        </article>

        <!-- 05: BMM Badge Generator -->
        <article class="pcard" data-cat="ai hackathon" data-reveal data-delay="120" id="proj-bmm-badge">
          <div class="pcard-img">
            <img src="assets/project/BMM_badge.png" alt="BMM Badge Generator" />
            <div class="pcard-overlay">
              <div class="pcard-overlay-inner">
                <span class="pcard-num">05</span>
                <div class="pcard-overlay-tags"><span class="ptag ptag-ai">AI</span><span class="ptag ptag-hackathon">Hackathon</span></div>
                <h3>BMM Badge Generator</h3>
                <p>Badge creation platform for BMM Seattle 2026 — live preview, custom layouts, instant PNG download.</p>
                <div class="pcard-stack-inline"><span>HTML</span><span>Canvas API</span><span>Supabase</span><span>JS</span></div>
                <a href="https://bmm2026-badge-generator.vercel.app/" target="_blank" rel="noopener" class="pcard-link" id="bmm-badge-live-btn">View Live ↗</a>
              </div>
            </div>
          </div>
          <div class="pcard-footer">
            <div><span class="pcard-label">AI · Hackathon</span><h3 class="pcard-title">BMM Badge Generator</h3></div>
            <a href="https://bmm2026-badge-generator.vercel.app/" target="_blank" rel="noopener" class="pcard-arrow">↗</a>
          </div>
        </article>

        <!-- 06: HydroSense -->
        <article class="pcard" data-cat="hackathon ai" data-reveal data-delay="160" id="proj-hydrosense">
          <div class="pcard-img">
            <img src="assets/project/hydrosense.png" alt="HydroSense" />
            <div class="pcard-overlay">
              <div class="pcard-overlay-inner">
                <span class="pcard-num">06</span>
                <div class="pcard-overlay-tags"><span class="ptag ptag-hackathon">SIH</span><span class="ptag ptag-ai">IoT · AI</span></div>
                <h3>HydroSense</h3>
                <p>IoT smart water quality monitoring — real-time web dashboard with Firebase, Arduino &amp; ESP32 sensors.</p>
                <div class="pcard-stack-inline"><span>Arduino</span><span>ESP32</span><span>Firebase</span><span>Netlify</span></div>
                <a href="https://hydrosense-1.netlify.app/" target="_blank" rel="noopener" class="pcard-link" id="hydrosense-live-btn">View Live ↗</a>
              </div>
            </div>
          </div>
          <div class="pcard-footer">
            <div><span class="pcard-label">IoT · AI · Hackathon</span><h3 class="pcard-title">HydroSense</h3></div>
            <a href="https://hydrosense-1.netlify.app/" target="_blank" rel="noopener" class="pcard-arrow">↗</a>
          </div>
        </article>

        <!-- 07: AI Chatbot Development — WIDE DARK CARD -->
        <article class="pcard pcard-wide pcard-dark" data-cat="ai" data-reveal id="proj-chatbot">
          <div class="pcard-dark-inner">
            <div class="pcard-dark-icon">
              <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>
            </div>
            <div class="pcard-dark-content">
              <div class="pcard-overlay-tags" style="margin-bottom:.75rem;"><span class="ptag ptag-ai">AI · Multiple Clients</span></div>
              <h3 class="pcard-dark-title">AI Chatbot Development</h3>
              <p class="pcard-dark-desc">Custom LLM-powered chatbots deployed for multiple business clients — customer support automation, lead generation, and intelligent FAQ systems with natural conversation flows.</p>
              <div class="pcard-stack-inline" style="margin-top:1rem;"><span>OpenAI GPT</span><span>Gemini API</span><span>Langchain</span><span>Python</span><span>Node.js</span><span>Twilio</span></div>
            </div>
            <div class="pcard-dark-visual">
              <div class="chat-bubble bot">Hello! How can I help you today?</div>
              <div class="chat-bubble user">I need support with my order.</div>
              <div class="chat-bubble bot">Sure! Let me pull up your details...</div>
              <div class="chat-bubble user">Thanks!</div>
              <div class="chat-typing"><span></span><span></span><span></span></div>
            </div>
          </div>
        </article>

        <!-- 08: Multi-Client Web Dev — WIDE DARK CARD -->
        <article class="pcard pcard-wide pcard-dark pcard-dark-alt" data-cat="client" data-reveal data-delay="100" id="proj-client-web">
          <div class="pcard-dark-inner">
            <div class="pcard-dark-icon">
              <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="3" rx="2"/><path d="M8 21h8"/><path d="M12 17v4"/></svg>
            </div>
            <div class="pcard-dark-content">
              <div class="pcard-overlay-tags" style="margin-bottom:.75rem;"><span class="ptag ptag-client">Client Work · Ongoing</span></div>
              <h3 class="pcard-dark-title">Multi-Client Web Dev &amp; Maintenance</h3>
              <p class="pcard-dark-desc">Ongoing development and maintenance for multiple clients across industries — delivering business sites, landing pages, performance fixes, SEO improvements, and feature updates.</p>
              <div class="pcard-stack-inline" style="margin-top:1rem;"><span>HTML</span><span>CSS</span><span>JavaScript</span><span>WordPress</span><span>React</span><span>SEO</span><span>Git</span></div>
            </div>
            <div class="pcard-dark-visual pcard-dark-visual-grid">
              <div class="mini-site"><div class="ms-bar"></div><div class="ms-content"><div></div><div></div></div></div>
              <div class="mini-site"><div class="ms-bar" style="background:rgba(85,214,255,0.5);"></div><div class="ms-content"><div></div><div></div></div></div>
              <div class="mini-site"><div class="ms-bar" style="background:rgba(34,197,94,0.5);"></div><div class="ms-content"><div></div><div></div></div></div>
            </div>
          </div>
        </article>

      </div><!-- /projects-masonry -->

      <!-- GitHub CTA -->
      <div class="github-cta" data-reveal>
        <p>And many more projects built for real clients.</p>
        <a href="https://github.com/JaySaner" target="_blank" rel="noopener" class="btn primary" id="github-btn">View GitHub →</a>
      </div>

    </div>
  </section>
  
  <!-- ═══════════════════════════ EXPERIENCE ═══════════════════════════ -->"""

new_content = re.sub(start_marker + r'.*?' + end_marker, new_projects_section, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
