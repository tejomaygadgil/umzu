# Wozu 🤔

Manage a project, develop a recipe, organize your inner thoughts, or plan a party with Wozu.

<img src="wozu.png" width="700">

## Basic concept

All human activity is composed of tasks that depend on one another.

Therefore, in Wozu you can do three things:

- Link tasks together
- Focus on tasks (Kanban)
- Embed URLs in tasks

This simple feature set encourages fast iteration and the exploration of ideas, not tooling.

## How to use

1. Fill out:
   
|File|Example|
|---|---|
|`graph.txt`|`a --> b`|
|`todo.txt`|`Want to do:` (green)<br>`c`<br>`Will do:` (blue)<br>`b`<br>`Doing:` (red)<br>`a`|
|`links.txt`|`a: somesite.com.com/someplace`|

2. Run `python server.py` to start UI.
3. Iterate to see changes rendered immediately.

## Some tips

- Adjust around until the graph look pretty. This will force you to draw useful connections.
- Use separate files to track different things, or put everything in one big graph.
- You can use version control (Git) to back up your changes!
- You can embed graphs within each other. [TODO]

## On the name

Wozu is German for "for what", or "in order to." 

All tasks are "for" something else so the name seemed fitting.

Plus I like the sound (woe-tsu).
