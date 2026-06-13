# GitHub Profile Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single-page GitHub Pages personal homepage for 杜承轩 / Chengxuan Du.

**Architecture:** The site is a static HTML/CSS page with no build step, so it can be opened directly and deployed to GitHub Pages. `index.html` owns page content and semantic structure; `style.css` owns layout, responsive behavior, and modern technology-inspired visual styling.

**Tech Stack:** HTML5, CSS3, local browser verification, Git.

---

## File Structure

- Create `index.html`: semantic single-page homepage with hero, about, exploration areas, selected projects, notes, and contact sections.
- Create `style.css`: responsive styling, color tokens, layout grids, button states, card styling, and mobile adjustments.
- Modify no existing application code. The existing design spec remains the source of truth.

## Implementation Tasks

### Task 1: Add Semantic Homepage HTML

**Files:**
- Create: `index.html`

- [ ] **Step 1: Create the complete static page structure**

Create `index.html` with this content:

```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta
      name="description"
      content="杜承轩 / Chengxuan Du 的个人主页：高中生，跨学科探索者，记录项目、阅读、实验与学习。"
    >
    <title>杜承轩 / Chengxuan Du</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="#top" aria-label="回到首页">CD</a>
      <nav class="site-nav" aria-label="主页导航">
        <a href="#about">About</a>
        <a href="#explore">Explore</a>
        <a href="#projects">Projects</a>
        <a href="#notes">Notes</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>

    <main id="top">
      <section class="hero section-shell" aria-labelledby="hero-title">
        <div class="hero-copy">
          <p class="eyebrow">High School Student · Interdisciplinary Explorer</p>
          <h1 id="hero-title">杜承轩 <span>Chengxuan Du</span></h1>
          <p class="hero-intro">
            我是一名高中生，正在通过项目、阅读与实验记录自己对科学、技术与社会问题的理解。
          </p>
          <p class="hero-intro english">
            I am a high school student exploring ideas across disciplines through projects, reading, and experiments.
          </p>
          <div class="hero-actions" aria-label="快速链接">
            <a class="button primary" href="https://github.com/" target="_blank" rel="noreferrer">GitHub</a>
            <a class="button" href="#projects">Projects</a>
            <a class="button" href="#notes">Notes</a>
          </div>
        </div>
        <aside class="status-panel" aria-label="个人状态摘要">
          <div class="panel-line">
            <span>Status</span>
            <strong>Learning in public</strong>
          </div>
          <div class="panel-line">
            <span>Focus</span>
            <strong>Science · AI · Society</strong>
          </div>
          <div class="panel-line">
            <span>Mode</span>
            <strong>Read → Build → Reflect</strong>
          </div>
        </aside>
      </section>

      <section id="about" class="content-section section-shell" aria-labelledby="about-title">
        <div class="section-heading">
          <p class="eyebrow">About</p>
          <h2 id="about-title">关于我</h2>
        </div>
        <div class="two-column">
          <p>
            我关注不同学科之间如何彼此连接：一个科学问题可能需要计算工具，一个技术项目也可能引出社会与伦理思考。这个主页会持续整理我的项目、阅读笔记和学习记录。
          </p>
          <p class="english">
            I am interested in how different fields connect. This site gathers my projects, reading notes, and learning records as my questions become clearer over time.
          </p>
        </div>
      </section>

      <section id="explore" class="content-section section-shell" aria-labelledby="explore-title">
        <div class="section-heading">
          <p class="eyebrow">Exploration Areas</p>
          <h2 id="explore-title">探索方向</h2>
        </div>
        <div class="card-grid">
          <article class="info-card">
            <span class="card-index">01</span>
            <h3>科学与技术</h3>
            <p>观察科学问题如何被建模、测量和解释。</p>
            <small>Science & Technology</small>
          </article>
          <article class="info-card">
            <span class="card-index">02</span>
            <h3>AI 与计算</h3>
            <p>用代码和小实验理解算法、数据与工具。</p>
            <small>AI & Computing</small>
          </article>
          <article class="info-card">
            <span class="card-index">03</span>
            <h3>人文与社会</h3>
            <p>思考技术变化与人的选择、制度和文化之间的关系。</p>
            <small>Humanities & Society</small>
          </article>
          <article class="info-card">
            <span class="card-index">04</span>
            <h3>研究笔记</h3>
            <p>把阅读、课程和问题意识整理成可回顾的记录。</p>
            <small>Research Notes</small>
          </article>
        </div>
      </section>

      <section id="projects" class="content-section section-shell" aria-labelledby="projects-title">
        <div class="section-heading">
          <p class="eyebrow">Selected Projects</p>
          <h2 id="projects-title">项目与记录</h2>
        </div>
        <div class="project-list">
          <article class="project-card">
            <div>
              <span class="tag">Reading</span>
              <h3>跨学科阅读笔记</h3>
            </div>
            <p>整理科学、技术与社会主题的阅读摘录、问题和短评。</p>
            <a href="#notes">查看笔记入口</a>
          </article>
          <article class="project-card">
            <div>
              <span class="tag">Experiment</span>
              <h3>AI 小实验</h3>
            </div>
            <p>通过小型编程实验理解模型、数据和交互式工具的工作方式。</p>
            <a href="#contact">等待更新</a>
          </article>
          <article class="project-card">
            <div>
              <span class="tag">Question Log</span>
              <h3>科学问题观察记录</h3>
            </div>
            <p>记录日常学习中遇到的科学问题，并尝试拆解成可研究的小问题。</p>
            <a href="#contact">等待更新</a>
          </article>
        </div>
      </section>

      <section id="notes" class="content-section section-shell" aria-labelledby="notes-title">
        <div class="section-heading">
          <p class="eyebrow">Notes & Learning</p>
          <h2 id="notes-title">笔记与学习</h2>
        </div>
        <div class="note-panel">
          <p>
            这里将逐步收集阅读笔记、课程总结、研究问题和短文反思。当前版本先保留清晰入口，后续可以连接到 GitHub 仓库、Markdown 笔记或独立页面。
          </p>
          <ul>
            <li>Reading notes / 阅读笔记</li>
            <li>Course learning / 课程学习</li>
            <li>Research questions / 研究问题</li>
            <li>Short reflections / 短文反思</li>
          </ul>
        </div>
      </section>

      <section id="contact" class="content-section section-shell contact-section" aria-labelledby="contact-title">
        <div class="section-heading">
          <p class="eyebrow">Contact</p>
          <h2 id="contact-title">联系</h2>
        </div>
        <p>
          如果你想交流项目、阅读或跨学科问题，可以通过 GitHub 或邮箱联系我。具体链接会在个人资料补充后更新。
        </p>
        <div class="contact-links">
          <a class="button primary" href="https://github.com/" target="_blank" rel="noreferrer">GitHub Profile</a>
          <a class="button" href="mailto:hello@example.com">Email Placeholder</a>
        </div>
      </section>
    </main>
  </body>
</html>
```

