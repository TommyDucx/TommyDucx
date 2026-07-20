# GitHub Profile README Design

Date: 2026-07-20

## Goal

Create a GitHub Profile README for `TommyDucx/TommyDucx` that appears on `https://github.com/TommyDucx` and presents Chengxuan Du / 杜承轩 as a bilingual high school student, interdisciplinary explorer, robotics innovator, and machine learning learner-builder.

The README should be inspired by the compact GitHub profile style seen on ConardLi's profile: clear personal identity, concise motto, visual GitHub stats, project highlights, and links. It must not copy ConardLi's wording, layout assets, or personal content.

## Confirmed Inputs

- GitHub username: `TommyDucx`
- Display name: `Chengxuan Du / 杜承轩`
- Primary format: GitHub Profile README, not the existing `index.html` site
- Language: bilingual Chinese and English, side-by-side or closely paired
- Tone:综合型, balancing research, projects, and personal growth
- Reference style: ConardLi's GitHub profile approach, especially concise identity, quote/motto, stats cards, and highlighted repositories
- Existing personal site files: `index.html` and `style.css`
- Research source folder: `/Users/tommydu/Desktop/MLForTommy`

## Audience

Primary audiences:

- GitHub visitors who want a fast overview of TommyDucx.
- Teachers, mentors, peers, and collaborators reviewing research/project work.
- People interested in beginner-friendly machine learning and federated learning demos.

Secondary audiences:

- Future program or competition reviewers looking for a concise public profile.
- Users who may continue from GitHub profile to the static personal website.

## Positioning

Core identity:

- English: High school student exploring AI, machine learning, federated learning, robotics, and interdisciplinary research.
- Chinese: 一名关注 AI、机器学习、联邦学习、机器人与跨学科研究的高中生。

Personal arc:

- Started from robotics and innovation practice.
- Built an interest in machine learning and federated learning.
- Uses code, experiments, visualizations, and reports to make abstract ideas understandable.

Important boundary:

- Avoid overstating credentials. Use "student", "explorer", "learner-builder", "project author", or "builder of learning demos" rather than unsupported labels like "AI researcher" unless the user later provides stronger evidence.

## README Structure

### 1. Header

Purpose:

- Immediately establish identity and direction.

Content:

- `Hi, I'm Chengxuan Du / 杜承轩`
- One concise bilingual positioning line.
- A short motto connecting learning, building, and explaining.
- Optional badges for Python, Machine Learning, Federated Learning, Robotics, and GitHub Profile.

### 2. About Me

Purpose:

- Explain who Chengxuan is in a way that feels mature but still age-appropriate.

Content:

- English and Chinese short paragraphs.
- Mention high school student status.
- Mention interdisciplinary exploration.
- Mention movement from robotics innovation to AI/ML experiments.

### 3. Featured Research Project: MLForTommy

Purpose:

- Make `/Users/tommydu/Desktop/MLForTommy` the central research/project highlight.

Facts confirmed from the local project:

- A beginner-friendly machine learning and federated learning simulation framework.
- Designed for high school classroom-style explanation.
- Focus is understanding principles, not industrial accuracy.
- Has five modules:
  - datasets
  - models
  - trainers
  - analysis tools
  - visualization
- Includes scripts for:
  - Iris experiment
  - MNIST experiment
  - iWildCam experiment
  - breast cancer experiment
- Produces CSV data, curves, comparison charts, reports, and principle summaries.
- Example report compares single-machine training and federated learning:
  - single-machine accuracy: 92.12%
  - federated learning accuracy: 88.58%
  - single-machine final loss: 0.2866
  - federated learning final loss: 0.4895
- iWildCam federated simulation report includes:
  - 5 clients
  - 20 federated rounds
  - local image classification setup
  - final test accuracy reported as 50.00% in a small-data simulation

README presentation:

- Keep results compact and honest.
- Explain that lower or unstable accuracy in small federated experiments is part of the learning/demo value.
- Link to repository or placeholder until `MLForTommy` is published under GitHub.

### 4. Recognition

Purpose:

- Include verified public achievements without turning the profile into an award list.

Facts confirmed from the Shenzhen News / 创新南山 article:

