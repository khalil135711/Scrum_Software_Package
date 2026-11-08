# Sprint Board
<img width="1646" height="805" alt="Bildschirmfoto 2026-11-08 um 18 02 30" src="https://github.com/user-attachments/assets/855509fd-fe6d-4eb1-8524-4f46601c3dd9" />

A small, self-contained Scrum board that runs in your browser. No accounts, no database, no build step.

## Features
- **Backlog:** add stories with story points (1, 2, 3, 5, 8, 13), delete, and pull into a sprint
- **Sprint planning:** start a sprint with a name, goal and length in days
- **Board:** To do / In progress / Done columns with drag-and-drop (or the arrow buttons for keyboard use)
- **Progress ribbon:** done, in-progress and to-do points at a glance
- **Reports:** live burndown against ideal pace, and velocity across completed sprints
- **Export / import** your data as JSON; light and dark themes follow your system

## Requirements
A modern browser (Chrome, Edge, Firefox, Safari). Python 3 is optional and only needed for Option B.

## Run it locally

### Option A: open the file
Double-click `index.html`. That's it.

### Option B: tiny local server (recommended)
```bash
git clone https://github.com/khalil135711/Scrum_Software_Package && cd Scrum_Software_Package
python serve.py          # opens http://localhost:8000
python serve.py 3000     # use a different port
```
On some systems the command is `python3 serve.py`.

### Option C: Node.js
```bash
cd sprint-board
npx serve .
```

## How to use it
1. **Backlog tab:** add a few stories and give each a point estimate.
2. **Board tab:** fill in the sprint form and select *Start sprint*.
3. **Backlog tab:** select *Add to sprint* on the stories you commit to.
4. **Board tab:** move cards across the columns as work progresses.
5. **Reports tab:** watch the burndown. When the sprint ends, select *Complete sprint* on the Board tab; unfinished stories return to the backlog and velocity is recorded.

## Where your data lives
Data is saved in your browser's localStorage, so it stays on your machine and is private to that browser and address. Opening via `file://` and via `localhost` count as different locations and do not share data. Use **Export data** to back up or move to another browser or computer, and **Import data** to restore.

## Limits
This is a single-user tool for learning, demos and small teams. It has no logins, real-time sync or integrations. For multi-user company use, see the tool comparison in the earlier package (Jira, Azure DevOps, Linear and others).

## Files
- `index.html`: the whole app (HTML, CSS and JavaScript)
- `serve.py`: optional local server
- `README.md`: this file

## Customizing
Colors and spacing are CSS variables at the top of `index.html`. Story point options are the `PTS` array in the script.
