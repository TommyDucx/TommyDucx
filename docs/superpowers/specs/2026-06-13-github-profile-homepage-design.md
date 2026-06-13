# GitHub Profile Homepage Design

Date: 2026-06-13

## Goal

Build a single-page GitHub Pages personal homepage for Du Chengxuan, a high school student with an interdisciplinary academic orientation. The page should present curiosity, learning discipline, and early research/project exploration without overstating credentials or inventing unverified achievements.

The site will use Chinese-first bilingual copy, with English support for academic and international readability.

## Audience

Primary audiences:

- Teachers, mentors, and peers who want to understand Chengxuan's interests and work.
- Future collaborators reviewing projects or notes on GitHub.
- Academic or program reviewers who need a concise, credible personal overview.

Secondary audiences:

- Friends or classmates looking for links to projects, notes, or contact information.

## Positioning

Core identity:

- Chinese: 杜承轩，高中生，跨学科探索者。
- English: Chengxuan Du, high school student and interdisciplinary explorer.

Tone:

- Curious, precise, reflective, and grounded.
- Serious enough for academic contexts, but age-appropriate for a high school student.
- Avoid exaggerated claims such as "researcher" unless supported by uploaded materials.

## Visual Direction

The homepage will use a modern technology style:

- Clean light interface with subtle blue, cyan, and green accents.
- Fine borders, soft shadows, and structured spacing.
- Code/research-inspired details such as small labels, metadata rows, or terminal-like text accents.
- No heavy cyberpunk visuals, large decorative gradients, or visual clutter.

The design should feel like a personal research lab notebook translated into a polished web page.

## Page Structure

### 1. Hero

Purpose:

- Establish identity immediately.
- Show bilingual name and one concise positioning statement.
- Provide quick links.

Content:

- Name: 杜承轩 / Chengxuan Du
- Role: 高中生 / High School Student
- Positioning: 跨学科探索者 / Interdisciplinary Explorer
- Short intro about using projects, reading, and experiments to understand science, technology, and society.
- Links: GitHub, Email, Projects, Notes.

### 2. About

Purpose:

- Explain who Chengxuan is in a grounded way.
- Emphasize curiosity, independent learning, and record-keeping.

Content:

- Chinese paragraph first.
- Short English companion paragraph.
- Placeholder-friendly copy that can be refined after the user uploads personal materials.

### 3. Exploration Areas

Purpose:

- Show interdisciplinary breadth without forcing a fixed major or research domain.

Initial areas:

- Science & Technology
- AI & Computing
- Humanities & Society
- Research Notes

Each area should have a short Chinese description and a compact English label.

### 4. Selected Projects

Purpose:

- Provide a portfolio section even before final personal materials are uploaded.
- Use clearly marked placeholders where project details are not yet confirmed.

Initial placeholder projects:

- 跨学科阅读笔记 / Interdisciplinary Reading Notes
- AI 小实验 / AI Mini Experiments
- 科学问题观察记录 / Scientific Question Log

After the user uploads materials, replace placeholders with real project names, descriptions, links, dates, and outcomes.

### 5. Notes & Learning

Purpose:

- Make the homepage maintainable over time.
- Provide a natural place for future reading notes, course summaries, and research reflections.

Content:

- Reading notes
- Course learning
- Research questions
- Short essays or reflections

### 6. Contact

Purpose:

- Give simple ways to connect.

Content:

- GitHub profile link.
- Email address placeholder until provided.
- Optional social or academic links if the user later provides them.

## Content Rules

- Do not invent awards, schools, projects, publications, affiliations, or research experience.
- Use placeholders only where personal information is missing.
- Treat uploaded materials as source material and rewrite them into concise website copy.
- Keep Chinese as the primary language; include English labels or short English summaries for each major section.
- Make it easy for the user to replace placeholder text later.

## Technical Direction

First implementation should be a simple static site:

- `index.html`
- `style.css`
- Optional `assets/` folder for a future avatar or visual assets.

No framework is needed for the first version. This keeps deployment to GitHub Pages simple and makes the files easy to edit.

The page should work by opening `index.html` directly in a browser and should also be ready for GitHub Pages hosting.

## Responsiveness

The design must work on:

- Mobile phones.
- Tablets.
- Desktop screens.

Expected responsive behavior:

- Hero content stacks cleanly on small screens.
- Cards use one column on mobile and multiple columns on desktop.
- Text never overflows buttons, cards, or labels.
- Navigation remains simple and usable.

## Verification

Before calling implementation complete:

- Open the local page in a browser.
- Check desktop and mobile viewport screenshots.
- Confirm Chinese and English text render correctly.
- Confirm links have sensible placeholders or real URLs.
- Confirm layout has no overlap or unreadable text.

## Open Inputs From User

The following information will be incorporated later:

- GitHub username.
- Email or preferred contact method.
- Personal photo or avatar, if desired.
- Real projects, notes, awards, activities, or coursework.
- Any preferred English spelling of the name, if different from "Chengxuan Du".
