# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this folder is

This is not a code project. It holds a proposal to the UC Davis Genome Center for a **Focus Group** (new or renewed). The proposal is written here and submitted as a PDF. The call for proposals, which is the source of truth for every requirement, is `Call for Focus Group Proposals 2026.pdf`. Read it before drafting or changing the proposal, and read any other instruction files added to this folder.

## This proposal

- **Name (chosen by the user):** AIDA: AI for Data Analysis and Automation. The name doesn't mention genomics, so the subtitle or the first sentence has to tie the group to the Genome Center's genomics mission.
- **Topic:** a technical, hands-on group sharing practical tips for using AI coding agents to speed up scientific research at the UC Davis Genome Center. It covers omics data analysis and lab automation.
- **Central idea (the user's):** the group is about the practical side of using AI agents to speed up research at the Genome Center. Every show-and-tell gets written up in a shared GitHub repository, in a form people can point their own AI agents at. Labs can then reuse each other's workflows and share ideas, rather than each lab starting from scratch. Build the Objectives, Activities and Impact sections around this repository.
- **Keep it informal (the user's choice).** Any topic is welcome, including simply which tools, editors or models someone uses. Every session is recorded and transcribed, and an AI agent turns the transcript into a write-up for the repository, so presenters have no extra work. Presenters can optionally add more: an installable agent skill, a note of how much time the workflow saved, and how they checked the results. Describe these extras as encouraged, never required. Presenters review the write-up before it is posted, and nothing confidential or unpublished goes in.
- **Status (2026-11-20): final.** `proposal.md` is the submitted text and `AIDA_proposal.pdf` is the PDF built from it (2 pages, letter, 11 pt). After any edit, rebuild with `python3 -I scripts/make_pdf.py proposal.md AIDA_proposal.pdf` (needs Google Chrome plus the Python `markdown` and `pypdf` packages) and confirm it still says 2 pages; the second page is nearly full, so any addition needs a matching cut. The Anaconda `pandoc` on this Mac is an Intel-only build and does not run. The old Claude Doc (https://claude.ai/artifact/JJnkJNjrbip4ZVLcDwA89N) is out of date; don't edit it.
- **The repository is public.** Never commit the call PDF (it's in `.gitignore`), unpublished data, or a participant's name unless that person has agreed to be listed.
- **Email subject line:** `Genome Center Focus Group Proposal – AIDA`
- **Type:** a new group. Leave out section 6 (Past Activities).
- **Leader:** Brett Phinney (Academic Federation), which meets the leader requirement.
- **Participants listed** (each added themselves by pull request, which counts as consent): Uri Keshet (Metabolomics Core), Adam Schaal (Genome Center), Gert Wohlgemuth (West Coast Metabolomics Center), Ziyue Yang (Fiehn Lab). Keep them in alphabetical order by surname.
- **Objective 3 (shared tools, data and computing)** is a condensed version of Gert Wohlgemuth's pull request #1. His full catalog of shared tools lives in `catalog/`; follow `catalog/README.md` when adding entries.
- **Budget (final, $8,500 of the $10k cap):** monthly show-and-tells $2,000; two half-day workshops $1,500; GPUs for local models $5,000, described as "hosted at the Genome Center" (the user chose not to name a machine). The user decided against the $1,500 sprint day.

## Proposal requirements (from the 2026 call)

- **Length:** 1 to 2 pages. This is a hard limit, so check the page count of the final PDF.
- **Funding:** up to $10k per year. It can pay for research activities, equipment, or sharing findings with other experts in the field. The budget must fit under this cap.
- **Required sections, in this order:**
  1. Focus Group Name
  2. Leader(s) and Interested Participants. The primary leader must be a Genome Center member (Faculty or Academic Federation). List all interested participants.
  3. Objectives and Scope, including how they fit the Genome Center's mission
  4. Participant Involvement: who takes part, their roles, and what each contributes
  5. Proposed Activities (research projects, seminars, workshops, other initiatives), each with its cost, which makes up the short budget
  6. Past Activities: only for renewals, a summary of past activities and accomplishments
  7. Potential Impact on genomics research, education, and outreach
- **Submission:** email the PDF to the address in the call, with the subject line `Genome Center Focus Group Proposal – <Focus Group Name>`.
- **Dates in the 2026 call:** due August 1, 2026; decisions by September 1, 2026. Both dates are before this file was created (2026-11-17). Before relying on them, confirm with the user whether a newer call or an extension applies.
- **Review:** the Genome Center Executive Committee evaluates proposals. Questions go to the contacts named in the call.

## Working notes

- Don't make up participants, their roles, past activities, or budget figures. Use only what the user or the files in this folder supply, and mark anything missing as a placeholder for the user to fill in.
- Put an item-by-item cost in the Proposed Activities section and keep the total at or under $10k.