- [ ] **Step 2: Verify HTML file exists**

Run: `test -f index.html`

Expected: command exits with status `0`.

- [ ] **Step 3: Commit HTML structure**

Run:

```bash
git add index.html
git commit -m "Add homepage HTML structure"
```

Expected: commit succeeds with one created file.

### Task 2: Add Modern Technology Styling

**Files:**
- Create: `style.css`

- [ ] **Step 1: Create responsive CSS**

Create `style.css` with this content:

```css
:root {
  color-scheme: light;
  --bg: #f7fafc;
  --surface: #ffffff;
  --surface-strong: #eef7fb;
  --text: #142033;
  --muted: #5d6b7c;
  --line: #d8e5ee;
  --blue: #2563eb;
  --cyan: #0891b2;
  --green: #059669;
  --shadow: 0 20px 60px rgba(20, 32, 51, 0.1);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  color: var(--text);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background:
    linear-gradient(135deg, rgba(37, 99, 235, 0.08), transparent 36rem),
    linear-gradient(225deg, rgba(5, 150, 105, 0.08), transparent 32rem),
    var(--bg);
  line-height: 1.65;
}

a {
  color: inherit;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  width: min(1120px, calc(100% - 2rem));
  margin: 0 auto;
  padding: 1rem 0;
  backdrop-filter: blur(16px);
}

.brand {
  display: inline-grid;
  width: 2.75rem;
  height: 2.75rem;
  place-items: center;
  border: 1px solid var(--line);
  border-radius: 0.5rem;
  background: rgba(255, 255, 255, 0.86);
  color: var(--blue);
  font-weight: 800;
  text-decoration: none;
  box-shadow: 0 10px 24px rgba(37, 99, 235, 0.12);
}

.site-nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: 0.3rem;
}

.site-nav a {
  border-radius: 0.4rem;
  padding: 0.5rem 0.7rem;
  color: var(--muted);
  font-size: 0.92rem;
  text-decoration: none;
}

.site-nav a:hover,
.site-nav a:focus-visible {
  background: rgba(37, 99, 235, 0.08);
  color: var(--blue);
}

.section-shell {
  width: min(1120px, calc(100% - 2rem));
  margin: 0 auto;
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(280px, 0.65fr);
  gap: 2rem;
  align-items: center;
  min-height: calc(100vh - 5rem);
  padding: 4rem 0 3rem;
}

.eyebrow {
  margin: 0 0 0.85rem;
  color: var(--cyan);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0;
  text-transform: uppercase;
}

h1,
h2,
h3,
p {
  margin-top: 0;
}

h1 {
  max-width: 760px;
  margin-bottom: 1.2rem;
  font-size: clamp(3rem, 8vw, 6.6rem);
  line-height: 0.98;
  letter-spacing: 0;
}

h1 span {
  display: block;
  color: var(--muted);
  font-size: clamp(1.6rem, 4vw, 3.4rem);
  font-weight: 700;
}

h2 {
  margin-bottom: 0;
  font-size: clamp(1.8rem, 4vw, 3rem);
  line-height: 1.15;
}

h3 {
  margin-bottom: 0.55rem;
  font-size: 1.12rem;
  line-height: 1.25;
}

.hero-intro {
  max-width: 720px;
  margin-bottom: 0.75rem;
  color: var(--text);
  font-size: 1.18rem;
}

.english {
  color: var(--muted);
}

.hero-actions,
.contact-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.5rem;
}

.button {
  display: inline-flex;
  min-height: 2.75rem;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--line);
  border-radius: 0.5rem;
  padding: 0.65rem 1rem;
  background: rgba(255, 255, 255, 0.88);
  color: var(--text);
  font-weight: 750;
  text-decoration: none;
}

.button:hover,
.button:focus-visible {
  border-color: rgba(37, 99, 235, 0.45);
  color: var(--blue);
  transform: translateY(-1px);
}

.button.primary {
  border-color: transparent;
  background: var(--blue);
  color: #ffffff;
  box-shadow: 0 14px 28px rgba(37, 99, 235, 0.24);
}

.button.primary:hover,
.button.primary:focus-visible {
  color: #ffffff;
  background: #1d4ed8;
}

.status-panel,
.info-card,
.project-card,
.note-panel {
  border: 1px solid var(--line);
  border-radius: 0.5rem;
  background: rgba(255, 255, 255, 0.86);
  box-shadow: var(--shadow);
}

.status-panel {
  padding: 1.2rem;
}

.panel-line {
  display: grid;
  gap: 0.25rem;
  border-bottom: 1px solid var(--line);
  padding: 1rem 0;
}

.panel-line:first-child {
  padding-top: 0;
}

.panel-line:last-child {
  border-bottom: 0;
  padding-bottom: 0;
}

.panel-line span {
  color: var(--muted);
  font-size: 0.82rem;
}

.panel-line strong {
  font-size: 1rem;
}

.content-section {
  padding: 4.5rem 0;
}

.section-heading {
  margin-bottom: 1.5rem;
}

.two-column {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.5rem;
  max-width: 920px;
}

.two-column p,
.contact-section > p {
  font-size: 1.05rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
}

.info-card {
  min-height: 15rem;
  padding: 1.1rem;
}

.card-index,
.tag {
  display: inline-flex;
  margin-bottom: 1rem;
  border: 1px solid rgba(8, 145, 178, 0.24);
  border-radius: 0.35rem;
  padding: 0.18rem 0.45rem;
  background: var(--surface-strong);
  color: var(--cyan);
  font-size: 0.76rem;
  font-weight: 800;
}

.info-card p,
.project-card p {
  color: var(--muted);
}

.info-card small {
  color: var(--green);
  font-weight: 800;
}

.project-list {
  display: grid;
  gap: 1rem;
}

.project-card {
  display: grid;
  grid-template-columns: minmax(180px, 0.45fr) minmax(0, 1fr) auto;
  gap: 1rem;
  align-items: center;
  padding: 1.1rem;
}

.project-card p {
  margin-bottom: 0;
}

.project-card a {
  color: var(--blue);
  font-weight: 800;
  text-decoration: none;
}

.project-card a:hover,
.project-card a:focus-visible {
  text-decoration: underline;
}

.note-panel {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(220px, 0.5fr);
  gap: 1.5rem;
  padding: 1.3rem;
}

.note-panel p {
  margin-bottom: 0;
}

.note-panel ul {
  margin: 0;
  padding-left: 1.1rem;
  color: var(--muted);
}

.contact-section {
  padding-bottom: 6rem;
}

@media (max-width: 860px) {
  .site-header {
    align-items: flex-start;
  }

  .hero {
    grid-template-columns: 1fr;
    min-height: auto;
    padding-top: 2.5rem;
  }

  .two-column,
  .note-panel {
    grid-template-columns: 1fr;
  }

  .card-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .project-card {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 560px) {
  .site-header {
    position: static;
    display: grid;
  }

  .site-nav {
    justify-content: flex-start;
  }

  .site-nav a {
    padding: 0.42rem 0.5rem;
    font-size: 0.86rem;
  }

  .hero {
    padding-top: 1rem;
  }

  h1 {
    font-size: 3rem;
  }

  .hero-intro {
    font-size: 1.02rem;
  }

  .card-grid {
    grid-template-columns: 1fr;
  }

  .content-section {
    padding: 3rem 0;
  }
}
```

