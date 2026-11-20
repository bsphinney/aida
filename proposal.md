# AIDA: AI for Data Analysis and Automation

Genome Center Focus Group Proposal (new group) · Leader: Brett Phinney · November 2026

## 1. Focus Group Name

**AIDA: AI for Data Analysis and Automation in Genomics Research**

AIDA is a hands-on group where Genome Center researchers share practical ways to use AI coding agents, and the tools they build with them, to speed up omics data analysis and lab automation. Every session feeds a shared library that any lab's AI agent can read and reuse.

## 2. Leader and Interested Participants

**Leader:** Brett Phinney, Proteomics Core, UC Davis Genome Center (Academic Federation member).

**Participants:** membership is open to anyone at the Genome Center who wants practical tips on using AI in their research, including faculty, staff scientists, core staff, postdocs and graduate students. People who have already agreed to take part:

- Uri Keshet, Metabolomics Core
- Adam Schaal, Genome Center
- Gert Wohlgemuth, West Coast Metabolomics Center
- Ziyue Yang, Fiehn Lab

## 3. Objectives and Scope

AI coding agents can now write analysis code, build pipelines, run jobs on a cluster and drive instruments. Most labs are learning to use them alone, and what one lab learns rarely reaches the next. AIDA shares that know-how across labs in a form that can be reused.

Objectives:

1. **Share practical experience.** Researchers show what works and what doesn't: tools, editors and models, prompts, analysis pipelines, lab automation, and jobs on the HPC@UCD clusters.
2. **Build a shared, agent-readable library.** Every session is written up in a public GitHub repository ([github.com/bsphinney/aida](https://github.com/bsphinney/aida)), organized so a researcher can point their own AI agent at it and reuse a workflow developed in another lab.
3. **Share tools, data and computing.** Labs and cores list the AI tools they build in a shared catalog, including agent skills and MCP servers that let any lab's agent use another lab's databases, instruments or pipelines, with access controlled by the owner. Labs that run local models can connect their GPU servers through an open interface ([InferWeave](https://github.com/InferWeave/inferweave-specs)) to share spare capacity.
4. **Use AI responsibly.** The group promotes checking AI-generated results, protecting unpublished and sensitive data, and making workflows repeatable with written steps, pinned model versions and automatic checks.

**Scope:** practical use of AI agents across genomics, transcriptomics, proteomics, metabolomics and lab operations, focused on what members can apply the next day rather than AI theory. This supports the Genome Center's mission of advancing genomics research through collaboration and shared resources.

## 4. Participant Involvement

The group is deliberately informal, so anyone can contribute without much preparation.

- **Presenters** give a short show-and-tell on anything useful, from which editor or model they use to a full analysis pipeline built with an agent. All experience levels are welcome.
- **Every session is recorded and transcribed.** An AI agent turns each transcript into a repository entry, so presenters write nothing up. Presenters approve the entry before it is posted, and no confidential or unpublished data is included.
- **Optional extras.** Presenters are encouraged, but never required, to add a reusable agent skill, an estimate of the time the workflow saved, and a note on how they checked the results.
- **Cores and trainees.** Cores can publish MCP servers for their services and data, starting from a shared template that is read-only by default. Graduate students and postdocs gain a career skill and a low-stakes place to present.
- **The leader** organizes the sessions and workshops, looks after the repository and runs the shared GPU hardware.

## 5. Proposed Activities and Budget

AIDA requests $8,500 for its first year, for three activities:

- **Monthly AI show-and-tells.** About 10 lunchtime sessions of one or two short demos each, followed by discussion. Each one becomes a write-up in the shared repository.
- **Two half-day hands-on workshops.** The first covers setting up an AI coding agent for data analysis and building an MCP server for a lab's own data. The second covers using agents for lab automation and running jobs on the HPC@UCD clusters.
- **GPUs for running AI models locally, hosted at the Genome Center.** These let labs use AI on data that cannot go to commercial AI services, such as unpublished results, human samples and controlled-access data. Labs can share them through the connected model servers (objective 3), and members will compare local and cloud models on the library's workflows.

| Activity | Cost |
| --- | --- |
| Monthly show-and-tells (lunch, about 10 sessions) | $2,000 |
| Two half-day hands-on workshops | $1,500 |
| GPUs for local AI models | $5,000 |
| **Total** | **$8,500** |

The group also runs two activities at no cost: the GitHub repository itself, and a Slack or Teams channel for quick questions between sessions.

## 6. Potential Impact

- **Research:** labs reuse each other's workflows and tools instead of starting from scratch, and their agents can use other labs' data services and spare GPU capacity, shortening the time from data to result. Presenters' notes on time saved build a measured record of the group's effect.
- **Education:** sessions and workshops teach researchers at every level an increasingly essential skill, with good habits for checking results and reproducibility. Graduate students and postdocs get hands-on training and a place to present.
- **Outreach:** the library outlasts any single meeting and helps labs that never attend. Because it is public, other genomics groups can use it too, raising the Genome Center's profile in practical, responsible AI for research. This proposal was itself written in that repository by five contributors and their AI agents.