- Recognized as Guangdong Province "Innovation Good Youngster" / 广东省“创新好少年”.
- In 2019, recognized as "深圳市南山区少年创新院小院士" and "中国少年科学院小院士".
- Reported achievements include:
  - 2 national championships in World Robot Contest education-ministry competition projects.
  - 2 championships in Guangdong Youth Robot Design Contest.
  - 1 third place in World Robot Contest Youth Design Contest Shenzhen station.
  - An intelligent backpack for improving load balance, with one utility model patent.

README presentation:

- Use a compact recognition section.
- Link to the public source: `https://www.sznews.com/news/content/2021-06/04/content_24272757.htm`
- Phrase as "reported by" or "publicly reported" where appropriate.

### 5. GitHub Stats And Tech Stack

Purpose:

- Match GitHub profile conventions and make the page visually active.

Content:

- GitHub stats image for `TommyDucx`.
- Top languages image for `TommyDucx`.
- Tech badges:
  - Python
  - NumPy
  - Matplotlib
  - Machine Learning
  - Federated Learning
  - Data Visualization
  - Robotics

Rules:

- External stats images should use well-known GitHub README badge/stat services.
- If a service fails, the README remains useful because core content is plain Markdown.

### 6. Learning Direction

Purpose:

- Show what Chengxuan is currently exploring.

Content:

- AI and machine learning fundamentals.
- Federated learning and privacy-preserving computation ideas.
- Robotics and intelligent systems.
- Interdisciplinary research, science communication, and education-friendly tools.

### 7. Links

Purpose:

- Provide clear next actions.

Links:

- GitHub: `https://github.com/TommyDucx`
- Personal site: if deployed later, link to GitHub Pages URL; until then, use relative link or omit.
- MLForTommy repository: use placeholder until the repository is published.
- Recognition source: Shenzhen News article.

## GitHub Profile Repository Requirements

To appear on GitHub profile Overview, the repository must be named exactly:

- `TommyDucx`

The README must live at:

- `README.md`

If the current workspace is not the `TommyDucx/TommyDucx` repository, implementation should still create `README.md` locally, but final instructions must explain that it needs to be pushed to a GitHub repository named `TommyDucx`.

## Automatic Research Update Workflow

User intent:

- When future work happens in `/Users/tommydu/Desktop/MLForTommy`, keep GitHub research achievements updated.

Design:

- Do not auto-push silently.
- Build a repeatable update workflow that can scan `MLForTommy` reports and refresh the Profile README research section.
- Prefer a script or documented checklist that:
  - reads `README.md` from `MLForTommy`
  - reads selected report files from `MLForTommy/outputs`
  - extracts concise project/result facts
  - updates a bounded section in the profile README between stable markers
  - shows a diff before commit/push
- Future pushes to GitHub should require explicit user confirmation unless the user later sets up a trusted automation.

Suggested markers:

```markdown
<!-- RESEARCH-RESULTS:START -->
...
<!-- RESEARCH-RESULTS:END -->
```

This keeps generated research updates separate from hand-written identity and recognition content.

## Content Rules

- Do not invent schools, awards, publications, repositories, email addresses, or affiliations.
- Keep wording age-appropriate for a high school student.
- Results from `MLForTommy` should be described as experiments, simulations, or learning frameworks unless publication/review evidence is provided.
- Keep Chinese and English aligned. English should not exaggerate beyond Chinese facts.
- Avoid copying ConardLi's wording or personal branding.

## Verification

Before calling implementation complete:

- Confirm `README.md` exists.
- Confirm it contains `TommyDucx`, `Chengxuan Du`, and `杜承轩`.
- Confirm it contains a visible MLForTommy section.
- Confirm it contains the Shenzhen News source link.
- Confirm no fake email or fake repository URL is introduced.
- Confirm Markdown has no unresolved placeholder markers such as unfinished notes or fix-me labels.
- Preview or inspect Markdown enough to ensure headings, lists, image links, and badges are well-formed.

## Open Inputs

The following can improve later versions:

- Whether `MLForTommy` is or will be published as a GitHub repository.
- Preferred personal motto.
- Preferred contact method.
- Whether to include GitHub Pages URL after deployment.
- Whether to set up an explicit automation for future profile updates.
