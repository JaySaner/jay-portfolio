import re

css_file = 'd:\\Jay_new_portfoliowebsite\\css\\style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = r'/\* ─── PROJECTS ─── \*/'
end_marker = r'/\* ─── EXPERIENCE TIMELINE ─── \*/'

new_css = """/* ─── PROJECTS ─── */
.filter-tabs {
  display: flex;
  gap: var(--sp2);
  margin-bottom: var(--sp6);
  flex-wrap: wrap;
}
.filter-btn {
  font-family: var(--font-head);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-3);
  background: var(--bg-1);
  border: var(--border);
  padding: 0.5rem 1.25rem;
  border-radius: 100px;
  transition: all 0.2s var(--ease);
  cursor: pointer;
}
.filter-btn:hover { color: var(--text-1); border-color: rgba(255,255,255,0.2); }
.filter-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }
.filter-btn.hidden-filter { opacity: 0.2; pointer-events: none; }

/* Masonry Grid */
.projects-masonry {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--sp4);
  margin-bottom: var(--sp6);
}

/* PCard Base */
.pcard {
  position: relative;
  background: var(--bg-1);
  border: var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: transform 0.4s var(--ease), border-color 0.4s var(--ease), box-shadow 0.4s var(--ease);
  display: flex;
  flex-direction: column;
}
.pcard:hover {
  transform: translateY(-6px);
  border-color: rgba(109,93,246,0.4);
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}
.pcard-featured {
  grid-column: 1 / -1;
}

/* Image & Overlay */
.pcard-img {
  position: relative;
  width: 100%;
  aspect-ratio: 16/10;
  overflow: hidden;
  background: var(--bg-2);
}
.pcard-featured .pcard-img { aspect-ratio: 21/9; }

.pcard-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  transition: transform 0.7s var(--ease);
}
.pcard:hover .pcard-img img {
  transform: scale(1.05);
}

.pcard-overlay {
  position: absolute;
  inset: 0;
  background: rgba(6, 7, 10, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: var(--sp4);
  opacity: 0;
  transition: opacity 0.4s var(--ease);
}
.pcard:hover .pcard-overlay { opacity: 1; }

.pcard-overlay-inner {
  transform: translateY(20px);
  transition: transform 0.4s var(--ease);
}
.pcard:hover .pcard-overlay-inner {
  transform: translateY(0);
}

.pcard-num {
  font-family: var(--font-head);
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.1em;
  margin-bottom: 0.5rem;
  display: block;
}

.pcard-overlay-tags {
  display: flex;
  gap: 0.5rem;
  margin-bottom: var(--sp2);
  flex-wrap: wrap;
}
.ptag {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  background: rgba(255,255,255,0.1);
  color: var(--text-1);
}
.ptag-ai { background: rgba(109,93,246,0.2); color: #a59efc; }
.ptag-hackathon { background: rgba(85,214,255,0.2); color: #8ce1ff; }
.ptag-client { background: rgba(34,197,94,0.2); color: #4ade80; }
.ptag-tools { background: rgba(245,158,11,0.2); color: #fbbf24; }

.pcard-overlay h3 {
  font-family: var(--font-head);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-1);
  margin-bottom: 0.5rem;
}
.pcard-featured .pcard-overlay h3 { font-size: 2rem; }

.pcard-overlay p {
  font-size: 0.95rem;
  color: var(--text-2);
  margin-bottom: var(--sp3);
  max-width: 600px;
  line-height: 1.6;
}

.pcard-stack-inline {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: var(--sp3);
}
.pcard-stack-inline span {
  font-size: 0.75rem;
  color: var(--text-3);
  background: var(--bg-0);
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  border: var(--border);
}

.pcard-link {
  display: inline-flex;
  align-items: center;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-1);
  transition: color 0.2s;
}
.pcard-link:hover { color: var(--accent); }

/* Footer bar (visible when not hovered) */
.pcard-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--sp3);
  background: var(--bg-1);
  border-top: var(--border);
}
.pcard-label {
  display: block;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-3);
  margin-bottom: 0.2rem;
}
.pcard-title {
  font-family: var(--font-head);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-1);
}
.pcard-arrow {
  width: 2.5rem; height: 2.5rem;
  border-radius: 50%;
  border: var(--border);
  display: flex; align-items: center; justify-content: center;
  color: var(--text-2);
  transition: all 0.3s;
}
.pcard:hover .pcard-arrow {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
  transform: rotate(45deg);
}

/* WIDE DARK CARDS (Chatbot / Multi-Client) */
.pcard-wide {
  grid-column: 1 / -1;
  background: linear-gradient(135deg, #0e0820 0%, #1a1040 100%);
  border: 1px solid rgba(109,93,246,0.3);
  display: flex;
  flex-direction: row;
}
.pcard-dark-alt {
  background: linear-gradient(135deg, #0a1520 0%, #0d1e30 100%);
  border-color: rgba(85,214,255,0.3);
}
.pcard-dark-inner {
  display: flex;
  width: 100%;
  padding: var(--sp5);
  gap: var(--sp5);
  align-items: center;
}
.pcard-dark-icon {
  flex-shrink: 0;
  width: 72px; height: 72px;
  background: rgba(0,0,0,0.3);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: var(--radius-lg);
  display: flex; align-items: center; justify-content: center;
  color: var(--text-1);
}
.pcard-dark-content {
  flex: 1;
}
.pcard-dark-title {
  font-family: var(--font-head);
  font-size: 1.75rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.5rem;
}
.pcard-dark-desc {
  font-size: 1rem;
  color: rgba(255,255,255,0.7);
  line-height: 1.6;
}
.pcard-dark-visual {
  flex-shrink: 0;
  width: 300px;
  background: rgba(0,0,0,0.4);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: var(--radius-lg);
  padding: var(--sp3);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.chat-bubble {
  padding: 0.5rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  max-width: 85%;
}
.chat-bubble.bot { background: rgba(255,255,255,0.1); color: var(--text-2); align-self: flex-start; border-bottom-left-radius: 2px; }
.chat-bubble.user { background: var(--accent); color: #fff; align-self: flex-end; border-bottom-right-radius: 2px; }
.chat-typing {
  display: flex; gap: 4px; padding: 0.5rem; background: rgba(255,255,255,0.05);
  border-radius: 12px; width: fit-content; border-bottom-left-radius: 2px;
}
.chat-typing span { width: 4px; height: 4px; background: rgba(255,255,255,0.3); border-radius: 50%; }

.pcard-dark-visual-grid {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.mini-site {
  background: rgba(255,255,255,0.05);
  border-radius: 6px;
  height: 60px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.ms-bar { height: 12px; background: rgba(109,93,246,0.5); }
.ms-content { padding: 6px; display: flex; gap: 6px; flex: 1; }
.ms-content div { background: rgba(255,255,255,0.05); border-radius: 2px; height: 100%; flex: 1; }

.github-cta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--bg-1);
  border: var(--border);
  border-radius: var(--radius-lg);
  padding: var(--sp4) var(--sp5);
  flex-wrap: wrap;
  gap: var(--sp3);
}
.github-cta p { font-size: 1.05rem; color: var(--text-2); }

@media (max-width: 1024px) {
  .projects-masonry { grid-template-columns: 1fr; }
  .pcard-wide { flex-direction: column; }
  .pcard-dark-inner { flex-direction: column; text-align: center; }
  .pcard-dark-icon { margin: 0 auto; }
  .pcard-overlay-tags, .pcard-stack-inline { justify-content: center; }
  .pcard-dark-visual { width: 100%; max-width: 400px; margin: 0 auto; }
}

/* ─── EXPERIENCE TIMELINE ─── */"""

new_content = re.sub(start_marker + r'.*?' + end_marker, new_css, content, flags=re.DOTALL)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
