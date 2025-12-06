<!-- Sync Impact Report:
Version change: None -> 1.0.0
Modified principles:
  - PROJECT_NAME: AI/Spec-Driven Book
  - PRINCIPLE_1_NAME: Spec-first
  - PRINCIPLE_2_NAME: 100% Reproducible
  - PRINCIPLE_3_NAME: Zero Manual Edits
  - PRINCIPLE_4_NAME: Quality & Performance
  - PRINCIPLE_5_NAME: Content Standards
  - PRINCIPLE_6_NAME: Operational Constraints
  - SECTION_2_NAME: Deployment & Validation
Added sections: None
Removed sections: SECTION_3_NAME, SECTION_3_CONTENT
Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/templates/commands/sp.phr.md ⚠ pending
Follow-up TODOs:
  - TODO(FILES_YAML): Needs to be updated with modified files.
  - TODO(TESTS_YAML): Needs to be updated with tests run.
  - TODO(LABELS): Needs to be updated with relevant labels.
  - TODO(USER): Needs to be updated with the git user name.
-->
# AI/Spec-Driven Book Constitution

## Core Principles

### Spec-first
Nothing gets written without an approved .spec.md

### 100% Reproducible
A fresh clone, `npm ci`, and `npm run build` must produce the exact same book.

### Zero Manual Edits
There must be zero manual edits in `/website` or generated files.

### Quality & Performance
The book must be clean, modern, and fast. Lighthouse Performance must be ≥ 90, and Accessibility ≥ 95.

### Content Standards
- Content must be in MDX only (`/docs` folder).
- Specs must be in the `/specs` folder.
- Docusaurus 3 (Classic template) must be used.
- The default Docusaurus theme with minimal custom CSS is required.
- All code blocks must be highlighted and testable when possible.
- Text is CC-BY-SA 4.0, and code snippets are MIT licensed.

### Operational Constraints
- No new content or feature without prior approved spec.
- Sidebar nesting must be ≤ 3 levels.
- Build time must be < 2 minutes.
- Mobile-responsive design is required (default theme is acceptable).

## Deployment & Validation

- Deployment must be via GitHub Actions to GitHub Pages.
- The site must be live at https://<user>.github.io/<repo>/.
- `npm run build` must succeed with zero errors.
- A fresh clone, `npm install`, and `npm run start` must work perfectly.
- There must be a minimum of 5 complete chapters.
- Every file must trace back to its origin.

## Governance
This Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All Pull Requests and code reviews must verify compliance with these principles. Complexity must be justified.

**Version**: 1.0.0 | **Ratified**: 2025-12-05 | **Last Amended**: 2025-12-05
