
basic PBF structure to work from, before we integrate it into our rules and throw out anything that would conflict, let's assess how it stacks up? questions and comments at the end

*plan*

-user: [directs] planning with initial prompt with requirements + ?

-ai high-powered model (architect role, @s/@o/@g/@dr): [clarifies] intent and presents choices if best options aren't clear

-user: [directs] based on ai questions and proposals

-architect:  [plans] complete project plan with detailed instructions for aless-powerful AI builder agent to implement

-user: [reviews] and [directs] updates or [approves]

(if necessary) -architect: modifies [plans ] or [clarifies] if necessary

(if necessary) -user: [reviews] and [directs] until loop is complete and user [approves]

*build* 

-ai high-powered model (coder role, @s/@o): [creates] detailed implementation steps for first phase of plan, including code snippets and shell commands etc for builder to tackle. only builder has write/edit access.

-ai base model (builder role, @b or builer+ role, @d): [saves] planning data (todos and emoji status) to working folder .md file to update status throughout build

-builder/builder+ (user may occassionally use builder+ for high-priorty edits justifying FAC spend): [edits] by beginning implementation of detailed plan in order prescribed by architect.

-at each completed step, builder [tests] its implementation (automatically if possible, with user if necessary), checks `@current_problems`, server or console errors as applicable, and suggest fixes proactively.

-if it works as intended, builder [saves] progress to .md for todos and moves on to implementing the next step (recurse until more coder output is required)

*fix*

-if errors are detected by builder or user, builder evaluates what about their most recent changes caused the error(s), suggests and attempts fix(es).

-builder [tests] its fix(es) (automatically if possible, with user if necessary), checks `@current_problems`, server or console errors as applicable, and suggests how it would attempt to fix again or advise coder for escalation.

-if it works as intended, builder [saves] progress to .md for todos and moves on to implementing the next step (recurse until more coder output is required)

-if it fails again, user [directs] builder to try again, or switches to higher model to try again, either in write mode or to suggest specific code changes for builder to implement

-repeat until errors for given step are resolved

-when it works as intended, builder [saves] progress to .md for todos and moves on to implementing the next step (recurse until more coder output is required--it takes too much context to do all work in coder role at once; coder works in logical prject chunks)

-repeat all phases until all phases of project plan are complete

my ordering and labeling got a little disorganized starting midway through, need you to ensure the entire flow has a consistent and clear structure, using the bracketed commands and roles and other aspects to organize a framwork that recurses its way from project start to project success, with no workflow holes in the process.

ideally, in addition to a framework that makes sense in written english, the entire process could also be represented visually somehow, either as a decision tree or flow diagram, or anything that makes all the recursive aspects clear so that a reader could follow a project all the way to completion on it. 

i may give this task to all high-cost models in this chat, sequentially. then we could analyze and synthesize each model's output into a single best document. is that a good idea? or should we save that step for a prompt that integrates this framework with the rest of the global rules stuff we've been doing? i think this replaces the "double helix" considerations, but i'm wondering if the logical framework in @devin.cursorrules is compatible/better or if this new custom framework is more practically useful for us?