- [ ] **Step 2: Verify stylesheet is linked**

Run: `grep -n 'href="style.css"' index.html`

Expected: output includes `<link rel="stylesheet" href="style.css">`.

- [ ] **Step 3: Commit CSS styling**

Run:

```bash
git add style.css index.html
git commit -m "Style GitHub profile homepage"
```

Expected: commit succeeds with the created stylesheet.

### Task 3: Verify Static Site Quality

**Files:**
- Verify: `index.html`
- Verify: `style.css`

- [ ] **Step 1: Check expected section anchors**

Run:

```bash
grep -n 'id="about"\|id="explore"\|id="projects"\|id="notes"\|id="contact"' index.html
```

Expected: output includes all five section ids.

- [ ] **Step 2: Check no unresolved forbidden placeholders**

Run:

```bash
grep -RIn 'T[B]D\|TO[D]O\|FIX[M]E' index.html style.css docs/superpowers/specs docs/superpowers/plans
```

Expected: no output and exit status `1`.

- [ ] **Step 3: Start a local static server**

Run:

```bash
python3 -m http.server 8000
```

Expected: server starts and serves the site at `http://localhost:8000`.

- [ ] **Step 4: Browser-check the desktop layout**

Open `http://localhost:8000` in the browser at a desktop viewport.

Expected:

- Hero shows "杜承轩" and "Chengxuan Du".
- Navigation links jump to sections.
- Cards and project rows have no overlap.
- Chinese and English text render cleanly.

- [ ] **Step 5: Browser-check the mobile layout**

Open `http://localhost:8000` in a mobile viewport around 390px wide.

Expected:

- Header and navigation wrap cleanly.
- Hero stacks above the status panel.
- Exploration cards become a single column.
- Project rows become single-column cards.
- Buttons and long English labels stay inside their containers.

- [ ] **Step 6: Commit any verification fixes**

If verification requires edits, run:

```bash
git add index.html style.css
git commit -m "Polish homepage responsive layout"
```

Expected: commit succeeds only if files changed. If no fixes are required, skip this step.

## Final Delivery

Report:

- Created files: `index.html`, `style.css`.
- Local preview URL used during verification.
- Any remaining placeholders requiring user-provided personal information: GitHub username, email, avatar, real projects, notes, awards, activities, coursework, and preferred English name spelling if different.
