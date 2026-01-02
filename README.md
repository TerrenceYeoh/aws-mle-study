# AWS MLE Study - Concept Maps

Study materials for the AWS Certified Machine Learning Engineer - Associate (MLA-C01) exam.

---

## Contents

```
AWS MLE Study/
├── README.md                        ← You are here
├── PLAN.md                          ← Processing progress tracker
├── data/learning_material/          ← Source PDFs
└── concept_map/
    ├── 00-master-concept-map.md     ← Overview of all sections
    ├── sections/                    ← 13 section-specific notes
    │   ├── 01-introduction/
    │   ├── 02-data-ingestion/
    │   ├── 03-data-transformation/
    │   ├── 04-managed-ai-services/
    │   ├── 05-sagemaker-algorithms/
    │   ├── 06-model-training/
    │   ├── 07-genai-fundamentals/
    │   ├── 08-bedrock-applications/
    │   ├── 09-mlops/
    │   ├── 10-security-compliance/
    │   ├── 11-management-governance/
    │   ├── 12-ml-best-practices/
    │   └── 13-exam-preparation/
    └── consolidated/                ← Quick reference materials
        ├── all-service-comparisons.md
        └── quick-reference.md
```

Each section contains:
- `concept-map.md` - Concepts, relationships, and exam tips
- `comparison-tables.md` - Service comparisons and decision tables

---

## Using with Obsidian (Recommended)

These notes use `[[wiki-style]]` links that work best with [Obsidian](https://obsidian.md/), a free knowledge management app.

### Setup

1. **Download Obsidian** (free): https://obsidian.md/

2. **Open as Vault**:
   - Launch Obsidian
   - Click "Open folder as vault"
   - Select the `concept_map/` folder (not the root folder)

3. **Done!** All notes are now linked and searchable.

> **Note:** Open `concept_map/` as the vault, not the root `AWS MLE Study/` folder. This keeps the graph focused on study notes only.

---

### Using the Graph View

The **Graph View** visualizes how concepts connect across all notes.

**To open:**
- Press `Ctrl+G` (Windows/Linux) or `Cmd+G` (Mac)
- Or click the graph icon in the left sidebar

**What you'll see:**
```
         ┌─────────┐
         │   S3    │──────────┐
         └────┬────┘          │
              │               │
    ┌─────────▼─────────┐     │
    │    SageMaker      │◄────┤
    └─────────┬─────────┘     │
              │               │
         ┌────▼────┐     ┌────▼────┐
         │  Glue   │     │   IAM   │
         └─────────┘     └─────────┘
```

- **Nodes** = Notes/concepts
- **Lines** = `[[links]]` between them
- **Clusters** = Related concepts grouped together
- **Node size** = More connections = larger node

**Graph Controls:**
| Action | Result |
|--------|--------|
| Scroll | Zoom in/out |
| Drag background | Pan view |
| Drag node | Move node |
| Click node | Open that note |
| Hover node | Highlight connections |

**Filters (in graph settings):**
- Filter by folder (e.g., only `sections/` or `consolidated/`)
- Filter by tag
- Show/hide orphan notes
- Adjust link distance and node size

---

### Local Graph View

See connections for **just the current note**:

1. Open any note
2. Click the "more options" menu (three dots)
3. Select "Open local graph"

This shows only concepts directly linked to/from the current note - useful for focused study.

---

### Useful Obsidian Features for Studying

#### Backlinks Panel
See "what links to this note" in the right sidebar. Helps answer: "Where else is S3 mentioned?"

#### Quick Switcher
Press `Ctrl+O` to quickly jump to any note by typing its name.

#### Search
Press `Ctrl+Shift+F` to search across all notes. Useful queries:
- `tag:#exam-tip` - Find all exam tips
- `"SageMaker"` - Find exact phrase
- `path:consolidated` - Search only in consolidated folder

#### Split View
Right-click a note tab → "Split right" to view two notes side-by-side (e.g., concept-map + comparison-tables).

#### Outline View
Enable in Settings → Core plugins → Outline. Shows table of contents for current note.

---

### Recommended Plugins (Optional)

These community plugins enhance the study experience:

| Plugin | Purpose |
|--------|---------|
| **Dataview** | Query notes like a database |
| **Spaced Repetition** | Create flashcards from notes |
| **Excalidraw** | Draw diagrams in notes |
| **Better Word Count** | Track study progress |

To install: Settings → Community plugins → Browse

---

## Study Workflow

> These paths are relative to the `concept_map/` vault in Obsidian.

### Quick Review (30 min)
1. Open `consolidated/quick-reference.md`
2. Review key formulas and service cheat sheet

### Deep Dive (1-2 hours)
1. Pick a section folder (e.g., `sections/05-sagemaker-algorithms/`)
2. Read `concept-map.md` for understanding
3. Use `comparison-tables.md` for memorization
4. Open local graph to see connections

### Pre-Exam Review
1. Open Graph View (`Ctrl+G`)
2. Explore clusters around major services (SageMaker, S3, Bedrock)
3. Review `consolidated/all-service-comparisons.md`
4. Final pass through `consolidated/quick-reference.md`

---

## File Format Notes

- **Links**: `[[Service-Name]]` format for Obsidian compatibility
- **Tables**: GitHub-flavored markdown
- **Diagrams**: ASCII art (renders in any viewer)

---

## Exam Quick Facts

| Aspect | Detail |
|--------|--------|
| Exam Code | MLA-C01 |
| Questions | 65 |
| Duration | 170 minutes |
| Passing Score | 720/1000 |
| Cost | $300 USD |

---

## Resources

- [AWS Exam Guide (PDF)](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf)
- [AWS Skill Builder](https://skillbuilder.aws/exam-prep/machine-learning-engineer-associate)
- [SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/)
- [Obsidian Help](https://help.obsidian.md/)

---

Good luck on your exam!
