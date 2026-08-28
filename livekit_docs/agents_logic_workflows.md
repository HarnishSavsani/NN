# Agents: Logic & Workflows

Agent sessions, workflows, tasks, tool definitions, turn detection, supervisor patterns, and agent server configuration.

- **Total pages in this section**: 40
- **Successful retrieves**: 40
- **API References / Placeholders**: 0

## Table of Contents

1. [agents/logic/](#page-1) (✓)
2. [agents/server/](#page-2) (✓)
3. [agents/logic/sessions/](#page-3) (✓)
4. [agents/logic/chat-context/](#page-4) (✓)
5. [agents/logic/tasks/](#page-5) (✓)
6. [agents/logic/workflows/](#page-6) (✓)
7. [agents/logic/supervisor-pattern/](#page-7) (✓)
8. [agents/logic/tools/](#page-8) (✓)
9. [agents/logic/nodes/](#page-9) (✓)
10. [agents/logic/turns/](#page-10) (✓)
11. [agents/logic/agents-handoffs/](#page-11) (✓)
12. [agents/logic/external-data/](#page-12) (✓)
13. [agents/logic/fallback-strategies/](#page-13) (✓)
14. [agents/prebuilt/tasks/](#page-14) (✓)
15. [agents/prebuilt/tools/](#page-15) (✓)
16. [agents/server/startup-modes](#page-16) (✓)
17. [agents/server/lifecycle/](#page-17) (✓)
18. [agents/server/agent-dispatch/](#page-18) (✓)
19. [agents/server/job/](#page-19) (✓)
20. [agents/server/options/](#page-20) (✓)
21. [agents/logic/tools/definition/#interruptions](#page-21) (✓)
22. [agents/logic/tools/toolsets/](#page-22) (✓)
23. [agents/logic/tools/async/](#page-23) (✓)
24. [agents/logic/tools/mcp/](#page-24) (✓)
25. [agents/logic/tools/forwarding/](#page-25) (✓)
26. [agents/logic/tools/design/](#page-26) (✓)
27. [agents/logic/turns/turn-detector/](#page-27) (✓)
28. [agents/logic/turns/adaptive-interruption-handling/](#page-28) (✓)
29. [agents/logic/turns/vad/](#page-29) (✓)
30. [agents/logic/turns/tuning/](#page-30) (✓)
31. [agents/prebuilt/tasks/get-name/](#page-31) (✓)
32. [agents/prebuilt/tasks/get-email/](#page-32) (✓)
33. [agents/prebuilt/tasks/get-address/](#page-33) (✓)
34. [agents/prebuilt/tasks/get-dob/](#page-34) (✓)
35. [agents/prebuilt/tasks/get-phone-number/](#page-35) (✓)
36. [agents/prebuilt/tasks/get-credit-card/](#page-36) (✓)
37. [agents/prebuilt/tasks/get-dtmf/](#page-37) (✓)
38. [agents/prebuilt/tasks/warm-transfer/](#page-38) (✓)
39. [agents/prebuilt/tools/end-call-tool/](#page-39) (✓)
40. [agents/prebuilt/tools/send-dtmf-events/](#page-40) (✓)

---

<a name="page-1"></a>
## Page 1: agents/logic/
**Original URL:** https://docs.livekit.io/agents/logic/  
**Source MD URL:** https://docs.livekit.io/agents/logic.md

LiveKit docs › Build Agents › Logic & Structure › Overview

---

# Logic and structure overview

> Learn how to structure agent logic with sessions, workflows, tasks, tools, and other components for building voice AI applications.

## Overview

LiveKit Agents provides modular components for structuring agent logic into focused, maintainable units that perform accurately and consistently in complex real-world scenarios. Use sessions, workflows, tasks, and tools to break down agent behavior, enabling reliable production applications that handle nuanced conversations, multi-step processes, and external integrations with precision.

## Logic and structure components

Use core components to structure your agent logic, including sessions, workflows, customization points, and external integrations. Build simple single-agent applications, or combine these components for complex, multi-agent workflows.

| Component | Description | Use cases |
| **Agent sessions** | Orchestrate input collection, pipeline management, and output delivery. The main orchestrator for your voice AI app. | Single-agent apps, session lifecycle management, and room I/O configuration. |
| **Chat context** | Manage the conversation history sent to the LLM on each turn. Create, copy, truncate, and merge contexts to control what the model knows. | Initializing context with user data, preserving history across handoffs, and injecting per-turn context. |
| **Tasks & task groups** | Create focused, reusable units that perform specific objectives and return typed results. Tasks run inside agents and take temporary control until completion. | Consent collection, structured data capture, and multi-step processes with task groups. |
| **Workflows** | Model repeatable patterns with agents, handoffs, and tasks for complex voice AI systems. | Multi-persona systems, conversation phase management, and specialized agent routing. |
| **Tool definition & use** | Extend agent capabilities with custom functions callable by the LLM for external actions and data access. | API integrations, frontend RPC calls, and triggering agent handoffs. |
| **Pipeline nodes & hooks** | Customize agent behavior at pipeline processing points with custom STT, LLM, TTS, and lifecycle hooks. Override nodes to modify input, output, or add custom logic. | Custom providers, output modification, and pronunciation control. |
| **Turn detection & interruptions** | Manage conversation flow with turn detection, interruption handling, and manual turn control. | Natural conversation timing, interruption management, and push-to-talk interfaces. |
| **Agents & handoffs** | Define distinct reasoning behaviors and transfer control between agents when different capabilities are needed. | Role-based agents, model specialization, and permission management. |
| **External data & RAG** | Connect agents to external data sources, databases, and APIs for RAG and data operations. Load initial context, perform RAG lookups, and integrate with external services. | Knowledge base search, user profile loading, and database operations. |

## In this section

Read more about each component.

- **[Agent sessions](https://docs.livekit.io/agents/logic/sessions.md)**: Main orchestrator for input collection, pipeline management, and output delivery.

- **[Chat context](https://docs.livekit.io/agents/logic/chat-context.md)**: Manage conversation history sent to the LLM on each turn.

- **[Tasks & task groups](https://docs.livekit.io/agents/logic/tasks.md)**: Focused units that perform specific objectives and return typed results.

- **[Workflows](https://docs.livekit.io/agents/logic/workflows.md)**: Model repeatable patterns with agents, handoffs, and tasks.

- **[Tool definition & use](https://docs.livekit.io/agents/logic/tools.md)**: Custom functions callable by the LLM for external actions.

- **[Pipeline nodes & hooks](https://docs.livekit.io/agents/logic/nodes.md)**: Customize behavior at pipeline processing points.

- **[Turn detection & interruptions](https://docs.livekit.io/agents/logic/turns.md)**: Manage conversation flow with turn detection and interruption handling.

- **[Agents & handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md)**: Define distinct agents and transfer control between them.

- **[External data & RAG](https://docs.livekit.io/agents/logic/external-data.md)**: Connect to external data sources, databases, and APIs.

---

This document was rendered at 2026-08-28T04:22:10.499Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic.md](https://docs.livekit.io/agents/logic.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-2"></a>
## Page 2: agents/server/
**Original URL:** https://docs.livekit.io/agents/server/  
**Source MD URL:** https://docs.livekit.io/agents/server.md

LiveKit docs › Build Agents › Agent Server › Overview

---

# Agent server overview

> An overview of agent server components for LiveKit Agents.

## Overview

LiveKit Agents supports an agent server architecture for managing multiple concurrent agent sessions and programmatic participants. Use dispatch, job execution, and configuration options to scale your agents horizontally and manage their lifecycles.

### Programmatic participants

The Agents framework isn't limited to AI agents. You can use it to deploy any code that needs to process realtime media and data streams as a programmatic participant. A programmatic participant is any code that joins a LiveKit room as a participant — this includes AI agents, media processors, or custom logic that processes realtime streams.

Some examples of what these participants can do include:

- **Process audio streams**: Analyze audio for patterns, quality metrics, or content detection.
- **Handle video processing**: Apply computer vision, video effects, or content moderation.
- **Manage data flows**: Aggregate, transform, or route realtime data between participants.
- **Provide services**: Act as bridges to external APIs, databases, or other systems.

The framework provides the same production-ready infrastructure for all types of programmatic participants, including automatic scaling and load balancing. You can use the [entrypoint function](https://docs.livekit.io/agents/server/job.md#entrypoint) without creating an `AgentSession` to build programmatic participants that are automatically dispatched to rooms.

- **[Processing raw media tracks](https://docs.livekit.io/transport/media/raw-tracks.md)**: Learn how to process raw audio and video tracks in your programmatic participants.

## Agent server components

Use core components to manage agent servers, including agent dispatch, job execution, and configuration.

| Component | Description | Use cases |
| **Agent dispatch** | Assign agents to rooms automatically or explicitly, with load balancing and high concurrency support. | Automatic agent assignment, explicit dispatch control, and custom dispatch logic. |
| **Job lifecycle** | Manage the entrypoint function, job execution, and session cleanup for each agent instance. | Entrypoint configuration, session management, and graceful shutdown. |
| **Server options** | Configure permissions, dispatch rules, prewarm functions, and server behavior. | Permission management, load balancing configuration, and server initialization. |

## In this section

Read more about each component.

- **[Server lifecycle](https://docs.livekit.io/agents/server/lifecycle.md)**: How agent servers register, receive requests, and manage jobs.

- **[Agent dispatch](https://docs.livekit.io/agents/server/agent-dispatch.md)**: Specify how and when agents are assigned to rooms.

- **[Job lifecycle](https://docs.livekit.io/agents/server/job.md)**: Learn about the entrypoint function and session management.

- **[Server options](https://docs.livekit.io/agents/server/options.md)**: Configure permissions, dispatch rules, and server behavior.

---

This document was rendered at 2026-08-28T04:22:10.499Z.
For the latest version of this document, see [https://docs.livekit.io/agents/server.md](https://docs.livekit.io/agents/server.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-3"></a>
## Page 3: agents/logic/sessions/
**Original URL:** https://docs.livekit.io/agents/logic/sessions/  
**Source MD URL:** https://docs.livekit.io/agents/logic/sessions.md

LiveKit docs › Build Agents › Logic & Structure › Agent sessions

---

# Agent session

> How to use AgentSession to orchestrate your voice AI app.

## Overview

The `AgentSession` is the main orchestrator for your voice AI app. The session is responsible for collecting user input, managing the voice pipeline, invoking the LLM, sending the output back to the user, and emits events for observability and control.

Each session requires at least one `Agent` to orchestrate. The agent is responsible for defining the core AI logic - instructions, tools, etc - of your app. The framework supports the design of custom [workflows](https://docs.livekit.io/agents/logic/workflows.md) to orchestrate handoff and delegation between multiple agents.

The following example shows how to begin a simple single-agent session:

**Python**:

```python
from livekit.agents import AgentSession, Agent, inference, room_io, TurnHandlingOptions
from livekit.plugins import noise_cancellation

session = AgentSession(
    stt="deepgram/nova-3:en",
    llm="google/gemma-4-31b-it",
    tts="inworld/inworld-tts-2:Ashley",
    turn_handling=TurnHandlingOptions(
        turn_detection=inference.TurnDetector(),
    ),
)

await session.start(
    room=ctx.room,
    agent=Agent(instructions="You are a helpful voice AI assistant."),
    room_options=room_io.RoomOptions(
        audio_input=room_io.AudioInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    ),
)

```

---

**Node.js**:

```ts
import { voice, inference } from '@livekit/agents';
import { BackgroundVoiceCancellation } from '@livekit/noise-cancellation-node';

const session = new voice.AgentSession({
  stt: "deepgram/nova-3:en",
  llm: "google/gemma-4-31b-it",
  tts: "inworld/inworld-tts-2:Ashley",
  turnHandling: {
    turnDetection: new inference.TurnDetector(),
  },
});

await session.start({
  room: ctx.room,
  agent: voice.Agent.create({
    instructions: "You are a helpful voice AI assistant.",
  }),
  inputOptions: {
    noiseCancellation: BackgroundVoiceCancellation(),
  },
});

```

> ℹ️ **Simplified imports**
> 
> In Node.js, the `voice` and `llm` exports are also available directly from `@livekit/agents`, so you can write `import { Agent, AgentSession, tool } from '@livekit/agents'` instead of qualifying them with `voice.` or `llm.`. The namespaced form shown throughout these docs is still supported.

## Lifecycle

An `AgentSession` progresses through several distinct phases during its operation:

- **Initializing**: The session is setting up. During initialization, no audio or video processing occurs yet. Agent state is set to `initializing`.
- **Starting**: The session is started using the `start()` method. It sets up I/O connections, initializes agent activity tracking, and begins forwarding audio and video frames. In this phase, the agent is transitioned into the `listening` state.
- **Running**: The session is actively processing user input and generating agent responses. During this phase, your agent controls the session and can transfer control to other agents. In this phase, the agent transitions between `listening`, `thinking`, and `speaking` states.
- **Closing**: When a session is closed, the cleanup process includes gracefully draining pending speech (if requested), waiting for any queued operations to complete, committing any remaining user transcripts, and closing all I/O connections. The session emits a `close` event and resets internal state.

The following diagram shows the lifecycle of an `AgentSession` using agent states:

```mermaid
stateDiagram-v2
initializing --> listening : session started
listening --> thinking : user input received
thinking --> speaking : response generated
speaking --> listening : response complete
speaking --> listening : interrupted
listening --> initializing : session shutdown requested and states resetnote right of initializing
Session setup in progress
(no media I/O yet)
end notenote right of speaking
Agent outputs synthesized
audio response
end note
```

You can monitor agent state changes via the [`agent_state_changed` event](https://docs.livekit.io/reference/agents/events.md#agent_state_changed).

## Events

`AgentSession` emits events throughout its lifecycle to provide visibility into the conversation flow. For more information, select the event name to see the properties and example code.

| **Event** | **Description** |
| [`agent_state_changed`](https://docs.livekit.io/reference/agents/events.md#agent_state_changed) | Emitted when the agent's state changes (for example, from `listening` to `thinking` or `speaking`). |
| [`user_state_changed`](https://docs.livekit.io/reference/agents/events.md#user_state_changed) | Emitted when the user's state changes (for example, from `listening` to `speaking`). |
| [`user_input_transcribed`](https://docs.livekit.io/reference/agents/events.md#user_input_transcribed) | Emitted when user speech is transcribed to text. |
| [`conversation_item_added`](https://docs.livekit.io/reference/agents/events.md#conversation_item_added) | Emitted when a message is added to the conversation history. |
| [`close`](https://docs.livekit.io/reference/agents/events.md#close) | Emitted when the session closes, either gracefully or due to an error. |

## Session options

The `AgentSession` constructor accepts numerous options to configure behavior. The following sections describe the available options grouped by category.

### AI models

Configure the default speech and language models for your agent session. You can override these models for specific agents or tasks. To learn more about models, see the [models](https://docs.livekit.io/agents/models.md) topic.

### Turn detection & interruptions

Turn detection and interruptions are critical for managing conversation flow. You can configure the turn detection mode, turn handling, and interrupt behavior with the `turn_handling` parameter for `AgentSession`. To learn more, see the [Turns overview](https://docs.livekit.io/agents/logic/turns.md) topic.

- [`preemptive_generation`](https://docs.livekit.io/agents/multimodality/audio.md#preemptive-generation): Speculatively begins LLM requests before end-of-turn is detected to reduce response latency. Increases LLM token usage because speculative responses may be discarded. Configured via `turn_handling`. Default: enabled.

### Tools and capabilities

Extend agent capabilities with [tools](https://docs.livekit.io/agents/logic/tools.md):

- `tools`: List of `FunctionTool` or `RawFunctionTool` objects shared by all agents in the session.
- `mcp_servers`: List of MCP (Model Context Protocol) servers providing external tools.
- `max_tool_steps`: Maximum consecutive tool calls per LLM turn. Default: `3`. When the limit is reached, the agent makes one final LLM call with tool use disabled to generate a spoken response summarizing the results so far.

> ℹ️ **Note**
> 
> With the `livekit-agents` [1.4.5 release](https://github.com/livekit/agents/releases/tag/livekit-agents%401.4.5), reaching the `max_tool_steps` limit generates a final reply instead of failing silently.
- `ivr_detection`: Whether to detect if the agent is interacting with an Interactive Voice Response (IVR) system. Default: `False`. To learn more, see [DTMF](https://docs.livekit.io/telephony/features/dtmf.md).

### User interaction

The following parameters control how the session responds to user presence and speech timing.

- **`user_away_timeout`** _(float)_ (optional) - Default: `15.0`: Time in seconds of silence before the framework sets the user state to `away`. Set to `None` to turn off. See [Handling inactive users](#handling-inactive-users) for a complete example.

- **`min_consecutive_speech_delay`** _(float)_ (optional) - Default: `0.0`: Minimum delay in seconds between consecutive agent utterances.

#### Handling inactive users

Combine `user_away_timeout` with the [`user_state_changed`](https://docs.livekit.io/reference/agents/events.md#user_state_changed) event to detect when a user has gone idle and respond accordingly. When neither the user nor the agent has spoken for the configured duration, the framework sets the user state to `away` and emits a `user_state_changed` event.

A common pattern is to prompt the user a few times to check if they're still present, then shut down the session if they don't respond. The following example demonstrates each step:

- Set `user_away_timeout` to control how long silence lasts before the user is marked as `away`. The default is 15 seconds.
- Listen for `user_state_changed` and check for `new_state == "away"` to trigger your check-in logic.
- Cancel any pending check-in task if the user speaks or otherwise becomes active again, which changes the state back to `speaking` or `listening`.
- Call `session.shutdown()` (Python) or `ctx.shutdown()` (Node.js) to gracefully end the session after exhausting retries. To learn more, see [Ending the session](https://docs.livekit.io/agents/server/job.md#session-shutdown).

**Python**:

```python
import asyncio
from livekit.agents import (
    Agent, AgentSession, JobContext, UserStateChangedEvent, inference,
)

# ctx is the JobContext from the entrypoint function
session = AgentSession(
    stt=inference.STT("deepgram/nova-3"),
    llm=inference.LLM("openai/gpt-4.1-mini"),
    tts=inference.TTS("inworld/inworld-tts-2"),
    user_away_timeout=12.5,  # seconds of silence before "away"
)

inactivity_task: asyncio.Task | None = None

async def check_if_user_present():
    # Prompt the user a few times, then end the session
    for _ in range(3):
        await session.generate_reply(
            instructions="The user has been inactive. Politely check if the user is still present."
        )
        await asyncio.sleep(10)
    session.shutdown()

@session.on("user_state_changed")
def on_user_state_changed(ev: UserStateChangedEvent):
    global inactivity_task
    if ev.new_state == "away":
        inactivity_task = asyncio.create_task(check_if_user_present())
        return

    # User came back (speaking, listening, etc.) — cancel the check-in
    if inactivity_task is not None:
        inactivity_task.cancel()
        inactivity_task = None

await session.start(
    agent=Agent(instructions="You are a helpful assistant."),
    room=ctx.room,
)

```

---

**Node.js**:

```typescript
import { type JobContext, voice, inference, Task, delay } from '@livekit/agents';

// ctx is the JobContext from the entry function
const session = new voice.AgentSession({
  stt: new inference.STT({ model: 'deepgram/nova-3' }),
  llm: new inference.LLM({ model: 'openai/gpt-4.1-mini' }),
  tts: new inference.TTS({ model: 'inworld/inworld-tts-2' }),
  voiceOptions: {
    userAwayTimeout: 12.5, // seconds of silence before "away"
  },
});

let task: Task<void> | null = null;

const checkIfUserPresent = async (controller: AbortController): Promise<void> => {
  // Prompt the user a few times, then end the session
  for (let i = 0; i < 3; i++) {
    if (controller.signal.aborted) return;
    const reply = await session.generateReply({
      instructions: 'The user has been inactive. Politely check if the user is still present.',
    });
    await reply.waitForPlayout();
    try {
      await delay(10000, { signal: controller.signal });
    } catch {
      return;
    }
  }
  if (!controller.signal.aborted) {
    ctx.shutdown();
  }
};

session.on(voice.AgentSessionEventTypes.UserStateChanged, (event) => {
  if (event.newState === 'away') {
    task = Task.from(checkIfUserPresent);
    return;
  }

  // User came back (speaking, listening, etc.) — cancel the check-in
  if (task) {
    task.cancel();
    task = null;
  }
});

await session.start({
  agent: voice.Agent.create({ instructions: 'You are a helpful assistant.' }),
  room: ctx.room,
});

```

### Text processing

Control how [text](https://docs.livekit.io/agents/multimodality/text.md) is processed:

- `tts_text_transforms`: Transforms to apply to TTS input text. Built-in transforms include `"filter_markdown"` and `"filter_emoji"`, and you can add custom callable transforms. Set to `None` to turn off. When not given, all built-in filters are applied by default. To learn more, see [Text transforms](https://docs.livekit.io/agents/multimodality/text.md#text-transforms).
- `use_tts_aligned_transcript`: Whether to use TTS-aligned transcript as input for the transcription node. Only applies if the TTS supports aligned transcripts. Default: turned off.

### Video sampling

Available in:
- [ ] Node.js
- [x] Python

Control video frame processing:

- `video_sampler`: Custom video sampler, or `None` to disable sampling. When not given, uses `VoiceActivityVideoSampler`.
- `VoiceActivityVideoSampler`: The default sampler. Varies the frame rate based on the session's `user_state`, capturing more frequently while the user is speaking and less frequently during silence. Construct it directly to override the defaults:

- `speaking_fps`: Target frames per second while the user is speaking. Default: `1.0`.
- `silent_fps`: Target frames per second while the user is silent. Set to `0` to drop all frames during silence. Default: `0.3`.

### Other options

`userdata`: Arbitrary per-session user data accessible via `session.userdata`. To learn more, see [Passing state](https://docs.livekit.io/agents/logic/agents-handoffs.md#passing-state).

## rtc_session options

The following optional parameters are available when you define your entrypoint function using the `rtc_session` decorator:

- `agent_name`: Name of agent for agent dispatch. If this is set, the agent must be explicitly dispatched to a room. To learn more, see [Agent dispatch](https://docs.livekit.io/agents/server/agent-dispatch.md).
- `type`: Agent server type determines when a new instance of the agent is created: for each room or for each publisher in a room. To learn more, see [Agent server type](https://docs.livekit.io/agents/server/options.md#servertype).
- `on_session_end`: Callback function to be called when the session ends. To learn more, see [Session reports](https://docs.livekit.io/deploy/observability/data.md#session-reports).
- `on_request`: Callback function to be called when a new request is received. To learn more, see [Request handler](https://docs.livekit.io/agents/server/options.md#request-handler).

## RoomIO

Communication between agent and user participants happens using media streams, also known as tracks. For voice AI apps, this is primarily audio, but can include vision. By default, track management is handled by `RoomIO`, a utility class that serves as a bridge between the agent session and the LiveKit room. When an AgentSession is initiated, it automatically creates a `RoomIO` object that enables all room participants to subscribe to available audio tracks.

When starting an `AgentSession`, you can configure how the session interacts with the LiveKit room by passing `room_options` to the `start()` method. These options control media track management, participant linking, and I/O behavior.

### Linked participant

In a session, an agent interacts with a specific _linked participant_. By default, the linked participant is the first participant to join a room. You can manually set or change the linked participant using the following methods:

- Pass the participant identity to the `RoomIO` constructor when creating the session. This requires a custom `RoomIO` object to be created. To learn more, see [Custom RoomIO](#custom-roomio).
- Set `participant_identity` in `RoomOptions` (or `RoomInputOptions` in Node.js). To learn more, see [Participant management](#participant-management).
- Call `RoomIO.set_participant()` within a session to change the linked participant dynamically.

#### Identifying the linked participant

Available in:
- [ ] Node.js
- [x] Python

In the default case, the linked participant is the first participant to join a room. You can identify the linked participant using the `session.room_io.linked_participant` property after starting the session:

**Python**:

```python

await session.start(
    # ... agent, room, room_options, etc.
)

participant = session.room_io.linked_participant

```

### Room options

Configure how the agent interacts with room participants using `RoomOptions`. The following sections describe available options for input and output configuration.

> ℹ️ **Python and Node.js differences**
> 
> In Python, as of the 1.3.1 release, a unified `RoomOptions` class is used to configure both input and output options for the session. In Node.js, `RoomInputOptions` and `RoomOutputOptions` are still supported.

#### In this section

The following sections describe the available room options:

| Component | Description | Use cases |
| [Input options](#input-options) | Configure input options for text, audio, and video. | Enable noise cancellation, pre-connect audio, or configure additional audio input options. Enable video input, add a callback function for text input, or disable text input entirely. |
| [Output options](#output-options) | Configure output options for text and audio. | Set transcription options, disable audio output, or set audio output sample rate, number of channels, and track options. |
| [Participant management](#participant-management) | Configure participant management options. | Configure the types of participants an agent can interact with and set the linked participant for the session. |
| [Clean up options](#clean-up-options) | Configure options for cleaning up session and room. | Close the session when linked participant leaves or automatically delete the room on session end. |

#### Input options

The following sections describe the available input options for [text](#text-input), [audio](#audio-input), and [video](#video-input).

##### Text input options

To enable or turn off text input, set the following parameter to `True` or `False`.

**Python**:

`RoomOptions.text_input`

---

**Node.js**:

`RoomInputOptions.textEnabled`

###### Text input callback

By default, text input interrupts the agent and generates a reply. You can customize this behavior by adding a callback function to handle text input. To learn more, see [Custom handling](https://docs.livekit.io/agents/multimodality/text.md#custom-handling) of text input.

##### Audio input options

To enable or turn off audio input, set the following parameter to `True` or `False`.

**Python**:

`RoomOptions.audio_input`

---

**Node.js**:

`RoomInputOptions.audioEnabled`

Additional options for audio input are available using the `AudioInputOptions` object (Python) or `RoomInputOptions.audioOptions` (Node.js):

- [Noise cancellation](https://docs.livekit.io/transport/media/noise-cancellation.md#agents) options: Reduce background noise in incoming audio.
- [Automatic gain control](https://docs.livekit.io/agents/multimodality/audio.md#agc) options (Python only): Normalize input audio levels. Enabled by default.
- [Pre-connect audio](https://docs.livekit.io/agents/multimodality/audio.md#instant-connect) options (Python Agent SDK only): Buffer audio prior to connection to reduce perceived latency.

For a full list of audio input options, see the reference documentation:

**Python**:

[AudioInputOptions](https://docs.livekit.io/reference/python/livekit/agents/voice/room_io/index.html.md#livekit.agents.voice.room_io.AudioInputOptions)

---

**Node.js**:

[RoomInputOptions.audioOptions](https://docs.livekit.io/reference/agents-js/interfaces/agents.voice.RoomInputOptions.html.md#audiooptions)

##### Video input options

To enable or turn off video input, set the following parameter to `True` or `False`. By default, video input is disabled.

**Python**:

`RoomOptions.video_input`

---

**Node.js**:

`RoomInputOptions.videoEnabled`

#### Output options

The following sections describe the available output options for text and audio.

##### Text output options

To enable or turn off text output, set the following parameter to `True` or `False`. By default, text output is enabled.

**Python**:

`RoomOptions.text_output`

---

**Node.js**:

`RoomOutputOptions.transcriptionEnabled`

###### Transcription options

By default, audio and text output are both enabled and a transcription is emitted in sync with the audio. You can turn off transcriptions or customize this behavior. To learn more, see [Transcriptions](https://docs.livekit.io/agents/multimodality/text.md#transcriptions).

##### Audio output options

To enable or turn off audio output, set the following parameter to `True` or `False`. By default, audio output is enabled.

**Python**:

`RoomOptions.audio_output`

---

**Node.js**:

`RoomOutputOptions.audioEnabled`

For additional audio output options, see the reference documentation:

**Python**:

[AudioOutputOptions](https://docs.livekit.io/reference/python/livekit/agents/voice/room_io/index.html.md#livekit.agents.voice.room_io.AudioOutputOptions)

---

**Node.js**:

[RoomOutputOptions.audioOptions](https://docs.livekit.io/reference/agents-js/interfaces/agents.voice.RoomOutputOptions.html.md#audiooptions)

#### Participant management

Use the following parameters to configure which types of participants your agent can interact with.

- **`participant_kinds`** _(list<rtc.ParticipantKind.ValueType>)_ (optional) - Default: `[rtc.ParticipantKind.PARTICIPANT_KIND_SIP, rtc.ParticipantKind.PARTICIPANT_KIND_STANDARD]`: List of [participant types](https://docs.livekit.io/intro/basics/rooms-participants-tracks/participants.md#types-of-participants) accepted for auto subscription. The list determines which types of participants can be linked to the session. By default, includes `SIP`, `STANDARD`, and `CONNECTOR` participants.

- **`participant_identity`** _(string)_ (optional) - Default: `None`: The participant identity to link to. The linked participant is the one the agent listens and responds to. By default, links to the first participant that joins the room. You can override this in the `RoomIO` constructor or by using `RoomIO.set_participant()`.

#### Clean up options

Use the following parameters to configure cleanup options for session and room.

##### Close when participant leaves

An `AgentSession` is associated with a specific participant in a LiveKit room. This participant is the _linked participant_ for the session. By default, the session automatically closes when the linked participant leaves the room for any of the following reasons:

- `CLIENT_INITIATED`: User initiated the disconnect.
- `ROOM_DELETED`: Delete room API was called.
- `USER_REJECTED`: Call was rejected by the user (for example, the line was busy).

You can leave the session open by turning this behavior off using the following parameter:

**Python**:

`RoomOptions.close_on_disconnect`

---

**Node.js**:

`RoomInputOptions.closeOnDisconnect`

##### Delete room when session ends

Available in:
- [ ] Node.js
- [x] Python

You can automatically delete the room on session end by setting the `delete_room_on_close` parameter to `True`. By default, after the last participant leaves a room, it remains open for a grace period specified by `departure_timeout` set on the [room](https://docs.livekit.io/reference/other/roomservice-api.md#room). Enabling `delete_room_on_close` ensures the room is deleted immediately after the session ends.

- **`delete_room_on_close`** _(bool)_ (optional) - Default: `False`: Whether to delete the room on session end. Default: `False`.

### Example usage

**Python**:

```python
from livekit.agents import room_io
from livekit.plugins import noise_cancellation


room_options=room_io.RoomOptions(
    video_input=True,
    audio_input=room_io.AudioInputOptions(
        noise_cancellation=noise_cancellation.BVC(),
    ),
    text_output=room_io.TextOutputOptions(
        sync_transcription=False,
    ),
    participant_identity="user_123",
)

await session.start(
    agent=my_agent,
    room=room,
    room_options=room_options,
)

```

---

**Node.js**:

In the Node.js Agents framework, room configuration uses separate `inputOptions` and `outputOptions` parameters instead of a unified `RoomOptions` object. For the complete interface definitions and default values, refer to the [RoomIO source code](https://github.com/livekit/agents-js/blob/main/agents/src/voice/room_io/room_io.ts).

When calling `session.start()`, pass `inputOptions` and `outputOptions` as separate parameters:

```typescript
import { BackgroundVoiceCancellation } from '@livekit/noise-cancellation-node';

// ... session and agentsetup

await session.start({
  room: ctx.room,
  agent: myAgent,
  inputOptions: {
    textEnabled: true,
    audioEnabled: true,
    videoEnabled: true,
    noiseCancellation: BackgroundVoiceCancellation(),
    participantIdentity: "user_123",
  },
  outputOptions: {
    syncTranscription: false,
  },
});

```

To learn more about publishing audio and video, see the following topics:

- **[Agent speech and audio](https://docs.livekit.io/agents/multimodality/audio.md)**: Add speech, audio, and background audio to your agent.

- **[Vision](https://docs.livekit.io/agents/multimodality/vision.md)**: Give your agent the ability to see images and live video.

- **[Text and transcription](https://docs.livekit.io/agents/multimodality/text.md)**: Send and receive text messages and transcription to and from your agent.

- **[Realtime media](https://docs.livekit.io/transport/media.md)**: Tracks are a core LiveKit concept. Learn more about publishing and subscribing to media.

- **[Camera and microphone](https://docs.livekit.io/transport/media/publish.md)**: Use the LiveKit SDKs to publish audio and video tracks from your user's device.

### Custom RoomIO

For greater control over media sharing in a room, you can create a custom `RoomIO` object. For example, you might want to manually control which input and output devices are used, or to control which participants an agent listens to or responds to.

To replace the default one created in `AgentSession`, create a `RoomIO` object in your entrypoint function and pass it an instance of the `AgentSession` in the constructor. For examples, see the following in the repository:

- **[Push-to-talk](https://docs.livekit.io/agents/logic/turns.md#manual)**: Create a push-to-talk interface with manual turn control.

- **[Toggling audio](https://docs.livekit.io/agents/multimodality/text.md#toggle-audio)**: Toggle audio input and output in a hybrid session.

---

This document was rendered at 2026-08-28T04:22:11.869Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/sessions.md](https://docs.livekit.io/agents/logic/sessions.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-4"></a>
## Page 4: agents/logic/chat-context/
**Original URL:** https://docs.livekit.io/agents/logic/chat-context/  
**Source MD URL:** https://docs.livekit.io/agents/logic/chat-context.md

LiveKit docs › Build Agents › Logic & Structure › Chat context

---

# Chat context

> How to use ChatContext to manage conversation history in your agents.

## Overview

`ChatContext` is the conversation history sent to the LLM on each turn. It holds an ordered list of items — messages and events like agent handoffs — that together define what the model knows about the current conversation.

Each agent and task maintains its own `chat_ctx`. By default, a new agent or task starts with an empty context. You can initialize it at construction time, modify it during turns, or pass it across handoffs.

### Accessing the context

Within an agent or task, the current context is available as `self.chat_ctx`:

**Python**:

```python
class MyAgent(Agent):
    async def on_enter(self) -> None:
        print(self.chat_ctx.items)

```

---

**Node.js**:

```ts
const agent = voice.Agent.create({
  onEnter(ctx) {
    console.log(ctx.agent.chatCtx.items);
  },
});

```

The complete conversation history across all agents in a session is available on `session.history`:

**Python**:

```python
history = self.session.history

```

---

**Node.js**:

```ts
const history = ctx.session.history;

```

### Structure

`ChatContext` exposes an `items` list. Each item has a `type` field that determines what it represents:

| Type | Description |
| `message` | A conversation turn with a `role` (`system`, `user`, or `assistant`) and `content` (text, [images](#adding-images-and-video-frames), or instructions). |
| `function_call` | A tool invocation requested by the LLM. |
| `function_call_output` | The result returned from a tool call. |
| `agent_handoff` | Added automatically when control transfers between agents. |
| `agent_config_update` | Records a change to the agent's instructions or tools. |

To get the text of a `message` type item, use `text_content` (Python) or `textContent` (Node.js). This property is only available on `ChatMessage` items.

## Core operations

These are the most commonly used `ChatContext` operations. For additional methods like `insert()` and `get_by_id()`, see the reference for [Python](https://docs.livekit.io/reference/python/livekit/agents/llm/index.html.md#livekit.agents.llm.ChatContext) and [Node.js](https://docs.livekit.io/reference/agents-js/classes/agents.llm.ChatContext.html.md).

### Creating a context

Create a `ChatContext` and add messages directly:

**Python**:

```python
from livekit.agents import ChatContext

chat_ctx = ChatContext()
chat_ctx.add_message(role="system", content="You are a helpful assistant.")
chat_ctx.add_message(role="user", content="Hello!")

```

---

**Node.js**:

```ts
import { llm } from '@livekit/agents';

const chatCtx = new llm.ChatContext();
chatCtx.addMessage({ role: 'system', content: 'You are a helpful assistant.' });
chatCtx.addMessage({ role: 'user', content: 'Hello!' });

```

### Copying a context

Use `copy()` to create a snapshot that can be passed to another agent or modified independently. By default, `copy()` includes all items — messages, function calls, handoff markers, and system (instruction) messages.

You can filter the copy with the following options:

| Option | Description |
| `exclude_instructions` | Omit system/developer messages. |
| `exclude_function_call` | Omit function calls and their outputs. |
| `exclude_handoff` | Omit agent handoff markers. |
| `exclude_empty_message` | Omit messages with no content. |
| `exclude_config_update` | Omit agent config update items. |

**Python**:

```python
# Copy everything
full_copy = self.chat_ctx.copy()

# Copy only user/assistant turns, without tool calls
turns_only = self.chat_ctx.copy(exclude_instructions=True, exclude_function_call=True)

```

---

**Node.js**:

```ts
// Copy everything
const fullCopy = ctx.agent.chatCtx.copy();

// Copy only user/assistant turns, without tool calls
const turnsOnly = ctx.agent.chatCtx.copy({ excludeInstructions: true, excludeFunctionCall: true });

```

### Truncating a context

`truncate()` reduces a context to the most recent _n_ items. It always preserves system instructions even if they fall outside the item window, and strips any leading function call items to avoid orphaned tool results. This is useful when you want to pass only the tail of a long conversation to the next agent:

**Python**:

```python
recent = self.chat_ctx.copy().truncate(max_items=6)

```

---

**Node.js**:

```ts
const recent = ctx.agent.chatCtx.copy().truncate(6);

```

### Merging contexts

`merge()` combines items from another context into the current one, deduplicating by item ID and maintaining chronological order. This is useful after parallel tasks when you need to reunify their conversation histories:

**Python**:

```python
primary_ctx.merge(other_ctx)

# Merge without carrying over tool calls
primary_ctx.merge(other_ctx, exclude_function_call=True)

```

---

**Node.js**:

```ts
primaryCtx.merge(otherCtx);

// Merge without carrying over tool calls
primaryCtx.merge(otherCtx, { excludeFunctionCall: true });

```

## Common patterns

These examples show how to use `ChatContext` in typical agent workflows. Each pattern includes both Python and Node.js examples.

### Initialize with user data

Load user-specific context before the session starts and pass it to the agent constructor. This is the recommended approach for personalizing the agent without a round-trip to the LLM:

**Python**:

```python
initial_ctx = ChatContext()
initial_ctx.add_message(role="assistant", content=f"The user's name is {user_name}.")

await session.start(
    room=ctx.room,
    agent=MyAgent(chat_ctx=initial_ctx),
)

```

---

**Node.js**:

```ts
const initialCtx = new llm.ChatContext();
initialCtx.addMessage({ role: 'assistant', content: `The user's name is ${userName}.` });

await session.start({
  room: ctx.room,
  agent: voice.Agent.create({
    instructions: 'You are a helpful assistant.',
    chatCtx: initialCtx,
  }),
});

```

For a complete example, see [External data and RAG](https://docs.livekit.io/agents/logic/external-data.md).

### Modifying context during a turn

Override the [`on_user_turn_completed`](https://docs.livekit.io/agents/logic/nodes.md#on_user_turn_completed) node to inject additional context before the LLM generates its reply. Messages added here apply to the current turn only. Call `update_chat_ctx` to persist them:

**Python**:

```python
from livekit.agents import ChatContext, ChatMessage

async def on_user_turn_completed(
    self, turn_ctx: ChatContext, new_message: ChatMessage,
) -> None:
    # your function that retrieves context from a database, API, or other source
    extra = await fetch_relevant_data(new_message.text_content)
    turn_ctx.add_message(role="assistant", content=extra)
    await self.update_chat_ctx(turn_ctx)  # persist beyond this turn

```

---

**Node.js**:

```ts
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async onUserTurnCompleted(ctx, chatCtx, newMessage) {
    // your function that retrieves context from a database, API, or other source
    const extra = await fetchRelevantData(newMessage.textContent);
    chatCtx.addMessage({ role: 'assistant', content: extra });
    await ctx.agent.updateChatCtx(chatCtx); // persist beyond this turn
  },
});

```

For more details on pipeline nodes, see [Pipeline nodes & hooks](https://docs.livekit.io/agents/logic/nodes.md).

### Passing context during handoffs

Pass the current context to the next agent to preserve conversation history across handoffs. Use `exclude_instructions=True` to avoid forwarding the previous agent's system prompt:

**Python**:

```python
return NextAgent(chat_ctx=self.chat_ctx.copy(exclude_instructions=True))

```

---

**Node.js**:

```ts
return llm.handoff({
  agent: createNextAgent(
    ctx.session.currentAgent.chatCtx.copy({ excludeInstructions: true }),
  ),
});

```

For long conversations, summarize the context before passing it to reduce token cost. See [Summarizing context](https://docs.livekit.io/agents/logic/agents-handoffs.md#summarizing-context) for a complete example.

### Adding images and video frames

Message content can include images alongside text. Pass a list of text and `ImageContent` items to `add_message`:

**Python**:

```python
from livekit.agents import ChatContext
from livekit.agents.llm import ImageContent

initial_ctx = ChatContext()
initial_ctx.add_message(
    role="user",
    content=[
        "Here is a picture of me",
        ImageContent(image="https://example.com/image.jpg"),
    ],
)

```

---

**Node.js**:

```ts
import { llm } from '@livekit/agents';

const initialCtx = new llm.ChatContext();
initialCtx.addMessage({
  role: 'user',
  content: [
    'Here is a picture of me',
    llm.createImageContent({ image: 'https://example.com/image.jpg' }),
  ],
});

```

You can also inject live video frames into the context during a conversation turn. For details, see [Images](https://docs.livekit.io/agents/multimodality/vision/images.md) and [Video](https://docs.livekit.io/agents/multimodality/vision/video.md).

### Custom context for `generate_reply()`

Pass a modified `ChatContext` to `generate_reply()` to fully control the context for a single reply. This replaces the agent's session-level context for that reply only, which is useful when you need to exclude certain messages, inject one-off context, or override instructions:

**Python**:

```python
# Copy and modify the current context for this reply only
ctx = session.current_agent.chat_ctx.copy()
# Modify as needed: trim history, inject context, replace instructions, etc.
await session.generate_reply(chat_ctx=ctx)

```

---

**Node.js**:

```ts
// Copy and modify the current context for this reply only
const ctx = session.currentAgent.chatCtx.copy();
// Modify as needed: trim history, inject context, replace instructions, etc.
await session.generateReply({ chatCtx: ctx });

```

For the full list of `generate_reply()` parameters, see [Speech & audio](https://docs.livekit.io/agents/multimodality/audio.md#generate_reply-parameters).

### Standalone LLM usage

`ChatContext` also works outside of agents and sessions. Pass it directly to an LLM's `chat()` method for background tasks, preprocessing, or any workflow that needs LLM output without the voice pipeline.

For more details, see [Standalone LLM usage](https://docs.livekit.io/agents/models/llm.md#standalone-usage).

## Additional resources

- **[Agents & handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md)**: How to pass and summarize context across agent handoffs.

- **[External data & RAG](https://docs.livekit.io/agents/logic/external-data.md)**: Load external data into the chat context at session start or during turns.

- **[Pipeline nodes & hooks](https://docs.livekit.io/agents/logic/nodes.md)**: Modify the chat context at specific points in the voice pipeline.

- **[Images & video](https://docs.livekit.io/agents/multimodality/vision/images.md)**: Add images and video frames to the chat context.

- **[Speech & audio](https://docs.livekit.io/agents/multimodality/audio.md)**: Use a custom chat context with generate_reply().

- **[LLM overview](https://docs.livekit.io/agents/models/llm.md)**: Use ChatContext with standalone LLM calls outside of agents.

---

This document was rendered at 2026-08-28T04:22:11.862Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/chat-context.md](https://docs.livekit.io/agents/logic/chat-context.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-5"></a>
## Page 5: agents/logic/tasks/
**Original URL:** https://docs.livekit.io/agents/logic/tasks/  
**Source MD URL:** https://docs.livekit.io/agents/logic/tasks.md

LiveKit docs › Build Agents › Logic & Structure › Tasks & task groups

---

# Tasks and task groups

> Use tasks to build complex workflows for your voice AI agents.

## Overview

Tasks are focused, reusable units that perform a specific objective and return a typed result. They run inside an agent and take control of the session only until their goal is achieved. A task can define its own [tools](https://docs.livekit.io/agents/logic/tools.md) and starts executing when it's created within the context of an agent.

For multi-step flows, the framework provides `TaskGroup`. A task group executes an ordered sequence of tasks while allowing users to return to earlier steps for corrections. All tasks in a group share conversation context, and when the group finishes, a summarized result is returned to the agent that started it.

Tasks and task groups are core building blocks for complex voice AI [workflows](https://docs.livekit.io/agents/logic/workflows.md). Reach for them whenever you want a guided, structured conversation that returns a typed result, for example:

- Qualifying a lead.
- Collecting patient intake information.
- Running a follow-up survey or feedback call.
- Gathering booking or service-request details.
- Collecting structured information such as an address or payment details.
- Obtaining recording consent at the start of a call.
- Walking through a series of questions one step at a time.
- Any discrete action that should complete and yield control.

You can build a structured collection flow two ways:

- **With the SDK**: compose `AgentTask`s and `TaskGroup`s using the LiveKit Agents SDK in Python or Node.js. Use this when you want fine-grained control, want to reuse the same collection step across multiple agents, or are composing structured collection into a larger code-first agent.
- **In Agent Builder**: configure fields in [Data Collection mode](https://docs.livekit.io/agents/start/builder.md#data-collection) to prototype a flow in the browser. Builder compiles the configuration into the same `AgentTask` and `TaskGroup` primitives documented on this page, so you can [download the code](https://docs.livekit.io/agents/start/builder.md#convert-to-code) when you need to extend it.

> 💡 **Prebuilt tasks**
> 
> See [Prebuilt tasks](https://docs.livekit.io/agents/prebuilt/tasks.md) for ready-to-use task components such as email collection, address capture, DTMF input, and warm transfer. Use these alongside your own custom tasks inside a `TaskGroup`.

## Defining a task

Define a task by extending the `AgentTask` class in Python or by calling `AgentTask.create` in Node.js, specifying a result type using [generics](https://typing.python.org/en/latest/reference/generics.html) (Python) or TypeScript [generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) (Node.js). Use the `on_enter` method or `onEnter` hook to begin the task's interaction with the user, and call the `complete` method with a result when finished. The task has full support for tools, similar to an agent.

**Python**:

```python
from livekit.agents import AgentTask, function_tool

class CollectConsent(AgentTask[bool]):
    def __init__(self, chat_ctx=None):
        super().__init__(
            instructions="""
            Ask for recording consent and get a clear yes or no answer.
            Be polite and professional.
            """,
            chat_ctx=chat_ctx,
        )

    async def on_enter(self) -> None:
        await self.session.generate_reply(
            instructions="""
            Briefly introduce yourself, then ask for permission to record the call for quality assurance and training purposes.
            Make it clear that they can decline.
            """
        )

    @function_tool
    async def consent_given(self) -> None:
        """Use this when the user gives consent to record."""
        self.complete(True)

    @function_tool
    async def consent_denied(self) -> None:
        """Use this when the user denies consent to record."""
        self.complete(False)

```

---

**Node.js**:

```tsx
import { llm, voice } from '@livekit/agents';

function createCollectConsentTask(chatCtx?: llm.ChatContext) {
  const task = voice.AgentTask.create<boolean>({
    instructions: `
      Ask for recording consent and get a clear yes or no answer.
      Be polite and professional.
    `,
    chatCtx,
    tools: [
      llm.tool({
        name: 'consentGiven',
        description: 'Use this when the user gives consent to record.',
        execute: async () => {
          task.complete(true);
        },
      }),
      llm.tool({
        name: 'consentDenied',
        description: 'Use this when the user denies consent to record.',
        execute: async () => {
          task.complete(false);
        },
      }),
    ],
    async onEnter(ctx) {
      await ctx.session.generateReply({
        instructions: `
          Briefly introduce yourself, then ask for permission to record
          the call for quality assurance and training purposes.
          Make it clear that they can decline.
        `,
      });
    },
  });

  return task;
}

```

### Running a task

A task must be created within the context of an [active](https://docs.livekit.io/agents/logic/agents-handoffs.md#active-agent) `Agent`, and runs automatically when it's created. The task takes control of the session until it returns a result. Await the task to receive its result.

A task can only be awaited from one of three call sites in agent code:

- **`on_enter`**: runs the task as the agent becomes active. Useful for deterministic setup steps.
- **`on_exit`**: runs the task as the agent becomes inactive. Useful for wrap-up steps before a handoff or session end.
- **A tool function body**: the tool instantiates and awaits the task. The LLM decides when to invoke the tool, so delegation happens mid-conversation.

Awaiting an `AgentTask` outside these call sites raises a `RuntimeError`.

**Python**:

```python
from livekit.agents import Agent, function_tool, get_job_context

class CustomerServiceAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a friendly customer service representative.")

    async def on_enter(self) -> None:
        if await CollectConsent(chat_ctx=self.chat_ctx):
            await self.session.generate_reply(instructions="Offer your assistance to the user.")
        else:
            await self.session.generate_reply(instructions="Inform the user that you are unable to proceed and will end the call.")
            job_ctx = get_job_context()
            await job_ctx.delete_room()

```

---

**Node.js**:

```tsx
import { voice } from '@livekit/agents';

const customerServiceAgent = voice.Agent.create({
  instructions: 'You are a friendly customer service representative.',
  async onEnter(ctx) {
    const consent = await createCollectConsentTask(ctx.agent.chatCtx.copy()).run();

    if (consent) {
      await ctx.session.generateReply({
        instructions: 'Offer your assistance to the user.',
      });
    } else {
      await ctx.session.generateReply({
        instructions: 'Inform the user that you are unable to proceed and will end the call.',
      });
      ctx.session.shutdown({ reason: 'user-ended-call' });
    }
  },
});

```

> ℹ️ **Testing limitation**
> 
> `get_job_context()` is unavailable in test environments and raises a `RuntimeError` when called. If your agent uses `get_job_context()`, avoid testing code paths that invoke it, or mock the call using `unittest.mock`.

### Passing conversation history to a task

By default, a task starts with an empty chat context. To include the parent agent's conversation history, pass `chat_ctx` to the task constructor. Use `exclude_instructions=True` (Python) or `excludeInstructions: true` (Node.js) to omit the parent's system prompt so the task's own instructions take effect:

**Python**:

```python
class GetContactInfoTask(AgentTask[ContactInfoResult]):
    def __init__(self, chat_ctx=None):
        super().__init__(
            instructions="Collect the user's name, email address, and phone number.",
            chat_ctx=chat_ctx,
        )
    # ....

class CustomerServiceAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a friendly customer service representative.")

    @function_tool()
    async def collect_contact_info(self):
        """Collect the user's contact information."""
        # Pass conversation history without the agent's system prompt
        result = await GetContactInfoTask(
            chat_ctx=self.chat_ctx.copy(exclude_instructions=True)
        )
        return f"Recorded contact info for {result.name}."

```

---

**Node.js**:

```tsx
function createGetContactInfoTask(chatCtx?: llm.ChatContext) {
  return voice.AgentTask.create<ContactInfoResult>({
    instructions: "Collect the user's name, email address, and phone number.",
    chatCtx,
  });
}

const customerServiceAgent = voice.Agent.create({
  instructions: 'You are a friendly customer service representative.',
  tools: [
    llm.tool({
      name: 'collectContactInfo',
      description: "Collect the user's contact information.",
      execute: async (_, { ctx }) => {
        // Pass conversation history without the agent's system prompt
        const result = await createGetContactInfoTask(
          ctx.session.currentAgent.chatCtx.copy({ excludeInstructions: true }),
        ).run();
        return `Recorded contact info for ${result.name}.`;
      },
    }),
  ],
});

```

The `copy()` method also accepts additional filters like `exclude_function_call` and `exclude_handoff`. For a complete list of available filters, refer to [Copying a context](https://docs.livekit.io/agents/logic/chat-context.md#copying-a-context).

### Task results

Use any result type you want. For complex results, use a custom dataclass (Python) or interface (Node.js).

**Python**:

```python
from dataclasses import dataclass

@dataclass
class ContactInfoResult:
    name: str
    email_address: str
    phone_number: str

class GetContactInfoTask(AgentTask[ContactInfoResult]):
    # ....

```

---

**Node.js**:

```tsx
interface ContactInfoResult {
  name: string;
  emailAddress: string;
  phoneNumber: string;
}

const getContactInfoTask = voice.AgentTask.create<ContactInfoResult>({
  // ....
});

```

### Unordered collection within tasks

You can use a single task to collect multiple pieces of information in any order. The following example collects strengths, weaknesses, and work style in a hypothetical interview. Candidates can answer the questions in any order:

**Python**:

```python
@dataclass
class BehavioralResults:
    strengths: str
    weaknesses: str
    work_style: str

class BehavioralTask(AgentTask[BehavioralResults]):
    def __init__(self) -> None:
        super().__init__(
            instructions="Collect strengths, weaknesses, and work style in any order."
        )
        self._results = {}
    
    @function_tool()
    async def record_strengths(self, strengths_summary: str):
        """Record candidate's strengths"""
        self._results["strengths"] = strengths_summary
        self._check_completion()
    
    @function_tool()
    async def record_weaknesses(self, weaknesses_summary: str):
        """Record candidate's weaknesses"""
        self._results["weaknesses"] = weaknesses_summary
        self._check_completion()
    
    @function_tool()
    async def record_work_style(self, work_style: str):
        """Record candidate's work style"""
        self._results["work_style"] = work_style
        self._check_completion()
    
    def _check_completion(self):
        required_keys = {"strengths", "weaknesses", "work_style"}
        if self._results.keys() == required_keys:
            results = BehavioralResults(
                strengths=self._results["strengths"],
                weaknesses=self._results["weaknesses"],
                work_style=self._results["work_style"]
            )
            self.complete(results)
        else:
            self.session.generate_reply(
                instructions="Continue collecting remaining information."
            )

```

---

**Node.js**:

```tsx
import { llm, voice } from '@livekit/agents';
import { z } from 'zod';

interface BehavioralResults {
  strengths: string;
  weaknesses: string;
  workStyle: string;
}

function createBehavioralTask() {
  const results: Partial<BehavioralResults> = {};

  const checkCompletion = () => {
    const { strengths, weaknesses, workStyle } = results;
    if (strengths && weaknesses && workStyle) {
      task.complete({ strengths, weaknesses, workStyle });
    } else {
      task.session.generateReply({
        instructions: 'Continue collecting remaining information.',
      });
    }
  };

  const task = voice.AgentTask.create<BehavioralResults>({
    instructions: 'Collect strengths, weaknesses, and work style in any order.',
    tools: [
      llm.tool({
        name: 'recordStrengths',
        description: "Record candidate's strengths",
        parameters: z.object({
          strengthsSummary: z.string().describe("Summary of candidate's strengths"),
        }),
        execute: async ({ strengthsSummary }) => {
          results.strengths = strengthsSummary;
          checkCompletion();
        },
      }),
      llm.tool({
        name: 'recordWeaknesses',
        description: "Record candidate's weaknesses",
        parameters: z.object({
          weaknessesSummary: z.string().describe("Summary of candidate's weaknesses"),
        }),
        execute: async ({ weaknessesSummary }) => {
          results.weaknesses = weaknessesSummary;
          checkCompletion();
        },
      }),
      llm.tool({
        name: 'recordWorkStyle',
        description: "Record candidate's work style",
        parameters: z.object({
          workStyle: z.string().describe("Description of candidate's work style"),
        }),
        execute: async ({ workStyle }) => {
          results.workStyle = workStyle;
          checkCompletion();
        },
      }),
    ],
  });

  return task;
}

```

## Task group

> 🔥 **Experimental feature**
> 
> `TaskGroup` is currently experimental and the API might change in a future release.

Task groups let you build complex, user-friendly workflows that mirror real conversational behavior — where users might need to revisit or correct earlier steps without losing context. They're designed as ordered, multi-step flows that can be broken into discrete tasks, with built-in regression support for safely moving backward.

`TaskGroup` supports task chaining, which allows tasks to call or re-enter other tasks dynamically while maintaining the overall flow order. This lets users return to earlier steps as often as needed. All tasks in the group share the same conversation context, and when the group finishes, the summarized context can be passed back to the controlling agent.

### Configuration options

`TaskGroup` supports the following parameters:

- **`summarize_chat_ctx`** _(boolean)_ (optional) - Default: `true`: Whether to summarize the interactions within the `TaskGroup` into one message and merge into the main context.

- **`chat_ctx`** _(llm.ChatContext)_ (optional) - Default: `llm.ChatContext`: The shared [chat context](https://docs.livekit.io/agents/logic/chat-context.md) within the TaskGroup. Pass the current chat context to ensure conversational continuity.

- **`return_exceptions`** _(boolean)_ (optional) - Default: `false`: Controls error handling when a sub-task raises an unhandled exception. When set to `true`, the exception is added to the results dictionary and the sequence continues. When set to `false`, the exception propagates immediately and the sequence stops.

- **`on_task_completed`** _((event: TaskCompletedEvent) => Promise<void>)_ (optional): An async callback invoked after each sub-task completes successfully. It receives a `TaskCompletedEvent` with the following fields:

- `agent_task`: `AgentTask` instance that just finished.
- `task_id`: String ID of the task.
- `result`: Value the task returned.

### Basic usage

Initialize and set up a `TaskGroup` by adding tasks to it. Add tasks in the order they should be executed:

**Python**:

```python
from livekit.agents.beta.workflows import GetEmailTask, TaskGroup


# Create and configure TaskGroup with the current agent's chat context
chat_ctx = self.chat_ctx
task_group = TaskGroup(chat_ctx=chat_ctx)

# Add tasks using lambda factories
task_group.add(
    lambda: GetEmailTask(), 
    id="get_email_task", 
    description="Collects the user's email"
)
task_group.add(
    lambda: GetCommuteTask(), 
    id="get_commute_task", 
    description="Records the user's commute flexibility"
)

# Execute the task group
results = await task_group  # Returns TaskGroupResult object
task_results = results.task_results

# Access results by task ID
print(task_results)
# Output: {
#   "get_email_task": GetEmailResult(email="john.doe@gmail.com"), 
#   "get_commute_task": CommuteResult(can_commute=True, commute_method="subway")
# }

```

---

**Node.js**:

```tsx
import { workflows, llm } from '@livekit/agents';

// Create and configure TaskGroup with the current agent's chat context
const chatCtx = ctx.agent.chatCtx.copy();
const taskGroup = new workflows.TaskGroup({ chatCtx });

// Add tasks using arrow-function factories
taskGroup.add(() => createGetEmailTask(), {
  id: 'get_email_task',
  description: "Collects the user's email",
});
taskGroup.add(() => createGetCommuteTask(), {
  id: 'get_commute_task',
  description: "Records the user's commute flexibility",
});

// Execute the task group
const results = await taskGroup.run(); // Returns TaskGroupResult object
const taskResults = results.taskResults;

// Access results by task ID
console.log(taskResults);
// Output: {
//   get_email_task: { email: "john.doe@gmail.com" },
//   get_commute_task: { canCommute: true, commuteMethod: "subway" }
// }

```

The `TaskGroup.add()` method takes a task factory and an options object (Python: `task_factory`, `id`, `description` as arguments; Node.js: factory function and `{ id, description }`):

- **Task factory**: A callable that returns a task instance (Python: typically a lambda; Node.js: an arrow function).
- **id**: A string identifier for the task used to access results.
- **description**: A string description that helps the LLM understand when to regress to this task.

The factory allows for tasks to be reinitialized with the same arguments when revisited. The task id and description are passed to the LLM as task identifiers when the LLM needs to regress to a previous task. This allows the LLM to understand the task's purpose and context when revisiting it. Task chaining is supported, allowing users to return to earlier steps as often as needed.

All tasks share the same conversation context. The context is summarized and passed back to the controlling agent when the group finishes. This option can be disabled when initializing the task group:

**Python**:

```python
# Disable context summarization
task_group = TaskGroup(summarize_chat_ctx=False)

```

---

**Node.js**:

```tsx
// Disable context summarization
const taskGroup = new workflows.TaskGroup({ summarizeChatCtx: false });

```

### Task completion callbacks

Add a callback function to a task group to run custom logic after each task completes. The callback receives a `TaskCompletedEvent` containing the completed task's ID, instance, and result.

Use the `on_task_completed` parameter to set the callback function. The following example prints a message after each task finishes:

**Python**:

```python
from livekit.agents.beta.workflows import TaskGroup, TaskCompletedEvent

async def print_task_result(event: TaskCompletedEvent) -> None:
    print(f"Task '{event.task_id}' completed with result: {event.result}")

task_group = TaskGroup(
    chat_ctx=self.chat_ctx,
    on_task_completed=print_task_result,
)
task_group.add(
    lambda: IntroTask(),
    id="intro_task",
    description="Collects name and introduction",
)
task_group.add(
    lambda: CommuteTask(),
    id="commute_task",
    description="Asks about commute flexibility",
)

results = await task_group

```

---

**Node.js**:

```tsx
import { workflows } from '@livekit/agents';

const taskGroup = new workflows.TaskGroup({
  chatCtx: ctx.agent.chatCtx.copy(),
  onTaskCompleted: async ({ taskId, result }) => {
    console.log(`Task '${taskId}' completed with result:`, result);
  },
});
taskGroup.add(() => createIntroTask(), {
  id: 'intro_task',
  description: 'Collects name and introduction',
});
taskGroup.add(() => createCommuteTask(), {
  id: 'commute_task',
  description: 'Asks about commute flexibility',
});

const results = await taskGroup.run();

```

### Early exit from a task group

Avoid calling `session.shutdown()` directly from `on_task_completed`. The callback runs while `TaskGroup` is still iterating its task stack. Because the group hasn't finished yet, shutting down the session at that point raises a `RuntimeError`.

To skip the remaining tasks when an earlier task signals an exit condition, raise a custom exception from the callback and catch it where you await the task group. With the default `return_exceptions=False`, `TaskGroup` propagates the exception to the awaiting code:

**Python**:

```python
from livekit.agents.beta.workflows import TaskGroup, TaskCompletedEvent

class ExistingProfileFound(Exception):
    """Raised to skip remaining intake tasks when a returning user is detected."""

async def check_for_existing_profile(event: TaskCompletedEvent) -> None:
    if event.task_id == "get_email_task":
        if database.find_user_by_email(event.result.email_address):
            raise ExistingProfileFound()

task_group = TaskGroup(
    chat_ctx=self.chat_ctx,
    on_task_completed=check_for_existing_profile,
)
task_group.add(lambda: GetEmailTask(), id="get_email_task", description="Collects the user's email")
task_group.add(lambda: GetAddressTask(), id="get_address_task", description="Collects the user's address")

try:
    results = await task_group
except ExistingProfileFound:
    # Safe to run cleanup logic here — the task group is no longer iterating
    await self.session.generate_reply(instructions="Welcome the returning user.")

```

---

**Node.js**:

Prebuilt tasks aren't available in Node.js. In the following example, you must [define your own tasks](#define-task) for `GetEmailTask` and `GetAddressTask`:

```tsx
import { workflows } from '@livekit/agents';

class ExistingProfileFound extends Error {}

const taskGroup = new workflows.TaskGroup({
  chatCtx: ctx.agent.chatCtx.copy(),
  onTaskCompleted: async ({ taskId, result }) => {
    if (taskId === 'get_email_task') {
      const { email } = result as { email: string };
      if (database.findUserByEmail(email)) {
        throw new ExistingProfileFound();
      }
    }
  },
});

taskGroup.add(() => createGetEmailTask(), {
  id: 'get_email_task',
  description: "Collects the user's email",
});
taskGroup.add(() => createGetAddressTask(), {
  id: 'get_address_task',
  description: "Collects the user's address",
});

try {
  const results = await taskGroup.run();
} catch (e) {
  if (e instanceof ExistingProfileFound) {
    // Safe to run cleanup logic here — the task group is no longer iterating
    await ctx.session.generateReply({ instructions: 'Welcome the returning user.' });
  } else {
    throw e;
  }
}

```

This pattern requires the default value `return_exceptions=False`. When `return_exceptions` is `True`, `TaskGroup` stores the exception in the results dictionary and continues the sequence instead of stopping.

`TaskGroup` uses the same exception-based mechanism internally to handle [regression](#taskgroup) — when the LLM requests to revisit an earlier task, the active task is completed with an internal exception that the group catches and uses to reorder the task stack.

### Complete workflow example

The following is a complete example showing how to build an interview workflow with `TaskGroup`. It collects basic candidate information and then asks about their commute flexibility:

**Python**:

```python
from livekit.agents import AgentTask, function_tool, RunContext
from livekit.agents.beta.workflows import TaskGroup
from dataclasses import dataclass

@dataclass
class IntroResults:
    name: str
    intro: str

@dataclass 
class CommuteResults:
    can_commute: bool
    commute_method: str

class IntroTask(AgentTask[IntroResults]):
    def __init__(self) -> None:
        super().__init__(
            instructions="Welcome the candidate and collect their name and introduction."
        )
    
    async def on_enter(self) -> None:
        await self.session.generate_reply(
            instructions="Welcome the candidate and gather their name."
        )
    
    @function_tool()
    async def record_intro(self, context: RunContext, name: str, intro_notes: str) -> None:
        """Record the candidate's name and introduction"""
        context.session.userdata.candidate_name = name
        results = IntroResults(name=name, intro=intro_notes)
        self.complete(results)

class CommuteTask(AgentTask[CommuteResults]):
    def __init__(self) -> None:
        super().__init__(
            instructions="Ask about the candidate's ability to commute to the office."
        )
    
    @function_tool()
    async def record_commute_flexibility(
        self, 
        context: RunContext, 
        can_commute: bool, 
        commute_method: str
    ) -> None:
        """Record commute flexibility and transportation method"""
        results = CommuteResults(can_commute=can_commute, commute_method=commute_method)
        self.complete(results)

# Set up the workflow
task_group = TaskGroup()
task_group.add(
    lambda: IntroTask(), 
    id="intro_task", 
    description="Collects name and introduction"
)
task_group.add(
    lambda: CommuteTask(), 
    id="commute_task", 
    description="Asks about commute flexibility"
)

# Execute and get results
results = await task_group
task_results = results.task_results

```

---

**Node.js**:

```tsx
import { workflows, llm, voice } from '@livekit/agents';
import { z } from 'zod';

interface IntroResults {
  name: string;
  intro: string;
}

interface CommuteResults {
  canCommute: boolean;
  commuteMethod: string;
}

interface InterviewUserData {
  candidateName?: string;
}

function createIntroTask() {
  const task = voice.AgentTask.create<IntroResults, InterviewUserData>({
    instructions: 'Welcome the candidate and collect their name and introduction.',
    tools: [
      llm.tool({
        name: 'recordIntro',
        description: "Record the candidate's name and introduction",
        parameters: z.object({
          name: z.string().describe("The candidate's name"),
          introNotes: z.string().describe('Introduction notes'),
        }),
        execute: async ({ name, introNotes }, { ctx }) => {
          ctx.userData.candidateName = name;
          task.complete({ name, intro: introNotes });
        },
      }),
    ],
    async onEnter(ctx) {
      await ctx.session.generateReply({
        instructions: 'Welcome the candidate and gather their name.',
      });
    },
  });

  return task;
}

function createCommuteTask() {
  const task = voice.AgentTask.create<CommuteResults>({
    instructions: "Ask about the candidate's ability to commute to the office.",
    tools: [
      llm.tool({
        name: 'recordCommuteFlexibility',
        description: 'Record commute flexibility and transportation method',
        parameters: z.object({
          canCommute: z.boolean().describe('Whether the candidate can commute'),
          commuteMethod: z.string().describe('Transportation method'),
        }),
        execute: async ({ canCommute, commuteMethod }) => {
          task.complete({ canCommute, commuteMethod });
        },
      }),
    ],
  });

  return task;
}

// Set up the workflow
const taskGroup = new workflows.TaskGroup();
taskGroup.add(() => createIntroTask(), {
  id: 'intro_task',
  description: 'Collects name and introduction',
});
taskGroup.add(() => createCommuteTask(), {
  id: 'commute_task',
  description: 'Asks about commute flexibility',
});

// Execute and get results
const results = await taskGroup.run();
const taskResults = results.taskResults;

```

### Best practices for testing task groups

The following sections provide specific guidelines for testing `TaskGroup` in both Python and Node.js SDKs. For Python agents, you can evaluate a task group across a complete, LLM-driven conversation by running it as an [agent simulation](https://docs.livekit.io/agents/start/testing/simulations.md).

#### Add a short delay before the first session.run() in Python

`TaskGroup` temporarily sets `llm=None` during task transitions. In the Python SDK, `session.run()` doesn't fall back to `session.llm` during this window, which can raise the following exception if the test calls `session.run()` too early:

`RuntimeError: trying to generate reply without an LLM model.`

Add a small delay between `session.start()` and the first `session.run()` call so the first sub-task can take over:

```python
await session.start()
await asyncio.sleep(0.5)
await session.run(...)

```

This delay isn't required in Node.js because `null` LLM values automatically fall back to `session.llm`.

#### Parse function call arguments

Test run results store function call arguments as raw JSON strings. The built-in assertion helpers (`is_function_call`, `contains_function_call` in Python, and `isFunctionCall`, `containsFunctionCall` in Node.js) parse the JSON for you and support partial-dict matching, so prefer them when checking known argument values.

Parse the JSON manually only when you need an assertion the helpers can't express, such as, range checks, regular expression matches, or comparisons against a value computed in the test.

**Python**:

Use the helper for direct value matches:

```python
result.expect.contains_function_call(
    name="record_commute",
    arguments={"can_commute": True},
)

```

Parse `item.arguments` only when you need a richer assertion:

```python
fnc = result.expect.contains_function_call(name="record_experience")
args = json.loads(fnc.event().item.arguments)
assert args["years_of_experience"] >= 5

```

---

**Node.js**:

Use the helper for direct value matches:

```typescript
result.expect.containsFunctionCall({
  name: 'recordCommute',
  args: { canCommute: true },
});

```

Parse `item.args` only when you need a richer assertion:

```typescript
const fnc = result.expect.containsFunctionCall({ name: 'recordExperience' });
const args = JSON.parse(fnc.event().item.args);
expect(args.yearsOfExperience).toBeGreaterThanOrEqual(5);

```

#### Initialize userData when tasks depend on it

If tasks read or write `ctx.userData`, initialize it when creating the session. The failure mode differs across SDKs:

- **Python:** accessing `session.userdata` when it's unset raises `ValueError: AgentSession userdata is not set`.
- **Node.js:** accessing `session.userData` when it's unset throws `Error: Voice agent userData is not set`.

In either case, pass an initialized value to the session constructor:

**Python**:

```python
AgentSession(llm=llm, userdata=MyUserdata(candidate_name=""))

```

---

**Node.js**:

```typescript
new voice.AgentSession<MyUserData>({ llm, userData: { candidateName: '' } });

```

#### Don't assert on startup output

Output generated during agent startup (for example from `session.say()` or `session.generate_reply()`) is not included in `RunResult`.

Structure tests to assert agent responses to user input, not startup messages.

#### Avoid awaiting playout inside onEnter() when triggered from a tool

If `onEnter()` runs inside a tool's `execute` function, awaiting speech playout can cause a circular wait. The tool call remains active until `onEnter()` returns.

Call `generateReply()` without awaiting it:

**Python**:

```python
async def on_enter(self) -> None:
    self.session.generate_reply(instructions="Welcome the user.")  # don't await

```

---

**Node.js**:

```typescript
const task = voice.AgentTask.create({
  onEnter(ctx) {
    ctx.session.generateReply({ instructions: 'Welcome the user.' }); // no await
  },
});

```

#### Consider multi-turn LLM behavior

An LLM might not call a task's completion tool on the first turn. It might require multiple exchanges before completing the task.

Prefer `containsFunctionCall()` over `nextEvent()` for more resilient tests, and use generous timeouts:

- `containsFunctionCall()` checks whether the call occurred anywhere in the response.
- `nextEvent()` only checks the immediate next event.

**Python**:

```python
result.expect.contains_function_call(name="consent_given")

```

---

**Node.js**:

```typescript
result.expect.containsFunctionCall({ name: 'consentGiven' });

```

#### Increase cleanup timeouts in Node.js

Session cleanup can be slow when a `TaskGroup` is mid-flow. Set an explicit timeout in your cleanup hook to avoid `afterEach` failures:

```typescript
afterEach(async () => {
  await session?.close();
}, 30000);

```

#### Example tests for task group

- **[Testing a task group (Node.js)](https://github.com/livekit/agents-js/blob/main/examples/src/testing/basic_task_group.test.ts)**: This test suite verifies the behavior of the basic task group example in the Node.js GitHub repo.

- **[Testing a survey agent task group (Python)](https://github.com/livekit/agents/blob/main/examples/survey/test_survey_agent.py)**: This test suite verifies the behavior of the survey agent task group example in the Python GitHub repo.

## Examples

The following examples show tasks and task groups in production-style agents:

- **[Survey agent (Python)](https://github.com/livekit/agents/blob/main/examples/survey/agent.py)**: Interview screening agent that runs a TaskGroup of five tasks: intro, email capture, commute, experience, and behavioral. Uses session userdata, a disqualify tool, CSV export, and post-interview LLM evaluation.

- **[Basic agent task (Node.js)](https://github.com/livekit/agents-js/blob/main/examples/src/basic_agent_task.ts)**: Survey agent that runs reusable `AgentTask`s from `onEnter` and from tools. Uses a generic info-collection task, then shows handoff to a separate weather agent and back.

- **[Basic task group (Node.js)](https://github.com/livekit/agents-js/blob/main/examples/src/basic_task_group.ts)**: Onboarding agent that starts a two-step TaskGroup (name then email) via a tool. Demonstrates `onTaskCompleted`, context summarization, and regression so users can correct earlier answers (e.g. "change my name to …").

## Additional resources

The following topics provide more information on creating complex workflows for your voice AI agents.

- **[Workflows](https://docs.livekit.io/agents/logic/workflows.md)**: Complete guide to defining and using workflows in your agents.

- **[Data Collection mode in Agent Builder](https://docs.livekit.io/agents/start/builder.md#data-collection)**: Build a structured data collection agent right from your browser.

- **[Tool definition and use](https://docs.livekit.io/agents/logic/tools.md)**: Complete guide to defining and using tools in your agents.

- **[Nodes](https://docs.livekit.io/agents/logic/nodes.md)**: Add custom behavior to any component of the voice pipeline.

- **[Testing & evaluation](https://docs.livekit.io/agents/start/testing.md)**: Test every aspect of your agents with a custom test suite.

---

This document was rendered at 2026-08-28T04:22:11.883Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/tasks.md](https://docs.livekit.io/agents/logic/tasks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-6"></a>
## Page 6: agents/logic/workflows/
**Original URL:** https://docs.livekit.io/agents/logic/workflows/  
**Source MD URL:** https://docs.livekit.io/agents/logic/workflows.md

LiveKit docs › Build Agents › Logic & Structure › Workflows

---

# Workflows

> How to model repeatable, accurate workflows through agents, handoffs, and tasks.

## Overview

The LiveKit Agents framework lets you build sophisticated voice AI apps with multiple personas, conversation phases, or specialized capabilities using agents, handoffs, and tasks.

## Core constructs

An [**agent session**](https://docs.livekit.io/agents/logic/sessions.md) is the main orchestrator of your voice AI app and can be composed of one or more agents. Agents are one of the core building blocks of a workflow that also includes tasks and tools. Each plays a distinct role in creating a flexible, maintainable system:

- [**Agents**](https://docs.livekit.io/agents/logic/agents-handoffs.md) hold long-lived control of a session. They define instructions, reasoning behavior, and tools, and can transfer control to another agent when different rules or capabilities are required.
- [**Tools**](https://docs.livekit.io/agents/build/tools.md) are user-defined functions callable by the model. They allow the agent to perform actions beyond generative text, such as reading from or writing to external systems. Tool invocations are model-driven: the LLM chooses to call them based on context, and the returned results are fed back to the model for continued reasoning. Tools can also trigger agent **handoffs**.
- [**Tasks**](https://docs.livekit.io/agents/logic/tasks.md) are short-lived units of work that run to completion and return a typed result. Unlike agents, tasks do not persist; they take temporary control only while executing. Tasks can include tool definitions used to complete their objectives.
- [**Task groups**](https://docs.livekit.io/agents/logic/tasks.md#taskgroup) run sequences of tasks for multi-step operations. They allow users to revisit earlier steps if corrections are needed, and all tasks in a group share conversation context. The summarized result is returned to the controlling agent when the group finishes.

This architecture makes workflows explicit and predictable: agents manage ongoing conversational control, tasks encapsulate discrete operations, tools execute side effects and enable handoffs, and task groups coordinate ordered multi-step flows with regression support. Together, these constructs form a testable and maintainable execution model for non-trivial voice AI systems.

## Choosing a pattern

Start with a single agent and a small set of tools. A single agent can handle multi-step flows by updating its instructions or changing available tools between conversation phases. For example, you might use one set of tools during booking lookup and another during confirmation.

Each pattern you layer on top of a single agent adds complexity, latency, or context management overhead. Split workflows only when you encounter a concrete limitation:

- **Instruction bloat:** The system prompt becomes large enough that the model starts to underperform on its primary task.
- **Conflicting tool access:** Different phases of the conversation require different tools or permissions.
- **Multi-turn data collection:** A workflow step requires its own LLM loop to gather and validate structured input over several conversational turns.
- **Backtracking:** Users need to revisit earlier steps to correct previously provided information.

When one of those signals is present, choose the simplest construct that addresses it:

| Pattern | Session control | Context | Latency cost | Correction handling | Best for |
| **Single agent + [tools](https://docs.livekit.io/agents/logic/tools.md)** | One agent stays in control for the entire session. | Full conversation context is retained. | None. | Manual. Re-prompt or re-ask. | Simple flows with few tools and no distinct conversation phases. |
| **[Supervisor pattern](https://docs.livekit.io/agents/logic/supervisor-pattern.md)** | One agent stays in control; tasks take temporary control and return a typed result. | Supervisor keeps full context. Tasks receive a scoped copy. | Minimal. Task runs within the same session. | Re-run the task from the supervisor. | One agent coordinates focused, reusable sub-operations such as data collection or verification. |
| **[Agent handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md)** | Control transfers fully to a new agent. The original agent doesn't participate afterward. | Explicit: pass `chat_ctx`, summarize, or start fresh. | Handoff overhead per transition. | Manual. Hand off back to the previous agent. | Distinct roles, model specialization, or permission boundaries between conversation phases. |
| **[Task groups](https://docs.livekit.io/agents/logic/tasks.md#taskgroup)** | TaskGroup orchestrates an ordered sequence of tasks. | Shared within the group. Summarized on completion. | Minimal. Sequential within the same session. | Built-in. Users can regress to earlier completed steps. | Ordered multi-step data collection where users might need to revisit earlier steps. |

These patterns aren't mutually exclusive. Different phases of a conversation can use different patterns. For example, an intake supervisor can hand off to a billing agent that uses its own supervisor pattern. For a deeper comparison, see [When to use the supervisor pattern](https://docs.livekit.io/agents/logic/supervisor-pattern.md#when-to-use).

### Example: booking flow

Consider an appointment agent that handles booking, rescheduling, and cancellation. All three intents share an initial lookup step. A single agent with tools works well here if the instructions stay concise and the tools don't conflict.

When the intents diverge, the supervisor pattern is a better fit. Booking might require multi-turn address collection, rescheduling needs calendar-specific tools, and cancellation requires a separate consent flow. One supervisor routes to focused specialist tasks and stays in control of the session, so it can handle mid-conversation intent changes if a user starts booking but decides to reschedule instead.

If each intent also requires a strict ordered sequence of sub-steps with backtracking, a task group within the supervisor is appropriate.

If the appointment flow ends with a payment step where the agent needs different instructions, tools, and access controls, an agent handoff is appropriate: the supervisor hands off to a dedicated billing agent once the appointment is confirmed.

## Best practices

Before building your workflow, map out the conversation phases, identify where different personas or capabilities are needed, and determine which operations are short-lived versus continuous. The following guidelines help you choose the right pattern for each part of your workflow:

- Create separate [**agents**](https://docs.livekit.io/agents/logic/agents-handoffs.md) when you need distinct reasoning behavior or tool access.
- Use [**tasks**](https://docs.livekit.io/agents/logic/tasks.md) for discrete operations that must complete before continuing the conversation (for example, consent collection, data capture, or verification).
- Expose external actions through [**tools**](https://docs.livekit.io/agents/logic/tools.md) with clear purpose and meaningful return values that contribute to reasoning.
- Plan how [**conversation context**](https://docs.livekit.io/agents/logic/agents-handoffs.md#context-preservation) is preserved or reset across agents. Some transitions require full continuity; others benefit from a clean slate.
- Use a [**task group**](https://docs.livekit.io/agents/logic/tasks.md#taskgroup) for ordered multi-step processes that might need to revisit earlier steps.
- Build workflows incrementally. Add [**tests and evals**](https://docs.livekit.io/agents/start/testing.md) to verify tool, task, and agent behavior, and run [**simulations**](https://docs.livekit.io/agents/start/testing/simulations.md) to check the whole flow end to end.
- Design for **user experience**: announce handoffs, preserve relevant context to avoid repetition, and handle correction paths cleanly.

Following these patterns keeps complex workflows predictable, testable, and extensible.

## Additional resources

For more information on specific topics related to building voice AI workflows, see the following topics:

- **[Supervisor pattern](https://docs.livekit.io/agents/logic/supervisor-pattern.md)**: Route work to specialist tasks while one agent stays in control.

- **[Agents and handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md)**: Define agents and agent handoffs to build multi-agent voice AI workflows.

- **[Tasks & task groups](https://docs.livekit.io/agents/logic/tasks.md)**: Use tasks and task groups to execute discrete operations and build complex workflows.

- **[Prompting guide](https://docs.livekit.io/agents/start/prompting.md)**: Complete guide to writing good instructions for your agents.

- **[Tool definition and use](https://docs.livekit.io/agents/build/tools.md)**: Use tools to call external services, inject custom logic, agent handoffs, and more.

- **[Testing & evaluation](https://docs.livekit.io/agents/start/testing.md)**: Test every aspect of your agents with a custom test suite.

- **[Agent-assisted warm transfer](https://docs.livekit.io/telephony/features/transfers/warm.md)**: Transfer calls to a human operator while providing a contextual summary.

- **[Call forwarding (cold transfer)](https://docs.livekit.io/telephony/features/transfers/cold.md)**: Forward calls to another number or SIP endpoint using SIP REFER.

---

This document was rendered at 2026-08-28T04:22:11.899Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/workflows.md](https://docs.livekit.io/agents/logic/workflows.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-7"></a>
## Page 7: agents/logic/supervisor-pattern/
**Original URL:** https://docs.livekit.io/agents/logic/supervisor-pattern/  
**Source MD URL:** https://docs.livekit.io/agents/logic/supervisor-pattern.md

LiveKit docs › Build Agents › Logic & Structure › Supervisor pattern

---

# Supervisor pattern

> A central agent routes work to specialist tasks while staying in control of the session.

## Overview

The supervisor pattern keeps a single [agent](https://docs.livekit.io/agents/logic/agents-handoffs.md) in long-lived control of a session and routes discrete work to specialist [tasks](https://docs.livekit.io/agents/logic/tasks.md). The supervisor decides when each task runs, integrates the result, and continues the conversation. Each task is independent, with its own instructions, tools, and LLM loop. This allows the supervisor to coordinate a set of focused sub-agents rather than handling everything in one prompt.

Use this pattern when one agent should remain aware of the full conversation while delegating focused operations such as collecting structured information, running verification steps, or retrieving external data. The supervisor remains the conversational entry point, while specialists handle narrow work and return results.

## When to use the supervisor pattern

The supervisor pattern is one option among several for structuring a voice AI application. Choose the simplest construct that fits your workflow:

- **A single agent with [tools](https://docs.livekit.io/agents/logic/tools.md)** can handle the conversation if one set of instructions and tools is sufficient.
- **The supervisor pattern** is appropriate when one agent should remain in control while delegating discrete operations to focused, reusable tasks.
- **[Agent handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md)** are appropriate when one agent's role is complete and another should take over with different instructions or tools. The original agent doesn't participate in subsequent steps.
- **[Task groups](https://docs.livekit.io/agents/logic/tasks.md#taskgroup)** are appropriate for ordered, multi-step delegation where users might need to revisit earlier steps. A task group structures supervisor-driven delegation with built-in sequencing and support for revisiting prior steps.

These patterns aren't mutually exclusive and are often combined in more complex voice AI applications. Different phases of a conversation might use different patterns. For example, an intake agent might use the supervisor pattern to collect structured information, then hand off to a billing agent that uses its own supervisor pattern for payment collection.

For broader context on agent patterns, see the LiveKit blog posts on the [supervisor pattern](https://livekit.com/blog/supervisor-pattern-voice-agents), the [ReAct pattern](https://livekit.com/blog/react-pattern-voice-agents), and the [human-in-the-loop pattern](https://livekit.com/blog/human-in-the-loop-voice-agents).

## Pattern anatomy

The pattern has three parts:

- **The supervisor.** A long-lived `Agent` whose instructions define available specialists, when to invoke each one, and how to interpret their results.
- **The specialists.** One or more `AgentTask` instances, each with focused instructions, its own tools, and a typed result. See [Tasks and task groups](https://docs.livekit.io/agents/logic/tasks.md) for the full task API.
- **The delegation surface.** The mechanism used to start a specialist. The most common approach is a function tool on the supervisor: the tool body instantiates and awaits a task, then returns its result to the LLM. Alternatively, lifecycle hooks (`on_enter` or `on_exit`) can trigger tasks at deterministic points.

Tools and tasks are distinct constructs. A tool is regular code that can perform any operation: call an API, write to a database, or start a task. A task is a sub-conversation with its own LLM loop, which can in turn call tools. Starting a task from a tool is one of several entry points; see [Running a task](https://docs.livekit.io/agents/logic/tasks.md#run-task) for the others and runtime constraints.

## Designing a supervisor

The pattern's effectiveness depends on a few design choices.

### Sizing tasks

Decide what belongs in a task versus a tool versus the supervisor itself:

- **Tool**: single deterministic operations that don't require LLM reasoning, such as fetching a record by ID, sending an email, or performing a computation.
- **Task**: focused sub-conversations that require reasoning and might span multiple turns, such as collecting a structured address, handling consent flows, or verifying identity.
- **Supervisor**: the conversational frame and routing logic. Domain-specific reasoning shouldn't live here.

A useful guideline is that if the model needs to ask clarifying questions, the work belongs in a task. If it's a single function call with arguments, it belongs in a tool.

### Writing supervisor instructions

The supervisor's instructions should explicitly name each specialist tool and describe when to use it. Be specific because routing behavior depends heavily on these descriptions. Instructions should also define how to interpret each result. For example: “After `lookup_order` returns, summarize the order status and ask whether the user would like to make changes.”

The supervisor sets the conversational tone. Specialist tasks define their own behavior, while the supervisor frames the overall interaction.

### Validating results

Treat task results as untrusted input until validated by the supervisor. Check results before continuing the conversation and define a recovery path for errors or unexpected outputs. Although task results are typed, validation is still required for the underlying values.

## Example: routing between specialist tasks

The following supervisor handles two kinds of customer requests by routing to different specialist tasks. `LookupOrderTask` collects an order number and returns the order status. `UpdateAddressTask` collects a new shipping address and returns confirmation. The supervisor exposes one function tool per task; the LLM picks the right tool based on what the user says.

**Python**:

```python
from dataclasses import dataclass
from livekit.agents import Agent, AgentTask, function_tool


# Typed result returned when LookupOrderTask completes.
@dataclass
class OrderLookupResult:
    order_id: str
    status: str


# Typed result returned when UpdateAddressTask completes.
@dataclass
class AddressUpdateResult:
    address: str


# The generic parameter ties this task to the type it returns.
class LookupOrderTask(AgentTask[OrderLookupResult]):
    def __init__(self, chat_ctx=None) -> None:
        super().__init__(
            instructions=(
                "Ask the customer for their order number. "
                "If they don't have one, ask them to check their email."
            ),
            chat_ctx=chat_ctx,
        )

    async def on_enter(self) -> None:
        await self.session.generate_reply(
            instructions="Ask for the order number."
        )

    # Task-internal tool. The task's LLM calls this when the user
    # provides an order number. Calling self.complete(...) ends the
    # task and returns the typed result to the supervisor.
    @function_tool()
    async def order_number_collected(self, order_id: str) -> None:
        """Call when the customer has provided their order number."""
        # In a real system, look up the order in your database here.
        self.complete(OrderLookupResult(order_id=order_id, status="shipped"))


class UpdateAddressTask(AgentTask[AddressUpdateResult]):
    def __init__(self, chat_ctx=None) -> None:
        super().__init__(
            instructions=(
                "Collect the customer's new shipping address: street, city, "
                "state, and zip code. Read it back to confirm before completing."
            ),
            chat_ctx=chat_ctx,
        )

    async def on_enter(self) -> None:
        await self.session.generate_reply(
            instructions="Ask for the new shipping address."
        )

    @function_tool()
    async def address_confirmed(self, address: str) -> None:
        """Call once the customer has confirmed their new address."""
        self.complete(AddressUpdateResult(address=address))


class CustomerServiceAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are a customer service representative. Greet the caller "
                "and ask how you can help. Route their request:\n"
                "- For questions about order status, call lookup_order.\n"
                "- For shipping address changes, call update_address.\n"
                "After a tool returns, summarize the outcome and ask whether "
                "the caller needs anything else."
            ),
        )

    # Routing tool called by the supervisor's LLM to delegate to
    # the specialist task. The tool body instantiates and awaits the task,
    # then returns its result string back to the LLM, which uses it to
    # continue the conversation.
    @function_tool()
    async def lookup_order(self) -> str:
        """Use when the customer wants to check the status of an order."""
        result = await LookupOrderTask(
            chat_ctx=self.chat_ctx.copy(exclude_instructions=True),
        )
        return f"Order {result.order_id} is {result.status}."

    @function_tool()
    async def update_address(self) -> str:
        """Use when the customer wants to change their shipping address."""
        result = await UpdateAddressTask(
            chat_ctx=self.chat_ctx.copy(exclude_instructions=True),
        )
        return f"Updated shipping address to: {result.address}."

```

---

**Node.js**:

```tsx
import { llm, voice } from '@livekit/agents';
import { z } from 'zod';

// Typed result returned when LookupOrderTask completes.
interface OrderLookupResult {
  orderId: string;
  status: string;
}

// Typed result returned when UpdateAddressTask completes.
interface AddressUpdateResult {
  address: string;
}

// The generic parameter ties this task to the type it returns.
function createLookupOrderTask(chatCtx?: llm.ChatContext) {
  const task = voice.AgentTask.create<OrderLookupResult>({
    instructions:
      "Ask the customer for their order number. If they don't have one, " +
      'ask them to check their email.',
    chatCtx,
    tools: [
      // Task-internal tool. The task's LLM calls this when the user
      // provides an order number. Calling task.complete(...) ends the
      // task and returns the typed result to the supervisor.
      llm.tool({
        name: 'orderNumberCollected',
        description: 'Call when the customer has provided their order number.',
        parameters: z.object({
          orderId: z.string().describe('The order number'),
        }),
        execute: async ({ orderId }) => {
          task.complete({ orderId, status: 'shipped' });
        },
      }),
    ],
    onEnter(ctx) {
      ctx.session.generateReply({
        instructions: 'Ask for the order number.',
      });
    },
  });

  return task;
}

function createUpdateAddressTask(chatCtx?: llm.ChatContext) {
  const task = voice.AgentTask.create<AddressUpdateResult>({
    instructions:
      "Collect the customer's new shipping address: street, city, state, " +
      'and zip code. Read it back to confirm before completing.',
    chatCtx,
    tools: [
      llm.tool({
        name: 'addressConfirmed',
        description: 'Call once the customer has confirmed their new address.',
        parameters: z.object({
          address: z.string().describe('The full shipping address'),
        }),
        execute: async ({ address }) => {
          task.complete({ address });
        },
      }),
    ],
    onEnter(ctx) {
      ctx.session.generateReply({
        instructions: 'Ask for the new shipping address.',
      });
    },
  });

  return task;
}

const customerServiceAgent = voice.Agent.create({
  instructions:
    'You are a customer service representative. Greet the caller and ' +
    'ask how you can help. Route their request:\n' +
    '- For questions about order status, call lookupOrder.\n' +
    '- For shipping address changes, call updateAddress.\n' +
    'After a tool returns, summarize the outcome and ask whether the ' +
    'caller needs anything else.',
  tools: [
    // Routing tool called by the supervisor's LLM to delegate to
    // the specialist task. The tool body instantiates and awaits the task,
    // then returns its result string back to the LLM, which uses it to
    // continue the conversation.
    llm.tool({
      name: 'lookupOrder',
      description: 'Use when the customer wants to check the status of an order.',
      execute: async (_, { ctx }) => {
        const result = await createLookupOrderTask(
          ctx.session.currentAgent.chatCtx.copy({ excludeInstructions: true }),
        ).run();
        return `Order ${result.orderId} is ${result.status}.`;
      },
    }),
    llm.tool({
      name: 'updateAddress',
      description: 'Use when the customer wants to change their shipping address.',
      execute: async (_, { ctx }) => {
        const result = await createUpdateAddressTask(
          ctx.session.currentAgent.chatCtx.copy({ excludeInstructions: true }),
        ).run();
        return `Updated shipping address to: ${result.address}.`;
      },
    }),
  ],
});

```

The supervisor's instructions name each specialist and describe when to invoke it; the LLM uses those descriptions to route incoming requests. Each task starts when its tool is called, takes over the session until it calls `complete(...)`, and returns its typed result to the supervisor for the rest of the conversation.

To pass the supervisor's [chat context](https://docs.livekit.io/agents/logic/chat-context.md) into a task so the specialist sees what came before, see [Passing conversation history to a task](https://docs.livekit.io/agents/logic/tasks.md#passing-context).

## Best practices

- **Keep specialist tasks focused.** One objective per task with a clear typed result. Split tasks that grow in scope.
- **Describe routing precisely in supervisor instructions.** The model relies on tool descriptions and instructions to route correctly. Ambiguity leads to misrouting.
- **Validate task results before continuing.** Typed results still require value-level validation (for example, empty or malformed fields).
- **Pass conversation context only when needed.** If a task doesn't require history, omitting it improves performance and reduces noise. See [Passing conversation history to a task](https://docs.livekit.io/agents/logic/tasks.md#passing-context).
- **Test the supervisor and each task independently.** Each task is a self-contained unit with a typed contract, so you can validate them on their own. To test the supervisor as a whole, drive it with representative user inputs and assert that it routes to the correct task or tool and handles the result. See [Test framework](https://docs.livekit.io/agents/start/testing/test-framework.md).
- **Validate the assembled flow with a simulation.** After you confirm the individual pieces work, run an [agent simulation](https://docs.livekit.io/agents/start/testing/simulations.md) to validate the end-to-end conversation.

## Additional resources

The following resources provide more information on the topics discussed in this guide.

- **[Workflows](https://docs.livekit.io/agents/logic/workflows.md)**: Model multi-step voice AI apps with agents, handoffs, and tasks.

- **[Tasks & task groups](https://docs.livekit.io/agents/logic/tasks.md)**: Define short-lived units of work that return typed results.

- **[Agents and handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md)**: Transfer long-lived control between agents with different instructions or tools.

- **[Tool definition and use](https://docs.livekit.io/agents/logic/tools.md)**: Define model-callable functions for external actions or to trigger delegation.

- **[Testing & evaluation](https://docs.livekit.io/agents/start/testing.md)**: Test the supervisor and each task independently.

---

This document was rendered at 2026-08-28T04:22:11.909Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/supervisor-pattern.md](https://docs.livekit.io/agents/logic/supervisor-pattern.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-8"></a>
## Page 8: agents/logic/tools/
**Original URL:** https://docs.livekit.io/agents/logic/tools/  
**Source MD URL:** https://docs.livekit.io/agents/logic/tools.md

LiveKit docs › Build Agents › Logic & Structure › Tool definition & use › Overview

---

# Tool definition and use

> Let your agents call external tools and more.

## Overview

LiveKit Agents has full support for LLM tool use. This feature allows you to create a custom library of tools to extend your agent's context, create interactive experiences, and overcome LLM limitations. Tools can run synchronously or [in the background](https://docs.livekit.io/agents/logic/tools/async.md), letting the agent keep talking while long-running work completes.

Within a tool, you can:

- Generate [agent speech](https://docs.livekit.io/agents/build/audio.md) with `session.say()` or `session.generate_reply()`.
- Call methods on the frontend using [RPC](https://docs.livekit.io/transport/data/rpc.md).
- Handoff control to another agent as part of a [workflow](https://docs.livekit.io/agents/logic/workflows.md).
- Store and retrieve session data from the `context`.
- Anything else that a Python function can do.
- [Call external APIs or lookup data for RAG](https://docs.livekit.io/agents/build/external-data.md).

### Tool types

Two types of tools are supported:

- **Function tools**: Tools that are defined as functions within your agent's code base and can be called by the LLM.
- **Provider tools**: Tools provided by a specific model provider (e.g. OpenAI, Gemini, etc.) and are executed internally by the provider's model server.

### Provider tools

Available in:
- [x] Node.js
- [x] Python

Many LLM providers, including OpenAI, Gemini, and SpaceXAI, include built-in server-side tools that are executed entirely within a single API call. Examples include web search, code execution, and file search. These tools, called "provider tools" in LiveKit Agents, can be added to any agent that uses a supported LLM. Where the underlying provider supports it, you can mix provider tools with function tools by passing them to the `tools` parameter on your `Agent`.

Node.js provider tools are currently available for OpenAI and Gemini.

**Python**:

```python
from livekit.plugins import openai  # replace with any supported provider

agent = MyAgent(
    llm=openai.responses.LLM(model="gpt-4.1"),
    tools=[openai.tools.WebSearch()],  # replace with any supported tool
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import * as openai from '@livekit/agents-plugin-openai';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  llm: new openai.responses.LLM({ model: 'gpt-4.1' }),
  tools: [new openai.WebSearch()],
});

```

Refer to the documentation for each model provider for usage details.

| Provider | Supported tools |
| [Anthropic](https://docs.livekit.io/agents/models/llm/anthropic.md#provider-tools) | `ComputerUse` |
| [Gemini](https://docs.livekit.io/agents/models/llm/gemini.md#provider-tools) | `GoogleSearch`, `GoogleMaps`, `URLContext`, `FileSearch`, `ToolCodeExecution` |
| [Mistral AI](https://docs.livekit.io/agents/models/llm/mistralai.md#provider-tools) | `WebSearch`, `DocumentLibrary`, `CodeInterpreter` |
| [OpenAI](https://docs.livekit.io/agents/models/llm/openai.md#provider-tools) | `WebSearch`, `FileSearch`, `CodeInterpreter` |
| [SpaceXAI](https://docs.livekit.io/agents/models/llm/spacexai.md#provider-tools) | `WebSearch`, `XSearch`, `FileSearch` |

### Examples

The following additional examples show how to use tools in different ways:

- **[Dynamic tool creation](https://docs.livekit.io/agents/logic/tools/definition.md#adding-tools-dynamically)**: Set the tools list directly and share tools between agents.

- **[MCP Agent](https://docs.livekit.io/reference/recipes/http_mcp_client.md)**: A voice AI agent with an integrated Model Context Protocol (MCP) client for the LiveKit API.

## In this section

Read more about each topic.

| Topic | Description |
| [Function tools](https://docs.livekit.io/agents/logic/tools/definition.md) | Define function tools with decorators, RunContext, speech in tools, interruptions, dynamic tools, and error handling. |
| [Toolsets](https://docs.livekit.io/agents/logic/tools/toolsets.md) | Group related tools and add or remove them as a unit. |
| [Async tools](https://docs.livekit.io/agents/logic/tools/async.md) | Run long-running tools in the background so the agent can keep talking. |
| [Model Context Protocol (MCP)](https://docs.livekit.io/agents/logic/tools/mcp.md) | Expose tools from MCP servers to your agent (Python only). |
| [Forwarding to the frontend](https://docs.livekit.io/agents/logic/tools/forwarding.md) | Fulfill tool calls via RPC from the client. |

## Additional resources

The following articles provide more information about the topics discussed in this guide:

- **[RPC](https://docs.livekit.io/transport/data/rpc.md)**: Complete documentation on function calling between LiveKit participants.

- **[Agent speech](https://docs.livekit.io/agents/build/audio.md)**: More information about precise control over agent speech output.

- **[Workflows](https://docs.livekit.io/agents/logic/workflows.md)**: Read more about handing off control to other agents.

- **[External data and RAG](https://docs.livekit.io/agents/build/external-data.md)**: Best practices for adding context and taking external actions.

---

This document was rendered at 2026-08-28T04:22:11.915Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/tools.md](https://docs.livekit.io/agents/logic/tools.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-9"></a>
## Page 9: agents/logic/nodes/
**Original URL:** https://docs.livekit.io/agents/logic/nodes/  
**Source MD URL:** https://docs.livekit.io/agents/logic/nodes.md

LiveKit docs › Build Agents › Logic & Structure › Pipeline nodes & hooks

---

# Pipeline nodes and hooks

> Learn how to customize the behavior of your agent with nodes and hooks in the voice pipeline.

## Overview

You can fully customize your agent's behavior at multiple **nodes** in the processing path. A node is a point in the path where one process transitions to another. Some example customizations include:

- Use a custom STT, LLM, or TTS provider without a plugin.
- Generate a custom greeting when an agent enters a session.
- Modify STT output to remove filler words before sending it to the LLM.
- Modify LLM output before sending it to TTS to customize pronunciation.
- Update the user interface when an agent or user finishes speaking.

The `Agent` supports the following nodes and hooks. Some nodes are only available for STT-LLM-TTS pipeline models, and others are only available for realtime models.

Lifecycle hooks:

- `on_enter()`: Called after the agent becomes the active agent in a session.
- `on_exit()`: Called before the agent gives control to another agent in the same session.
- `on_user_turn_completed()`: Called when the user's [turn](https://docs.livekit.io/agents/logic/turns.md) has ended, before the agent's reply.
- `on_user_turn_exceeded()`: Called when the user has been speaking long enough to exceed a configured [user turn limit](https://docs.livekit.io/agents/logic/turns.md#user-turn-limit).

STT-LLM-TTS pipeline nodes:

- `stt_node()`: Transcribe input audio to text.
- `llm_node()`: Perform inference and generate a new conversation turn (or tool call).
- `tts_node()`: Synthesize speech from the LLM text output.

Realtime model nodes:

- `realtime_audio_output_node()`: Adjust output audio before publishing to the user.

Transcription node:

- `transcription_node()`: Access transcription timestamps, or adjust pipeline or realtime model transcription before sending to the user.

The following diagrams show the processing path for STT-LLM-TTS pipeline models and realtime models.

**STT-LLM-TTS pipeline**:

![Diagram showing voice pipeline agent processing path.](/images/agents/voice-pipeline-agent.svg)

---

**Realtime model**:

![Diagram showing realtime agent processing path.](/images/agents/realtime-agent.svg)

## How to implement

Override the method within a custom `Agent` subclass, or pass hooks to `Agent.create`, to customize the behavior of your agent at a specific node in the processing path. `Agent.create` hooks receive a `ctx` object first and use `AsyncIterable` inputs and outputs for stream nodes. To use the default implementation, call `Agent.default.<node-name>()`. For instance, this code overrides the STT node while maintaining the default behavior.

**Python**:

```python
async def stt_node(self, audio: AsyncIterable[rtc.AudioFrame], model_settings: ModelSettings) -> Optional[AsyncIterable[stt.SpeechEvent]]:
    # insert custom before STT processing here
    events = Agent.default.stt_node(self, audio, model_settings)
    # insert custom after STT processing here
    return events

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  sttNode(ctx, audio, modelSettings) {
    // insert custom before STT processing here
    const events = voice.Agent.default.sttNode(ctx.agent, audio, modelSettings);
    // insert custom after STT processing here
    return events;
  },
});

```

## Lifecycle hooks

The following lifecycle hooks are available for customization.

### On enter

The `on_enter` node is called when the agent becomes the active agent in a session. Each session can have only one active agent at a time, which can be read from the `session.agent` property. Change the active agent using [Workflows](https://docs.livekit.io/agents/logic/workflows.md).

For example, to greet the user:

**Python**:

```python
async def on_enter(self):
    await self.session.generate_reply(
        instructions="Greet the user with a warm welcome",
    )

```

---

**Node.js**:

```typescript
const agent = voice.Agent.create({
  onEnter(ctx) {
    ctx.session.generateReply({
      instructions: "Greet the user with a warm welcome",
    });
  },
});

```

### On exit

The `on_exit` node is called before the agent gives control to another agent in the same session as part of a [workflow](https://docs.livekit.io/agents/logic/workflows.md). Use it to save data, say goodbye, or perform other actions and cleanup.

For example, to say goodbye:

**Python**:

```python
async def on_exit(self):
    await self.session.generate_reply(
        instructions="Tell the user a friendly goodbye before you exit.",
    )

```

---

**Node.js**:

```typescript
const agent = voice.Agent.create({
  onExit(ctx) {
    ctx.session.generateReply({
      instructions: "Tell the user a friendly goodbye before you exit.",
    });
  },
});

```

### On user turn completed

The `on_user_turn_completed` node is called when the user's [turn](https://docs.livekit.io/agents/logic/turns.md) has ended, before the agent's reply. Override this method to modify the content of the turn, cancel the agent's reply, or perform other actions.

> ℹ️ **Realtime model turn detection**
> 
> To use the `on_user_turn_completed` node with a [realtime model](https://docs.livekit.io/agents/models/realtime.md), you must configure [turn detection](https://docs.livekit.io/agents/logic/turns.md) to occur in your agent instead of within the realtime model.

The node receives the following parameters:

- `turn_ctx`: The full [`ChatContext`](https://docs.livekit.io/agents/logic/chat-context.md), up to but not including the user's latest message.
- `new_message`: The user's latest message, representing their current turn.

After the node is complete, the `new_message` is added to the chat context.

One common use of this node is [retrieval-augmented generation (RAG)](https://docs.livekit.io/agents/build/external-data.md). You can retrieve context relevant to the newest message and inject it into the chat context for the LLM.

**Python**:

```python
from livekit.agents import ChatContext, ChatMessage

async def on_user_turn_completed(
    self, turn_ctx: ChatContext, new_message: ChatMessage,
) -> None:
    rag_content = await my_rag_lookup(new_message.text_content)
    turn_ctx.add_message(
        role="assistant",
        content=f"Additional information relevant to the user's next message: {rag_content}"
    )

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async onUserTurnCompleted(ctx, chatCtx, newMessage) {
    const ragContent = await myRagLookup(newMessage.textContent);
    chatCtx.addMessage({
      role: 'assistant',
      content: `Additional information relevant to the user's next message: ${ragContent}`,
    });
  },
});

```

Additional messages added in this way are not persisted beyond the current turn. To permanently add messages to the chat history, use the `update_chat_ctx` method:

**Python**:

```python
async def on_user_turn_completed(
    self, turn_ctx: ChatContext, new_message: ChatMessage,
) -> None:
    rag_content = await my_rag_lookup(new_message.text_content)
    turn_ctx.add_message(role="assistant", content=rag_content)
    await self.update_chat_ctx(turn_ctx)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async onUserTurnCompleted(ctx, chatCtx, newMessage) {
    const ragContent = await myRagLookup(newMessage.textContent);
    chatCtx.addMessage({
      role: 'assistant',
      content: `Additional information relevant to the user's next message: ${ragContent}`,
    });
    await ctx.agent.updateChatCtx(chatCtx);
  },
});

```

You can also edit the `new_message` object to modify the user's message before it's added to the chat context. For example, you can remove offensive content or add additional context. These changes are persisted to the chat history going forward.

**Python**:

```python
async def on_user_turn_completed(
    self, turn_ctx: ChatContext, new_message: ChatMessage,
) -> None:
    new_message.content = ["... modified message ..."]

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  onUserTurnCompleted(ctx, chatCtx, newMessage) {
    newMessage.content = ['... modified message ...'];
  },
});

```

To abort generation entirely — for example, in a push-to-talk interface — you can do the following:

**Python**:

```python
async def on_user_turn_completed(
    self, turn_ctx: ChatContext, new_message: ChatMessage,
) -> None:
    if not new_message.text_content:
        # for example, raise StopResponse to stop the agent from generating a reply
        raise StopResponse()

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  onUserTurnCompleted(ctx, chatCtx, newMessage) {
    if (!newMessage.textContent) {
      // raise StopResponse to stop the agent from generating a reply
      throw new voice.StopResponse();
    }
  },
});

```

#### Fast pre-response

Use the `on_user_turn_completed` node to speak a short filler phrase, such as "let me think about that", while the main reply is still generating. A smaller, faster model produces the filler. Calling `say` without awaiting the speech handle it returns lets the two run concurrently, which reduces the perceived gap between the user's turn and the agent's response.

To implement this, override `on_user_turn_completed` to build a trimmed context for the fast model, then call `say` with `add_to_chat_ctx=False` so the filler stays out of the main reply's history:

**Python**:

```python
from livekit.agents import Agent, ChatContext, ChatMessage, inference, llm

class PreResponseAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a helpful assistant.",
            llm=inference.LLM("openai/gpt-4.1-mini"),
        )
        # A smaller, faster model generates the filler phrase
        self._fast_llm = inference.LLM("openai/gpt-5.4-nano")
        self._fast_llm_prompt = llm.ChatMessage(
            role="system",
            content=[
                "Generate a short instant response to the user's message with 5 to 10 words.",
                "Do not answer the question directly. Examples: let me think about that, "
                "wait a moment, that's a good question.",
            ],
        )

    async def on_user_turn_completed(
        self, turn_ctx: ChatContext, new_message: ChatMessage,
    ) -> None:
        # Trim the context: drop instructions and tool-call history, keep only recent items
        fast_ctx = turn_ctx.copy(
            exclude_instructions=True,
            exclude_function_call=True,
        ).truncate(max_items=3)
        fast_ctx.items.insert(0, self._fast_llm_prompt)
        fast_ctx.items.append(new_message)

        # Speak the filler without awaiting, so the main reply generates concurrently
        self.session.say(
            self._fast_llm.chat(chat_ctx=fast_ctx).to_str_iterable(),
            add_to_chat_ctx=False,
        )

```

---

**Node.js**:

```typescript
import { inference, llm, toStream, voice } from '@livekit/agents';

const FAST_LLM_PROMPT =
  "Generate a short instant response to the user's message with 5 to 10 words. " +
  'Do not answer the question directly. Examples: let me think about that, ' +
  "wait a moment, that's a good question.";

// A smaller, faster model generates the filler phrase
const fastLLM = new inference.LLM({ model: 'openai/gpt-5.4-nano' });

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  llm: new inference.LLM({ model: 'openai/gpt-4.1-mini' }),
  onUserTurnCompleted(ctx, turnCtx, newMessage) {
    // Trim the context: drop instructions and tool-call history, keep only recent items
    const fastCtx = turnCtx
      .copy({ excludeInstructions: true, excludeFunctionCall: true })
      .truncate(3);
    fastCtx.items.unshift(llm.ChatMessage.create({ role: 'system', content: FAST_LLM_PROMPT }));
    fastCtx.items.push(newMessage);

    // Stream the filler text from the fast model
    async function* fillerText() {
      for await (const chunk of fastLLM.chat({ chatCtx: fastCtx })) {
        if (chunk.delta?.content) yield chunk.delta.content;
      }
    }

    // Speak the filler without awaiting, so the main reply generates concurrently
    // say() takes a ReadableStream, so wrap the async generator with toStream()
    ctx.session.say(toStream(fillerText()), { addToChatCtx: false });
  },
});

```

### On user turn exceeded

The `on_user_turn_exceeded` node is called when the user has been speaking long enough to trip a configured [user turn limit](https://docs.livekit.io/agents/logic/turns.md#user-turn-limit). The node lets the agent step in when a caller keeps talking past the configured `max_words` or `max_duration` threshold. The node is only invoked when at least one threshold is set in `turn_handling.user_turn_limit`.

The node receives a `UserTurnExceededEvent` with the following fields:

- `transcript`: Transcript from the current uncommitted user turn. Previous turns in the accumulation window are already in the chat context.
- `accumulated_transcript`: Full transcript since the user started speaking in the current accumulation window. In Node.js, this field is `accumulatedTranscript`.
- `accumulated_word_count`: Total word count across the accumulation window. In Node.js, this field is `accumulatedWordCount`.
- `duration`: Wall-clock duration of the accumulation window. Python uses seconds and Node.js uses milliseconds.

The default implementation calls `session.generate_reply` with `allow_interruptions=False` and `tool_choice="none"` to respond with a short reply. The user cannot interrupt the default reply.

Override the node to customize the behavior. For example, to deliver a prewritten response with `say` instead of generating a new reply:

**Python**:

```python
from livekit.agents import Agent, UserTurnExceededEvent

class MyAgent(Agent):
    async def on_user_turn_exceeded(self, ev: UserTurnExceededEvent) -> None:
        await self.session.say("Sorry to jump in. Can I help with anything specific?")

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

class MyAgent extends voice.Agent {
  async onUserTurnExceeded(ev: voice.UserTurnExceededEvent): Promise<void> {
    await this.session.say('Sorry to jump in. Can I help with anything specific?');
  }
}

```

The framework skips the `on_user_turn_exceeded` callback if the agent enters the `speaking` state before the threshold fires. This happens when the user pauses long enough for end-of-utterance detection to end their turn naturally and the agent's normal reply starts playing.

## STT-LLM-TTS pipeline nodes

The following nodes are available for STT-LLM-TTS pipeline models.

### STT node

The `stt_node` transcribes audio frames into speech events, converting user audio input into text for the LLM. By default, this node uses the Speech-To-Text (STT) capability from the current agent. If the STT implementation doesn't support streaming natively, a Voice Activity Detection (VAD) mechanism wraps the STT.

You can override this node to implement:

- Custom pre-processing of audio frames
- Additional buffering mechanisms
- Alternative STT strategies
- Post-processing of the transcribed text

To use the default implementation, call `Agent.default.stt_node()`.

This example adds a noise filtering step:

**Python**:

```python
from livekit import rtc
from livekit.agents import ModelSettings, stt, Agent
from typing import AsyncIterable, Optional

async def stt_node(
    self, audio: AsyncIterable[rtc.AudioFrame], model_settings: ModelSettings
) -> Optional[AsyncIterable[stt.SpeechEvent]]:
    async def filtered_audio():
        async for frame in audio:
            # insert custom audio preprocessing here
            yield frame

    async for event in Agent.default.stt_node(self, filtered_audio(), model_settings):
        # insert custom text postprocessing here
        yield event

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async *sttNode(ctx, audio, modelSettings) {
    // Create a transformed audio stream
    async function* filteredAudio() {
      for await (const frame of audio) {
        // insert custom audio preprocessing here
        yield frame;
      }
    }

    const events = await voice.Agent.default.sttNode(
      ctx.agent,
      filteredAudio(),
      modelSettings,
    );
    if (!events) return;

    for await (const event of events) {
      // insert custom text postprocessing here
      yield event;
    }
  },
});

```

### LLM node

The `llm_node` is responsible for performing inference based on the current chat context and creating the agent's response or tool calls. It may yield plain text (as `str`) for straightforward text generation, or `llm.ChatChunk` objects that can include text and optional tool calls. `ChatChunk` is helpful for capturing more complex outputs such as function calls, usage statistics, or other metadata.

You can override this node to:

- Customize how the LLM is used
- Modify the chat context prior to inference
- Adjust how tool invocations and responses are handled
- Implement a custom LLM provider without a plugin

To use the default implementation, call `Agent.default.llm_node()`.

**Python**:

```python
from livekit.agents import ModelSettings, llm, FunctionTool, Agent
from typing import AsyncIterable

async def llm_node(
    self,
    chat_ctx: llm.ChatContext,
    tools: list[FunctionTool],
    model_settings: ModelSettings
) -> AsyncIterable[llm.ChatChunk]:
    # Insert custom preprocessing here
    async for chunk in Agent.default.llm_node(self, chat_ctx, tools, model_settings):
        # Insert custom postprocessing here
        yield chunk

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async *llmNode(ctx, chatCtx, toolCtx, modelSettings) {
    // Insert custom preprocessing here
    const stream = await voice.Agent.default.llmNode(
      ctx.agent,
      chatCtx,
      toolCtx,
      modelSettings,
    );
    if (!stream) return;

    for await (const chunk of stream) {
      // Insert custom postprocessing here
      yield chunk;
    }
  },
});

```

#### Send an early response to TTS

By default, the agent waits for the LLM node to finish before sending its output to the TTS node. Sometimes you want to flush part of a response to TTS right away — for example, a filler phrase like "One moment" while a slow tool call completes in the background.

To do this, emit a `FlushSentinel` from your LLM node. `FlushSentinel` is a marker that acts as a segment boundary. In Python it's a class you instantiate (`FlushSentinel()`); in Node.js it's a symbol you yield directly (`FlushSentinel`). When the pipeline encounters one in the stream, it immediately sends all text produced so far to the TTS node for synthesis without waiting for the node to finish. Any text produced after the sentinel begins a new speech segment.

> ℹ️ **Each segment plays out independently**
> 
> A `FlushSentinel` creates a hard playout boundary. Each section of the reply is synthesized in a separate TTS pass, played as a separate audio segment, and emitted as a separate transcript segment. Segments are synthesized sequentially, with the next segment starting while the previous one is still playing. Without a `FlushSentinel`, the entire reply is a single segment.

In this example, the LLM node checks whether the model responded with only a `get_weather` tool call and no accompanying text. Without the filler, the user would hear silence until the tool finishes. The flush sends a spoken acknowledgment to TTS immediately while the tool result is still being processed:

**Python**:

```python
import asyncio
from collections.abc import AsyncIterable

from livekit.agents import Agent, FlushSentinel, ModelSettings, llm

async def llm_node(
    self,
    chat_ctx: llm.ChatContext,
    tools: list[llm.FunctionTool],
    model_settings: ModelSettings,
) -> AsyncIterable[llm.ChatChunk | FlushSentinel]:
    called_tools: list[llm.FunctionToolCall] = []
    has_text_message = False
    async for chunk in Agent.default.llm_node(self, chat_ctx, tools, model_settings):
        if isinstance(chunk, llm.ChatChunk) and chunk.delta:
            if chunk.delta.content:
                has_text_message = True
            if chunk.delta.tool_calls:
                called_tools.extend(chunk.delta.tool_calls)
        yield chunk

    # If the model only called get_weather (with no text of its own), speak a
    # filler phrase right away instead of waiting for the tool result.
    tool_names = [tool.name for tool in called_tools]
    if not has_text_message and "get_weather" in tool_names:
        yield "One moment while I look that up. "
        # Send the filler phrase to TTS immediately, ending the current
        # segment and starting a new one.
        yield FlushSentinel()

        # Simulate additional processing, then speak the rest.
        await asyncio.sleep(3)
        yield "Okay, I found what you were looking for. "

```

---

**Node.js**:

```typescript
import { FlushSentinel, delay, voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async *llmNode(ctx, chatCtx, toolCtx, modelSettings) {
    const stream = await voice.Agent.default.llmNode(ctx.agent, chatCtx, toolCtx, modelSettings);
    if (!stream) return;

    const calledTools: string[] = [];
    let hasTextMessage = false;
    for await (const chunk of stream) {
      if (typeof chunk !== 'string' && chunk !== FlushSentinel && chunk.delta) {
        if (chunk.delta.content) hasTextMessage = true;
        if (chunk.delta.toolCalls) {
          calledTools.push(...chunk.delta.toolCalls.map((toolCall) => toolCall.name));
        }
      }
      yield chunk;
    }

    // If the model only called getWeather (with no text of its own), speak a
    // filler phrase right away instead of waiting for the tool result.
    if (!hasTextMessage && calledTools.includes('getWeather')) {
      yield 'One moment while I look that up. ';
      // Send the filler phrase to TTS immediately, ending the current
      // segment and starting a new one.
      yield FlushSentinel;

      // Simulate additional processing, then speak the rest.
      await delay(3000);
      yield 'Okay, I found what you were looking for. ';
    }
  },
});

```

Although the reply plays out as separate segments, the agent records it as a single assistant message in the conversation history. Interruptions are handled per segment: if the user interrupts, segments that already finished playing are kept, and the segment in progress is truncated at the point of interruption. The whole reply remains one `SpeechHandle`, so the `speech_created` event fires once regardless of how many segments the reply contains.

> 🔀 **Behavior change: Flushed replies**
> 
> Per-segment playout was introduced in `livekit-agents` 1.6.0 (Python) and `@livekit/agents` 1.4.6 (Node.js). In earlier versions, a flushed reply played as one continuous audio stream with a single transcript segment.

### TTS node

The `tts_node` synthesizes audio from text segments, converting the LLM output into speech. By default, this node uses the Text-To-Speech capability from the agent. If the TTS implementation doesn't support streaming natively, it uses a sentence tokenizer to split text for incremental synthesis.

You can override this node to:

- Provide different text chunking behavior
- Implement a custom TTS engine
- [Add custom pronunciation rules](https://docs.livekit.io/agents/multimodality/audio/customization.md#pronunciation)
- [Adjust the volume of the audio output](https://docs.livekit.io/agents/multimodality/audio/customization.md#volume)
- Apply any other specialized audio processing

To use the default implementation, call `Agent.default.tts_node()`.

**Python**:

```python
from livekit import rtc
from livekit.agents import ModelSettings, Agent
from typing import AsyncIterable

async def tts_node(
    self, text: AsyncIterable[str], model_settings: ModelSettings
) -> AsyncIterable[rtc.AudioFrame]:
    # Insert custom text processing here
    async for frame in Agent.default.tts_node(self, text, model_settings):
        # Insert custom audio processing here
        yield frame

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import type { AudioFrame } from '@livekit/rtc-node';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async *ttsNode(ctx, text, modelSettings) {
    const audioStream = await voice.Agent.default.ttsNode(
      ctx.agent,
      text,
      modelSettings,
    );
    if (!audioStream) return;

    for await (const frame of audioStream) {
      // Insert custom audio processing here
      yield frame;
    }
  },
});

```

#### Speeding up output audio

You can modify the agent's output audio before its playout by adding a processor to the `tts_node`. For example, you can speed up the agent's speech by time-stretching the audio without changing its pitch. The same processor also works for the realtime audio output node when using a realtime model.

The following example time stretches the audio by a configurable speed factor. A speed factor greater than `1.0` speeds up the speech, while a value less than `1.0` slows it down.

**Python**:

> ℹ️ **Install librosa**
> 
> This example uses [`librosa`](https://librosa.org/) for time stretching. Install it with `pip install librosa`.

The frames are buffered into 100 ms chunks with `AudioByteStream` before processing:

```python
from collections.abc import AsyncIterable

import librosa
import numpy as np

from livekit import rtc
from livekit.agents import Agent, ModelSettings, utils


class MyAgent(Agent):
    def __init__(self, *, speed_factor: float = 1.2) -> None:
        super().__init__(
            instructions="You are a helpful voice AI assistant.",
        )
        self.speed_factor = speed_factor

    async def tts_node(self, text: AsyncIterable[str], model_settings: ModelSettings):
        return self._process_audio_stream(
            Agent.default.tts_node(self, text, model_settings)
        )

    async def realtime_audio_output_node(
        self, audio: AsyncIterable[rtc.AudioFrame], model_settings: ModelSettings
    ) -> AsyncIterable[rtc.AudioFrame]:
        return self._process_audio_stream(
            Agent.default.realtime_audio_output_node(self, audio, model_settings)
        )

    async def _process_audio_stream(
        self, audio: AsyncIterable[rtc.AudioFrame]
    ) -> AsyncIterable[rtc.AudioFrame]:
        stream: utils.audio.AudioByteStream | None = None
        async for frame in audio:
            if stream is None:
                stream = utils.audio.AudioByteStream(
                    sample_rate=frame.sample_rate,
                    num_channels=frame.num_channels,
                    samples_per_channel=frame.sample_rate // 10,  # 100ms
                )
            for f in stream.push(frame.data):
                yield self._process_audio(f)

        for f in stream.flush():
            yield self._process_audio(f)

    def _process_audio(self, frame: rtc.AudioFrame) -> rtc.AudioFrame:
        # time-stretch without pitch change
        audio_data = np.frombuffer(frame.data, dtype=np.int16)
        stretched = librosa.effects.time_stretch(
            audio_data.astype(np.float32) / np.iinfo(np.int16).max,
            rate=self.speed_factor,
        )
        stretched = (stretched * np.iinfo(np.int16).max).astype(np.int16)
        return rtc.AudioFrame(
            data=stretched.tobytes(),
            sample_rate=frame.sample_rate,
            num_channels=frame.num_channels,
            samples_per_channel=stretched.shape[-1],
        )

```

---

**Node.js**:

> ℹ️ **Install soundtouchjs**
> 
> This example uses [`soundtouchjs`](https://www.npmjs.com/package/soundtouchjs) for time stretching. Install it with `pnpm add soundtouchjs`.

`SoundTouch` buffers audio internally and emits stretched frames as they become ready. It processes interleaved stereo floats, so each mono frame is converted to floats for processing and back to 16-bit PCM afterward:

```typescript
import { voice } from '@livekit/agents';
import { AudioFrame } from '@livekit/rtc-node';
import { SoundTouch } from 'soundtouchjs';

function createAgent(speedFactor = 1.2) {
  async function* processAudioStream(source: AsyncIterable<AudioFrame>): AsyncIterable<AudioFrame> {
    const soundTouch = new SoundTouch();
    soundTouch.tempo = speedFactor;
    let sampleRate = 24000;
    let channels = 1;

    // pull every stretched frame SoundTouch has buffered so far
    function* drain() {
      const output = soundTouch.outputBuffer;
      while (output.frameCount > 0) {
        const frames = output.frameCount;
        const interleaved = new Float32Array(frames * 2);
        output.receiveSamples(interleaved, frames);

        const data = new Int16Array(frames);
        for (let f = 0; f < frames; f++) {
          const sample = Math.max(-1, Math.min(1, interleaved[f * 2]));
          data[f] = Math.round(sample * 0x7fff);
        }
        yield new AudioFrame(data, sampleRate, channels, frames);
      }
    }

    for await (const frame of source) {
      sampleRate = frame.sampleRate;
      channels = frame.channels;

      // duplicate the mono channel into interleaved stereo floats
      const samples = frame.samplesPerChannel;
      const stereo = new Float32Array(samples * 2);
      for (let f = 0; f < samples; f++) {
        const sample = frame.data[f] / 0x8000;
        stereo[f * 2] = sample;
        stereo[f * 2 + 1] = sample;
      }

      soundTouch.inputBuffer.putSamples(stereo, 0, samples);
      soundTouch.process();
      yield* drain();
    }

    soundTouch.process();
    yield* drain();
  }

  return voice.Agent.create({
    instructions: 'You are a helpful voice AI assistant.',
    async ttsNode(ctx, text, modelSettings) {
      const source = await voice.Agent.default.ttsNode(ctx.agent, text, modelSettings);
      return source ? processAudioStream(source) : null;
    },
    async realtimeAudioOutputNode(ctx, audio, modelSettings) {
      const source = await voice.Agent.default.realtimeAudioOutputNode(
        ctx.agent,
        audio,
        modelSettings,
      );
      return source ? processAudioStream(source) : null;
    },
  });
}

```

## Realtime model nodes

The following nodes are available for realtime models.

### Realtime audio output node

The `realtime_audio_output_node` is called when a realtime model outputs speech. This allows you to modify the audio output before it's sent to the user. For example, you can [adjust the volume of the audio output](https://docs.livekit.io/agents/multimodality/audio/customization.md#volume).

To use the default implementation, call `Agent.default.realtime_audio_output_node()`.

**Python**:

```python
from livekit.agents import ModelSettings, rtc, Agent
from typing import AsyncIterable

async def realtime_audio_output_node(
    self, audio: AsyncIterable[rtc.AudioFrame], model_settings: ModelSettings
) -> AsyncIterable[rtc.AudioFrame]:
    # Insert custom audio preprocessing here
    async for frame in Agent.default.realtime_audio_output_node(self, audio, model_settings):
        # Insert custom audio postprocessing here
        yield frame

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async *realtimeAudioOutputNode(ctx, audio, modelSettings) {
    // Insert custom audio preprocessing here
    const outputStream = await voice.Agent.default.realtimeAudioOutputNode(
      ctx.agent,
      audio,
      modelSettings,
    );

    if (!outputStream) return;

    for await (const frame of outputStream) {
      // Insert custom audio postprocessing here
      yield frame;
    }
  },
});

```

## Transcription node

The `transcription_node` is part of the forwarding path for [agent transcriptions](https://docs.livekit.io/agents/build/text.md#transcriptions) and can be used to adjust or post-process text coming from an LLM (or any other source) into a final transcribed form. It may also be used to access [transcription timestamps](https://docs.livekit.io/agents/build/text.md#tts-aligned-transcriptions) for TTS-aligned transcriptions.

By default, the node simply passes the transcription to the task that forwards it to the designated output. You can override this node to:

- Clean up formatting
- Fix punctuation
- Strip unwanted characters
- Perform any other text transformations
- Access [transcription timestamps](https://docs.livekit.io/agents/build/text.md#tts-aligned-transcriptions) for TTS-aligned transcriptions

To use the default implementation, call `Agent.default.transcription_node()`.

**Python**:

```python
from livekit.agents import ModelSettings
from typing import AsyncIterable

async def transcription_node(self, text: AsyncIterable[str], model_settings: ModelSettings) -> AsyncIterable[str]:
    async for delta in text:
        yield delta.replace("😘", "")

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async *transcriptionNode(ctx, text, modelSettings) {
    for await (const chunk of text) {
      // chunk may be a plain string or a TimedString (for TTS-aligned transcriptions)
      yield typeof chunk === 'string' ? chunk.replace('😘', '') : chunk;
    }
  },
});

```

## Examples

The following examples demonstrate advanced usage of nodes and hooks:

- **[Restaurant Agent](https://docs.livekit.io/reference/recipes/restaurant-agent.md)**: A restaurant front-of-house agent demonstrates the `on_enter` and `on_exit` lifecycle hooks.

- **[LLM Output Replacement](https://docs.livekit.io/reference/recipes/replacing_llm_output.md)**: Remove chain-of-thought reasoning from the LLM stream so it doesn't reach TTS or chat history.

- **[Keyword Detection](https://github.com/livekit-examples/python-agents-examples/blob/main/docs/examples/keyword-detection/keyword_detection.py)**: Use the `stt_node` to detect keywords in the user's speech.

- **[LLM Content Filter](https://docs.livekit.io/reference/recipes/llm_powered_content_filter.md)**: Implement content filtering in the `llm_node`.

---

This document was rendered at 2026-08-28T04:22:11.942Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/nodes.md](https://docs.livekit.io/agents/logic/nodes.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-10"></a>
## Page 10: agents/logic/turns/
**Original URL:** https://docs.livekit.io/agents/logic/turns/  
**Source MD URL:** https://docs.livekit.io/agents/logic/turns.md

LiveKit docs › Build Agents › Logic & Structure › Turn detection & interruptions › Overview

---

# Turns overview

> Guide to managing conversation turns in voice AI.

## Overview

Turn detection is the process of determining when a user begins or ends their "turn" in a conversation. This lets the agent know when to start listening and when to respond.

Most turn detection techniques rely on voice activity detection (VAD) to detect periods of silence in user input. The agent applies heuristics to the VAD data to perform phrase endpointing, which determines the end of a sentence or thought. The agent can use endpoints alone or apply a model that understands the meaning of speech to determine when a turn is complete.

Effective turn detection and interruption management is essential to great voice AI experiences.

This page covers user-side detection and interruption handling. Turn-taking is also affected by features that live in other parts of the agent pipeline (preemptive generation, background voice cancellation, and agent-side speech scheduling) that don't fit cleanly into either category. For a recommended starting config that combines all of these, plus a troubleshooting matrix, see [Turn-taking tuning](https://docs.livekit.io/agents/logic/turns/tuning.md).

## Turn detection

Turn detection determines when the user has finished speaking (so the agent can respond) and when the user starts speaking mid-response (so the agent can yield).

LiveKit supports multiple detection strategies and optional features that work together to make turn-taking feel natural:

- **Detection modes**: Choose how the session determines when a user turn is complete. For most agents, use LiveKit's [turn detector model](#turn-detector-model). It's the default, and it handles the widest range of conversations. The other modes are for specific situations:

| Mode | When to use it |
| [Turn detector model](#turn-detector-model) | **Recommended for most agents, and the default.** Predicts end of turn from both the meaning of speech and its acoustic properties, on top of VAD. |
| [Realtime models](#realtime-models) | When using a realtime LLM (for example, the OpenAI Realtime API or Gemini Live API), rely on its built-in server-side detection or pair it with the turn detector model. |
| [VAD only](#vad-only) | When you need minimal latency, or support for a spoken language the turn detector model doesn't cover. |
| [STT endpointing](#stt-endpointing) | When you're already using an STT with its own turn detection (for example, AssemblyAI or Deepgram Flux). |
| [Manual turn control](#manual) | For push-to-talk or fully explicit control over turn boundaries. |
- **Supporting features**: Regardless of detection mode, you can tune behavior with additional turn handling options. The following features are available in addition to turn detection modes to make turn-taking feel natural:

| Feature | Description |
| [Endpointing delay](#endpointing-configuration) | Controls how long the agent waits after speech (or after an STT end-of-utterance signal) before treating the turn as complete. Use fixed `min_delay` and `max_delay`, or dynamic endpointing (Python only) to adapt the delay based on session pause statistics. |
| [Adaptive interruption handling](#adaptive-interruption-handling) | Controls how the agent detects and reacts when the user speaks while the agent is talking. Adaptive interruption handling can distinguish true interruptions from conversational backchanneling. |
| [VAD](https://docs.livekit.io/agents/logic/turns/vad.md) | Use VAD in addition to turn detection modes to improve end-of-turn timing and interruption responsiveness. |
| [Noise cancellation](#noise-cancellation) | Enhanced noise cancellation improves the quality of turn detection and speech-to-text (STT) for voice AI apps by reducing background noise. |

### Turn detector model

The turn detector model is the recommended way to achieve the natural behavior of an agent that listens while the user speaks and replies after they finish their thought. It's also the default: `AgentSession` enables the [audio turn detector](https://docs.livekit.io/agents/logic/turns/turn-detector.md#audio-turn-detector) automatically, so most agents need no turn-detection configuration at all.

It's built for the STT-LLM-TTS pipeline alongside a VAD:

- **[LiveKit turn detector](https://docs.livekit.io/agents/logic/turns/turn-detector.md)**: Audio and text models that detect end of turn from the meaning of speech.

- **[Silero VAD](https://docs.livekit.io/agents/logic/turns/vad.md)**: Silero VAD model for voice activity detection.

The following example uses the recommended [audio turn detector](https://docs.livekit.io/agents/logic/turns/turn-detector.md#audio-turn-detector):

**Python**:

```python
from livekit.agents import AgentSession, TurnHandlingOptions, inference

session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection=inference.TurnDetector(),
    ),
    # ... stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { inference, voice } from '@livekit/agents';

const session = new voice.AgentSession({
  turnHandling: {
    turnDetection: new inference.TurnDetector(),
  },
  // ... stt, tts, llm, etc.
});

```

See the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md) for a complete example.

### Realtime models

Realtime models include built-in turn detection options based on VAD and other techniques. Set the `turn_detection` parameter to `"realtime_llm"` and configure the realtime model's turn detection options directly.

You can also use the [LiveKit turn detector](https://docs.livekit.io/agents/logic/turns/turn-detector.md) with realtime models.

- **[OpenAI Realtime API turn detection](https://docs.livekit.io/agents/models/realtime/plugins/openai.md#turn-detection)**: Turn detection options for the OpenAI Realtime API.

- **[Gemini Live API turn detection](https://docs.livekit.io/agents/models/realtime/plugins/gemini.md#turn-detection)**: Turn detection options for the Gemini Live API.

#### Interruption in realtime mode

When you use a realtime model with server-side turn detection, the model decides when the user is interrupting. The agent forwards user audio to the model unchanged and reacts to the model's interruption signal directly. As a result, [InterruptionOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) mostly does not apply: `enabled` must remain `True`, `discard_audio_if_uninterruptible` still gates buffered audio, and every other field is ignored. Tune interruption on the model itself instead. For example, the OpenAI Realtime API exposes `threshold`, `prefix_padding_ms`, and `silence_duration_ms` on its server VAD `TurnDetection` object (and `eagerness` and `interrupt_response` for semantic VAD).

> 🔥 **Disabling interruptions is a hard error**
> 
> With a realtime model that has server-side turn detection enabled, the SDK rejects `turn_handling.interruption.enabled=False` at session start with a `ValueError`. To disable user interruptions for a realtime model, set the model's own `turn_detection=None` and use VAD on the `AgentSession` instead.

`discard_audio_if_uninterruptible` controls whether buffered user audio is forwarded to the realtime session while the agent is in a non-interruptible utterance.

The following telephony-friendly configuration uses server VAD with a higher threshold for noisy phone audio and a tighter silence window for quicker turn closing.

**Python**:

```python
from livekit.agents import AgentSession
from livekit.plugins.openai import realtime
from openai.types.beta.realtime.session import TurnDetection

session = AgentSession(
    llm=realtime.RealtimeModel(
        turn_detection=TurnDetection(
            type="server_vad",
            threshold=0.7,            # less sensitive (better for noisy phone audio)
            prefix_padding_ms=300,
            silence_duration_ms=400,  # tighter silence window for snappier turn closing
        ),
    ),
    # ... tts, etc.
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import * as openai from '@livekit/agents-plugin-openai';

const session = new voice.AgentSession({
  llm: new openai.realtime.RealtimeModel({
    turnDetection: {
      type: 'server_vad',
      threshold: 0.7,
      prefix_padding_ms: 300,
      silence_duration_ms: 400,
    },
  }),
  // ... tts, etc.
});

```

For the full set of provider-side options, see [OpenAI Realtime API turn detection](https://docs.livekit.io/agents/models/realtime/plugins/openai.md#turn-detection) or [Gemini Live API turn detection](https://docs.livekit.io/agents/models/realtime/plugins/gemini.md#turn-detection).

### VAD only

Use VAD-only detection when you need minimal latency or support for a spoken language the [turn detector model](#turn-detector-model) doesn't cover. To use VAD alone, set `turn_detection="vad"`.

**Python**:

```python
session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection="vad",
    ),
    # ... stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const session = new voice.AgentSession({
  turnHandling: {
    turnDetection: 'vad',
  },
  // ... stt, tts, llm, etc.
});

```

### STT endpointing

Some STT providers, such as [AssemblyAI](https://docs.livekit.io/agents/models/stt/assemblyai.md) and [Deepgram Flux](https://docs.livekit.io/agents/models/stt/deepgram.md), include their own turn detection. If you're already using one, you can rely on it directly instead of the [turn detector model](#turn-detector-model).

The session's bundled VAD continues to handle interruption detection, so the agent stays responsive while the STT determines turn boundaries.

To use STT endpointing, set `turn_detection="stt"` and provide an STT plugin.

**Python**:

```python
session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection="stt",
    ),
    stt=assemblyai.STT(),  # AssemblyAI is the recommended STT plugin for STT-based endpointing
    # ... tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import * as assemblyai from '@livekit/agents-plugin-assemblyai';

const session = new voice.AgentSession({
  stt: new assemblyai.STT(), // AssemblyAI is the recommended STT plugin for STT-based endpointing
  turnHandling: {
    turnDetection: 'stt',
  },
  // ... tts, llm, etc.
});

```

#### Additional endpointing configuration options

You can configure additional endpointing behavior using the `endpointing` key in the turn handling options. By default, the agent uses fixed endpointing and always uses the configured `min_delay` and `max_delay`. With dynamic endpointing, the agent adapts the delay within that range based on session pause statistics, so turn-taking can feel more responsive over time.

To learn more, see the [EndpointingOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#endpointingoptions) reference.

### Manual turn control

For push-to-talk or fully explicit control over turn boundaries, disable automatic turn detection by setting `turn_detection="manual"` in the turn handling options for the `AgentSession`.

You can control the user's turn with `session.interrupt()`, `session.clear_user_turn()`, and `session.commit_user_turn()` methods.

> 💡 **Manual control vs. text-only sessions**
> 
> This is different from toggling audio input/output for [text-only sessions](https://docs.livekit.io/agents/build/text.md#text-only-sessions).

For instance, you can use this to implement a push-to-talk interface. Here is a simple example using [RPC](https://docs.livekit.io/transport/data/rpc.md) methods that the frontend can call:

**Python**:

```python
session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection="manual",
    ),
    # ... stt, tts, llm, etc.
)

# Disable audio input at the start
session.input.set_audio_enabled(False)

# When user starts speaking
@ctx.room.local_participant.register_rpc_method("start_turn")
async def start_turn(data: rtc.RpcInvocationData):
    session.interrupt()  # Stop any current agent speech
    session.clear_user_turn()  # Clear any previous input
    session.input.set_audio_enabled(True)  # Start listening

# When user finishes speaking
@ctx.room.local_participant.register_rpc_method("end_turn")
async def end_turn(data: rtc.RpcInvocationData):
    session.input.set_audio_enabled(False)  # Stop listening
    session.commit_user_turn()  # Process the input and generate response

# When user cancels their turn
@ctx.room.local_participant.register_rpc_method("cancel_turn")
async def cancel_turn(data: rtc.RpcInvocationData):
    session.input.set_audio_enabled(False)  # Stop listening
    session.clear_user_turn()  # Discard the input

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const session = new voice.AgentSession({
  turnHandling: {
    turnDetection: 'manual',
  },
  // ... stt, tts, llm, etc.
});

// Disable audio input at the start
session.input.setAudioEnabled(false);

// When user starts speaking
ctx.room.localParticipant.registerRpcMethod('start_turn', async (data) => {
  session.interrupt(); // Stop any current agent speech
  session.clearUserTurn(); // Clear any previous input
  session.input.setAudioEnabled(true); // Start listening
  return 'ok';
});

// When user finishes speaking
ctx.room.localParticipant.registerRpcMethod('end_turn', async (data) => {
  session.input.setAudioEnabled(false); // Stop listening
  session.commitUserTurn(); // Process the input and generate response
  return 'ok';
});

// When user cancels their turn
ctx.room.localParticipant.registerRpcMethod('cancel_turn', async (data) => {
  session.input.setAudioEnabled(false); // Stop listening
  session.clearUserTurn(); // Discard the input
  return 'ok';
});

```

These RPC methods map to the user pressing and releasing a talk button on the frontend:

- `start_turn`: interrupts the agent, clears any buffered input, and starts listening to the user.
- `end_turn`: stops listening and commits the turn so the agent generates a reply.
- `cancel_turn`: stops listening and discards the turn without a reply.

#### Capture the turn transcript

Available in:
- [ ] Node.js
- [x] Python

Both SDKs commit a turn with `commit_user_turn()`, but only the Python SDK returns the transcript. In Python, `commit_user_turn()` returns an `asyncio.Future[str]` that resolves with the user's transcript once speech-to-text (STT) completes. Await it to capture what the user said:

```python
@ctx.room.local_participant.register_rpc_method("end_turn")
async def end_turn(data: rtc.RpcInvocationData):
    session.input.set_audio_enabled(False)  # Stop listening
    transcript = await session.commit_user_turn(
        # How long to wait for the final transcript after committing the turn.
        # Increase this value if your STT is slow to return final results.
        transcript_timeout=5.0,
        # Silence appended to the STT stream to flush the buffer and force a final transcript.
        stt_flush_duration=2.0,
    )
    logger.info(f"user said: {transcript}")

```

Both `transcript_timeout` and `stt_flush_duration` default to `2.0` seconds.

#### Commit a turn without a reply

Available in:
- [ ] Node.js
- [x] Python

In Python, pass `skip_reply=True` to `commit_user_turn()` to commit and transcribe the user's turn without generating a reply. This is useful when you only need the transcript, or when your app decides separately when the agent should speak:

```python
transcript = await session.commit_user_turn(skip_reply=True)

```

#### Listen to a specific participant

Available in:
- [ ] Node.js
- [x] Python

In a room with multiple participants, route audio input to whoever started the turn so the agent only listens to that caller. Use the caller identity from the RPC invocation:

```python
@ctx.room.local_participant.register_rpc_method("start_turn")
async def start_turn(data: rtc.RpcInvocationData):
    session.interrupt()
    session.clear_user_turn()
    # Listen to the participant who started the turn.
    session.room_io.set_participant(data.caller_identity)
    session.input.set_audio_enabled(True)

```

#### Ignore empty turns

If a user commits a turn without speaking, you can stop the agent from replying by overriding the [`on_user_turn_completed`](https://docs.livekit.io/agents/logic/nodes.md#on_user_turn_completed) node and raising `StopResponse` when the transcript is empty:

**Python**:

```python
from livekit.agents.llm import ChatContext, ChatMessage, StopResponse

class MyAgent(Agent):
    async def on_user_turn_completed(
        self, turn_ctx: ChatContext, new_message: ChatMessage
    ) -> None:
        if not new_message.text_content:
            raise StopResponse()

```

---

**Node.js**:

```typescript
import { llm, voice } from '@livekit/agents';

const agent = voice.Agent.create({
  async onUserTurnCompleted(ctx, chatCtx, newMessage) {
    if (!newMessage.textContent || newMessage.textContent.length === 0) {
      throw new voice.StopResponse();
    }
  },
});

```

### Reducing background noise

[Enhanced noise cancellation](https://docs.livekit.io/transport/media/noise-cancellation.md) is available in LiveKit Cloud and improves the quality of turn detection and speech-to-text (STT) for voice AI apps. You can add background noise and voice cancellation to your agent by adding it to the [room options](https://docs.livekit.io/agents/logic/sessions.md#room-options) when you start your agent session. To learn how to enable it, see the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md).

## Interruptions

The framework pauses the agent's speech whenever it detects user speech in the input audio, ensuring the agent feels responsive. The user can interrupt the agent at any time, either by speaking (with automatic turn detection) or via the `session.interrupt()` method. When interrupted, the agent stops speaking and automatically truncates its conversation history to include only the portion of the speech that the user heard before interruption.

> ℹ️ **Disabling interruptions**
> 
> You can disable user interruptions when [scheduling speech](https://docs.livekit.io/agents/build/audio.md#manual) using the `say()` or `generate_reply()` methods by setting `turn_handling.interruption.enabled` to `false`. To learn more, see [Interruption mode](#interruption-mode).

To explicitly interrupt the agent, call the `interrupt()` method on the handle or session at any time. This can be performed even when interruption is disabled in the turn handling options.

**Python**:

```python
handle = session.say("Hello world")
handle.interrupt()

# or from the session
session.interrupt()

```

---

**Node.js**:

```typescript
const handle = session.say('Hello world');
handle.interrupt();

// or from the session
session.interrupt();

```

> 💡 **Long-running tool calls**
> 
> See the section on tool [interruptions](https://docs.livekit.io/agents/build/tools.md#interruptions) for more information on handling interruptions during long-running tool calls.

### Interruption mode

The interruption options control whether the agent can be interrupted and how interruptions are detected. Key settings:

- `enabled`: When `True`, the agent can be interrupted by user speech; when `False`, the agent cannot be interrupted.
- `mode`: Determines how the framework detects interruptions. Only applies when `enabled` is `True`. The following modes are available:- `"adaptive"`: Adaptive interruption handling. This is the default mode for agents deployed to LiveKit Cloud, when used with most STT providers. To learn more see [Adaptive interruption handling](#adaptive-interruption-handling).
- `"vad"`: Use [VAD](https://docs.livekit.io/agents/logic/turns/vad.md) for interruption detection. Interruption detection is based on speech start and stop cues.

For realtime models with server-side turn detection, see [Interruption in realtime mode](#interruption-in-realtime-mode) for which of these fields are ignored.

To learn more, see the [InterruptionOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) reference.

### Adaptive interruption handling

Adaptive interruption handling enables your agent to intelligently detect when users interrupt mid-response. Rather than using fixed thresholds, adaptive interruption handling analyzes the audio signals to determine whether an interruption is intentional.

- **[Adaptive interruption handling](https://docs.livekit.io/agents/logic/turns/adaptive-interruption-handling.md)**: Use adaptive interruption handling to distinguish between true interruptions and conversational backchanneling.

### False interruptions

In some cases, the framework detects human speech audio and interrupts the agent, but the transcription comes up empty as no actual words are spoken. In these cases, the VAD-based interruption is considered a false positive. By default, the agent resumes speaking from where it left off after a false interruption. You can configure this behavior using the `resume_false_interruption` and `false_interruption_timeout` parameters.

- `false_interruption_timeout`: If an interruption is detected, but the user is silent, this is the duration of silence to wait after an interruption before emitting an `agent_false_interruption` event. Python uses seconds (for example, `2.0`); Node.js uses milliseconds (for example, `2000`).
- `resume_false_interruption`: Whether to resume the agent's speech after a false interruption is detected. If `True`, the agent continues speaking from where it left off after the `false_interruption_timeout` period has passed with no user transcription.

Set these parameters in the `interruption` key of the turn handling options. For example, the following configuration resumes the agent's speech after a false interruption is detected after 2 seconds of silence. Pass it to the `turn_handling` parameter of `AgentSession`:

**Python**:

```python
turn_handling = {
    "interruption": {
        "false_interruption_timeout": 2.0,
        "resume_false_interruption": True,
        # ... other interruption parameters
    },
}

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
    turnHandling: {
        interruption: {
            falseInterruptionTimeout: 2000,
            resumeFalseInterruption: true,
            // ... other interruption parameters
        },
    },
    // ... other parameters
});

```

For more information on these parameters, see the [InterruptionOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) reference.

### Additional configuration options

For a complete list of interruption options, see the [InterruptionOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) reference.

The following additional parameters are available in the `interruption` options object `InterruptionOptions`:

- `discard_audio_if_uninterruptible`: When `True`, drop buffered audio if the agent is speaking and cannot be interrupted.
- `min_duration`: Minimum duration of speech (in seconds) to register as an interruption.
- `min_words`: Minimum number of words to be considered as an interruption. Only used if STT is enabled. Set to a value greater than `0` to require actual speech content before triggering interruptions.

To learn more about these parameters, see the [InterruptionOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) reference.

## User turn limit

User turn limits cap how long a user can speak before the agent interrupts. This is useful for voicebot scenarios where a caller might monopolize the turn: long-form callers, voicemail greetings, or users reading off a list. Unlike [interruptions](#interruptions), which are user-initiated, user turn limits are agent-initiated.

Configure user turn limits in the `user_turn_limit` key of the turn handling options. Set `max_words`, `max_duration`, or both. Both default to disabled, so the feature is off until you opt in. Pass the options to the `turn_handling` parameter of `AgentSession`:

**Python**:

```python
session = AgentSession(
    turn_handling={
        "user_turn_limit": {
            "max_words": 100,
            "max_duration": 30.0,
        },
    },
    # ... other parameters
)

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
    turnHandling: {
        userTurnLimit: {
            maxWords: 100,
            maxDuration: 30_000,
        },
    },
    // ... other parameters
});

```

Python uses seconds for `max_duration`. Node.js uses milliseconds for `maxDuration`.

Word count and duration accumulate across consecutive user turns and reset only when the agent transitions to the `speaking` state. A user who pauses briefly mid-monologue still trips the threshold.

When a threshold is crossed, the framework calls the agent's [`on_user_turn_exceeded`](https://docs.livekit.io/agents/logic/nodes.md#on_user_turn_exceeded) hook with a `UserTurnExceededEvent`. The default implementation calls `generate_reply` with `allow_interruptions=False` and `tool_choice="none"` to politely cut in. Override the hook to customize the behavior:

**Python**:

```python
from livekit.agents import Agent, UserTurnExceededEvent

class MyAgent(Agent):
    async def on_user_turn_exceeded(self, ev: UserTurnExceededEvent) -> None:
        await self.session.say("Sorry to jump in. Can I help with anything specific?")

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  async onUserTurnExceeded(ctx, ev) {
    await ctx.session.say('Sorry to jump in. Can I help with anything specific?');
  },
});

```

> ℹ️ **Default reply cannot be interrupted**
> 
> The default `on_user_turn_exceeded` implementation calls `generate_reply` with `allow_interruptions=False`, so the user cannot cut in while the agent is delivering the cut-in reply. Override the hook if you need different interruption semantics.

The framework skips the `on_user_turn_exceeded` callback if the agent enters the `speaking` state before the threshold fires. This happens when the user pauses long enough for end-of-utterance detection to end their turn naturally and the agent's normal reply starts playing.

To learn more, see the [UserTurnLimitOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#userturnlimitoptions) reference and the [`on_user_turn_exceeded`](https://docs.livekit.io/agents/logic/nodes.md#on_user_turn_exceeded) hook docs.

## Session events

The `AgentSession` emits events for turn handling. For a list of all available events, see the [Events](https://docs.livekit.io/reference/agents/events.md) reference.

### Interruption events

The `AgentSession` exposes interruption events to monitor the flow of a conversation:

**Python**:

```python
@session.on("user_interruption_detected")
def on_interruption(ev):
    print(f"User interrupted at: {ev.timestamp}")
    print(f"Interruption probability: {ev.probability}")

@session.on("agent_false_interruption")
def on_false_interruption(ev):
    print("False interruption detected, resuming speech")

```

---

**Node.js**:

```typescript
session.on('user_interruption_detected', (ev) => {
  console.log(`User interrupted at: ${ev.timestamp}`);
  console.log(`Interruption probability: ${ev.probability}`);
});

session.on('agent_false_interruption', () => {
  console.log('False interruption detected, resuming speech');
});

```

### Turn-taking events

The `AgentSession` exposes user and agent state events to monitor the flow of a conversation:

**Python**:

```python
from livekit.agents import UserStateChangedEvent, AgentStateChangedEvent

@session.on("user_state_changed")
def on_user_state_changed(ev: UserStateChangedEvent):
    if ev.new_state == "speaking":
        print("User started speaking")
    elif ev.new_state == "listening":
        print("User stopped speaking")
    elif ev.new_state == "away":
        print("User is not present (e.g. disconnected)")

@session.on("agent_state_changed")
def on_agent_state_changed(ev: AgentStateChangedEvent):
    if ev.new_state == "initializing":
        print("Agent is starting up")
    elif ev.new_state == "idle":
        print("Agent is ready but not processing")
    elif ev.new_state == "listening":
        print("Agent is listening for user input")
    elif ev.new_state == "thinking":
        print("Agent is processing user input and generating a response")
    elif ev.new_state == "speaking":
        print("Agent started speaking")

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

session.on(voice.AgentSessionEventTypes.UserStateChanged, (ev) => {
  if (ev.newState === 'speaking') {
    console.log('User started speaking');
  } else if (ev.newState === 'listening') {
    console.log('User stopped speaking');
  } else if (ev.newState === 'away') {
    console.log('User is not present (e.g. disconnected)');
  }
});

session.on(voice.AgentSessionEventTypes.AgentStateChanged, (ev) => {
  if (ev.newState === 'initializing') {
    console.log('Agent is starting up');
  } else if (ev.newState === 'idle') {
    console.log('Agent is ready but not processing');
  } else if (ev.newState === 'listening') {
    console.log('Agent is listening for user input');
  } else if (ev.newState === 'thinking') {
    console.log('Agent is processing user input and generating a response');
  } else if (ev.newState === 'speaking') {
    console.log('Agent started speaking');
  }
});

```

## Additional resources

- **[Agent speech](https://docs.livekit.io/agents/build/audio.md)**: Guide to agent speech and related methods.

- **[Pipeline nodes](https://docs.livekit.io/agents/build/nodes.md)**: Monitor input and output as it flows through the voice pipeline.

- **[Turn-taking tuning](https://docs.livekit.io/agents/logic/turns/tuning.md)**: Recommended configs and a troubleshooting guide for turn-taking knobs.

- **[Turn handling options](https://docs.livekit.io/reference/agents/turn-handling-options.md)**: Reference documentation for turn detection, endpointing, and interruption handling options for your agent session.

---

This document was rendered at 2026-08-28T04:22:11.938Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/turns.md](https://docs.livekit.io/agents/logic/turns.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-11"></a>
## Page 11: agents/logic/agents-handoffs/
**Original URL:** https://docs.livekit.io/agents/logic/agents-handoffs/  
**Source MD URL:** https://docs.livekit.io/agents/logic/agents-handoffs.md

LiveKit docs › Build Agents › Logic & Structure › Agents & handoffs

---

# Agents and handoffs

> How to use agents and handoffs as part of a voice AI workflow.

## Overview

Agents are the core units of a voice AI [workflow](https://docs.livekit.io/agents/logic/workflows.md). They define the instructions, tools, and reasoning behavior that drive a conversation. An agent can transfer control to other agents when different logic or capabilities are required. Create separate agents when you need distinct reasoning behavior or tool access:

- **Different roles**: A moderator agent versus a coaching agent.
- **Model specialization**: A lightweight triage model before escalating to a larger one.
- **Different permissions**: An agent with payment API access versus one handling general inquiries.
- **Specialized contexts**: Agents optimized for particular conversation phases.

## Agents

Agents orchestrate the session flow — managing tools, reasoning steps, and control transfers between other agents or tasks.

### Defining an agent

Use `Agent.create` to define a custom agent with instructions, tools, and lifecycle hooks.

**Python**:

```python
from livekit.agents import Agent

class HelpfulAssistant(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful voice AI assistant.")

    async def on_enter(self) -> None:
        await self.session.generate_reply(instructions="Greet the user and ask how you can help them.")

```

---

**Node.js**:

```ts
import { voice } from '@livekit/agents';

const helpfulAssistant = voice.Agent.create({
  instructions: 'You are a helpful voice AI assistant.',
  onEnter(ctx) {
    ctx.session.generateReply({
      instructions: 'Greet the user and ask how you can help them.',
    });
  },
});

```

You can also create an agent inline:

**Python**:

```python
agent = Agent(instructions="You are a helpful voice AI assistant.")

```

---

**Node.js**:

```ts
const agent = voice.Agent.create({
  instructions: 'You are a helpful voice AI assistant.',
});

```

### Setting the active agent

The **active** agent is the agent currently in control of the session. The initial agent is defined in the `AgentSession` constructor. You can change the active agent using the `update_agent` method in Python, or a handoff from a [tool call](#tool-handoff). You can read the active agent using the `current_agent` property.

Specify the initial agent in the `AgentSession` constructor:

**Python**:

```python
session = AgentSession(
    agent=CustomerServiceAgent()
    # ...
)

```

---

**Node.js**:

```ts
await session.start({
  agent: createCustomerServiceAgent(),
  room: ctx.room,
});

```

To set a new agent, use the `update_agent` method:

**Python**:

```python
session.update_agent(CustomerServiceAgent())

```

---

**Node.js**:

```ts
session.updateAgent(createCustomerServiceAgent());

```

### Agent handoffs

A **handoff** transfers session control from one agent to another. You can return a different agent from within a tool call to hand off control automatically. This allows the LLM to make decisions about when a handoff should occur. For more information, see [tool return value](https://docs.livekit.io/agents/logic/tools/definition.md#return-value).

**Python**:

```python
from livekit.agents import Agent, RunContext, function_tool

class CustomerServiceAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="""You are a friendly customer service representative. Help customers with
            general inquiries, account questions, and technical support. If a customer needs
            specialized help, transfer them to the appropriate specialist."""
        )

    async def on_enter(self) -> None:
        await self.session.generate_reply(instructions="Greet the user warmly and offer your assistance.")

    @function_tool()
    async def transfer_to_billing(self, context: RunContext):
        """Transfer the customer to a billing specialist for account and payment questions."""
        return BillingAgent(chat_ctx=self.chat_ctx), "Transferring to billing"

    @function_tool()
    async def transfer_to_technical_support(self, context: RunContext):
        """Transfer the customer to technical support for product issues and troubleshooting."""
        return TechnicalSupportAgent(chat_ctx=self.chat_ctx), "Transferring to technical support"

class BillingAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="""You are a billing specialist. Help customers with account questions, 
            payments, refunds, and billing inquiries. Be thorough and empathetic."""
        )

    async def on_enter(self) -> None:
        await self.session.generate_reply(instructions="Introduce yourself as a billing specialist and ask how you can help with their account.")

class TechnicalSupportAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="""You are a technical support specialist. Help customers troubleshoot 
            product issues, setup problems, and technical questions. Ask clarifying questions 
            to diagnose problems effectively."""
        )

    async def on_enter(self) -> None:
        await self.session.generate_reply(instructions="Introduce yourself as a technical support specialist and offer to help with any technical issues.")

```

---

**Node.js**:

```ts
import { voice, llm } from '@livekit/agents';

function createCustomerServiceAgent() {
  return voice.Agent.create({
    instructions: `You are a friendly customer service representative. Help customers with
      general inquiries, account questions, and technical support. If a customer needs
      specialized help, transfer them to the appropriate specialist.`,
    tools: [
      llm.tool({
        name: 'transferToBilling',
        description: 'Transfer the customer to a billing specialist for account and payment questions.',
        execute: async () => {
          return llm.handoff({
            agent: createBillingAgent(),
            returns: 'Transferring to billing',
          });
        },
      }),
      llm.tool({
        name: 'transferToTechnicalSupport',
        description: 'Transfer the customer to technical support for product issues and troubleshooting.',
        execute: async () => {
          return llm.handoff({
            agent: createTechnicalSupportAgent(),
            returns: 'Transferring to technical support',
          });
        },
      }),
    ],
    onEnter(ctx) {
      ctx.session.generateReply({
        instructions: 'Greet the user warmly and offer your assistance.',
      });
    },
  });
}

function createBillingAgent() {
  return voice.Agent.create({
    instructions: `You are a billing specialist. Help customers with account questions,
      payments, refunds, and billing inquiries. Be thorough and empathetic.`,
    onEnter(ctx) {
      ctx.session.generateReply({
        instructions: 'Introduce yourself as a billing specialist and ask how you can help with their account.',
      });
    },
  });
}

function createTechnicalSupportAgent() {
  return voice.Agent.create({
    instructions: `You are a technical support specialist. Help customers troubleshoot
      product issues, setup problems, and technical questions. Ask clarifying questions
      to diagnose problems effectively.`,
    onEnter(ctx) {
      ctx.session.generateReply({
        instructions: 'Introduce yourself as a technical support specialist and offer to help with any technical issues.',
      });
    },
  });
}

```

> ℹ️ **Passing chat_ctx to agents**
> 
> In Python, `BillingAgent(chat_ctx=self.chat_ctx)` passes `chat_ctx` even though `BillingAgent.__init__` doesn't explicitly accept it. This works because the `Agent` base class constructor accepts `chat_ctx` as a keyword argument. In Node.js, pass `chatCtx` in the `Agent.create` options object. For more details, see [context preservation](#context-preservation).

#### Chat history

When an agent handoff occurs, an `AgentHandoff` item (or `AgentHandoffItem` in Node.js) is added to the chat context with the following properties:

- `old_agent_id`: ID of the agent that was active before the handoff.
- `new_agent_id`: ID of the agent that took over session control after the handoff.

### Passing state

To store custom state within your session, use the `userdata` attribute. The type of `userdata` is up to you, but the recommended approach is to use a `dataclass` in Python or a typed interface in TypeScript.

**Python**:

```python
from livekit.agents import AgentSession
from dataclasses import dataclass

@dataclass
class MySessionInfo:
    user_name: str | None = None
    age: int | None = None

```

---

**Node.js**:

```ts
interface MySessionInfo {
  userName?: string;
  age?: number;
}

```

To add userdata to your session, pass it in the constructor. You must also specify the type of userdata on the `AgentSession` itself.

**Python**:

```python
session = AgentSession[MySessionInfo](
    userdata=MySessionInfo(),
    # ... tts, stt, llm, etc.
)

```

---

**Node.js**:

```ts
const session = new voice.AgentSession<MySessionInfo>({
  userData: { userName: 'Steve' },
  // ... vad, stt, tts, llm, etc.
});

```

Userdata is available as `session.userdata`, and is also available within function tools on the `RunContext`. The following example shows how to use userdata in an agent workflow that starts with the `IntakeAgent`.

**Python**:

```python
class IntakeAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="""You are an intake agent. Learn the user's name and age."""
        )
        
    @function_tool()
    async def record_name(self, context: RunContext[MySessionInfo], name: str):
        """Use this tool to record the user's name."""
        context.userdata.user_name = name
        return self._handoff_if_done()
    
    @function_tool()
    async def record_age(self, context: RunContext[MySessionInfo], age: int):
        """Use this tool to record the user's age."""
        context.userdata.age = age
        return self._handoff_if_done()
    
    def _handoff_if_done(self):
        if self.session.userdata.user_name and self.session.userdata.age:
            return CustomerServiceAgent()
        else:
            return None

class CustomerServiceAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a friendly customer service representative.")

    async def on_enter(self) -> None:
        userdata: MySessionInfo = self.session.userdata
        await self.session.generate_reply(
            instructions=f"Greet {userdata.user_name} personally and offer your assistance."
        )

```

---

**Node.js**:

```ts
import { voice, llm } from '@livekit/agents';
import { z } from 'zod';

function handoffIfDone(ctx: voice.RunContext<MySessionInfo>) {
  if (ctx.userData.userName && ctx.userData.age) {
    return llm.handoff({
      agent: createCustomerServiceAgent(),
      returns: 'Information collected, transferring to customer service',
    });
  }
  return 'Please provide both your name and age.';
}

function createIntakeAgent() {
  return voice.Agent.create<MySessionInfo>({
    instructions: "You are an intake agent. Learn the user's name and age.",
    tools: [
      llm.tool({
        name: 'recordName',
        description: 'Use this tool to record the user\'s name.',
        parameters: z.object({
          name: z.string(),
        }),
        execute: async ({ name }, { ctx }) => {
          ctx.userData.userName = name;
          return handoffIfDone(ctx);
        },
      }),
      llm.tool({
        name: 'recordAge',
        description: 'Use this tool to record the user\'s age.',
        parameters: z.object({
          age: z.number(),
        }),
        execute: async ({ age }, { ctx }) => {
          ctx.userData.age = age;
          return handoffIfDone(ctx);
        },
      }),
    ],
  });
}

function createCustomerServiceAgent() {
  return voice.Agent.create<MySessionInfo>({
    instructions: 'You are a friendly customer service representative.',
    onEnter(ctx) {
      const userData = ctx.session.userData;
      ctx.session.generateReply({
      instructions: `Greet ${userData.userName} personally and offer your assistance.`,
      });
    },
  });
}

```

## Context preservation

By default, each new agent or task starts with a fresh conversation history for their LLM prompt. This applies to both [tool-based handoffs](#tool-handoff) and `update_agent`. In either case, the new agent only sees its own instructions unless you explicitly pass conversation history using `chat_ctx`.

To include the prior conversation, set the `chat_ctx` parameter in the `Agent` or `AgentTask` constructor. You can either copy the prior agent's `chat_ctx`, or construct a new one based on custom business logic to provide the appropriate context. For example, see [Summarizing context](#summarizing-context) for a helper function that summarizes the prior conversation and passes it to the next agent.

When you pass `chat_ctx.copy()`, the copy includes any instructions in the chat context by default. You can remove them by passing the `exclude_instructions` parameter so only the conversation turns carry over, not the system prompt. See the following examples.

**Python**:

```python
from livekit.agents import ChatContext, function_tool, Agent

class TechnicalSupportAgent(Agent):
    def __init__(self, chat_ctx: ChatContext):
        super().__init__(
            instructions="""You are a technical support specialist. Help customers troubleshoot 
            product issues, setup problems, and technical questions.""",
            chat_ctx=chat_ctx
        )

class CustomerServiceAgent(Agent):
    # ...

    @function_tool()
    async def transfer_to_technical_support(self):
        """Transfer the customer to technical support for product issues and troubleshooting."""
        await self.session.generate_reply(instructions="Inform the customer that you're transferring them to the technical support team.")
        
        # Pass only the conversation turns, not the previous agent's instructions
        return TechnicalSupportAgent(chat_ctx=self.chat_ctx.copy(exclude_instructions=True))

```

---

**Node.js**:

```ts
import { voice, llm } from '@livekit/agents';

function createTechnicalSupportAgent(chatCtx: llm.ChatContext) {
  return voice.Agent.create({
    instructions: `You are a technical support specialist. Help customers troubleshoot
      product issues, setup problems, and technical questions.`,
    chatCtx,
  });
}

function createCustomerServiceAgent(chatCtx: llm.ChatContext) {
  return voice.Agent.create({
    // ... instructions, chatCtx, etc.
    chatCtx,
    tools: [
      llm.tool({
        name: 'transferToTechnicalSupport',
        description: 'Transfer the customer to technical support for product issues and troubleshooting.',
        execute: async (_, { ctx }) => {
          await ctx.session.generateReply({
            instructions: 'Inform the customer that you\'re transferring them to the technical support team.',
          });

          return llm.handoff({
            agent: createTechnicalSupportAgent(
              ctx.session.currentAgent.chatCtx.copy({ excludeInstructions: true }),
            ),
            returns: 'Transferring to technical support team',
          });
        },
      }),
    ],
  });
}

```

The complete conversation history for the session is always available in `session.history`. For a full reference on the `ChatContext` API, see [Chat context](https://docs.livekit.io/agents/logic/chat-context.md).

### Summarizing context

When the prior conversation is long, summarize it before handoff to keep the next agent's context compact. The following helper function filters the chat context down to user and assistant turns, then uses a separate LLM call to generate a brief summary string. It allows you to pass in any `LLM` instance (including a lighter or faster model) independently of the main voice agent.

**Python**:

In Python, [`LLMStream.collect()`](https://docs.livekit.io/agents/models/llm.md#collect) awaits the full response stream and returns a `CollectedResponse` with `text`, `tool_calls`, and `usage` fields.

```python
from livekit.agents import llm, ChatContext, function_tool, Agent, RunContext

async def summarize_session(summarizer: llm.LLM, chat_ctx: ChatContext) -> str | None:
    """Generate a brief summary of user/assistant turns using a separate LLM call."""
    summary_ctx = ChatContext()
    summary_ctx.add_message(
        role="system",
        content="Summarize the conversation between user and assistant. Keep the summary brief, touching on the main topics and outcomes.",
    )

    n_summarized = 0
    for item in chat_ctx.items:
        if item.type != "message":
            continue
        if item.role not in ("user", "assistant"):
            continue
        if item.extra.get("is_summary") is True:  # avoid summarizing previous summaries
            continue
        text = (item.text_content or "").strip()
        if text:
            summary_ctx.add_message(role="user", content=f"{item.role}: {text}")
            n_summarized += 1

    if n_summarized == 0:
        return None

    response = await summarizer.chat(chat_ctx=summary_ctx).collect()
    return response.text.strip() if response.text else None


class TriageAgent(Agent):
    # ...

    @function_tool()
    async def transfer_to_specialist(self, context: RunContext, topic: str):
        """Hand off to a specialist once triage is complete."""
        summarizer = self.session.llm  # or pass a different model, e.g. openai.LLM(model="gpt-4o-mini")
        summary = await summarize_session(summarizer, self.chat_ctx) if summarizer else None

        # Build a fresh context with only the summary for the next agent
        chat_ctx = ChatContext()
        if summary:
            chat_ctx.add_message(role="system", content=f"Prior conversation summary: {summary}")

        return SpecialistAgent(topic, chat_ctx=chat_ctx)

```

---

**Node.js**:

The following example uses `collect()` to accumulate the full response:

```ts
import { voice, llm } from '@livekit/agents';
import { LLM } from '@livekit/agents/llm';
import { z } from 'zod';

async function summarizeSession(
  summarizerLlm: llm.LLM,
  chatCtx: llm.ChatContext,
): Promise<string | null> {
  const summaryCtx = new llm.ChatContext();
  summaryCtx.addMessage({
    role: 'system',
    content: 'Summarize the conversation between user and assistant. Keep the summary brief, touching on the main topics and outcomes.',
  });

  let nSummarized = 0;
  for (const item of chatCtx.items) {
    if (item.type !== 'message') continue;
    if (item.role !== 'user' && item.role !== 'assistant') continue;
    if (item.extra?.is_summary === true) continue; // avoid summarizing previous summaries
    const text = item.textContent?.trim();
    if (text) {
      summaryCtx.addMessage({ role: 'user', content: `${item.role}: ${text}` });
      nSummarized++;
    }
  }

  if (nSummarized === 0) return null;

  const response = await summarizerLlm.chat({ chatCtx: summaryCtx }).collect();
  return response.text || null;
}

function createTriageAgent() {
  return voice.Agent.create({
    // ...
    tools: [
      llm.tool({
        name: 'transferToSpecialist',
        description: 'Hand off to a specialist once triage is complete.',
        parameters: z.object({ topic: z.string() }),
        execute: async ({ topic }, { ctx }) => {
          const sessionLlm = ctx.session.llm;
          const summary =
            sessionLlm instanceof LLM
              ? await summarizeSession(sessionLlm, ctx.session.currentAgent.chatCtx)
              : null;

          // Build a fresh context with only the summary for the next agent
          const chatCtx = new llm.ChatContext();
          if (summary) {
            chatCtx.addMessage({ role: 'system', content: `Prior conversation summary: ${summary}` });
          }

          return llm.handoff({
            agent: createSpecialistAgent(topic, chatCtx),
            returns: `Transferring to ${topic} specialist`,
          });
        },
      }),
    ],
  });
}

```

Other strategies for managing context at handoff:

- **Truncate:** Pass `chat_ctx.copy().truncate(max_items=6)` to carry only the last few turns.
- **Userdata summary:** Store key facts in `userdata` and inject a brief summary (for example, as YAML or JSON) as a system message when the next agent starts.

## Overriding plugins

You can override any of the plugins used in the session by setting the corresponding attributes in your `Agent` or `AgentTask` constructor. This allows you to customize the behavior and properties of the active agent or task in the session by modifying the prompt, TTS, LLM, STT plugins, and more.

For instance, you can change the voice for a specific agent by overriding the `tts` attribute:

**Python**:

```python
from livekit.agents import Agent, inference

class CustomerServiceManager(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a customer service manager who can handle escalated issues.",
            tts=inference.TTS(model="inworld/inworld-tts-2", voice="Ashley")
        )

```

---

**Node.js**:

```ts
import { voice, inference } from '@livekit/agents';

function createCustomerServiceManager() {
  return voice.Agent.create({
    instructions: 'You are a customer service manager who can handle escalated issues.',
    tts: new inference.TTS({ model: 'inworld/inworld-tts-2', voice: 'Ashley' }),
  });
}

```

## Updating models at runtime

Available in:
- [ ] Node.js
- [x] Python

To replace a model on the active agent without a full handoff, call `update_options()` on the `Agent`. The method takes an `stt`, `vad`, `llm`, or `tts` parameter. It changes only the models that you pass. The `stt`, `llm`, and `tts` parameters also accept an inference model string, the same as the constructor. To turn off a model, pass `None`. This overrides the session default.

If the agent is active, the STT and VAD change immediately. The LLM and TTS change at the next generation or synthesis. If the agent isn't active, the new model replaces the stored model. The agent then uses the new model at the next start. The call is synchronous.

The following tool switches the active agent to a more capable LLM for complex requests:

```python
from livekit.agents import Agent, RunContext, function_tool

class Assistant(Agent):
    @function_tool()
    async def escalate_to_advanced_model(self, context: RunContext) -> str:
        """Switch to a more capable model for complex requests."""
        self.update_options(llm="openai/chat-latest")
        return "Switched to the advanced model."

```

> 🔥 **Realtime models can't be replaced on an active agent**
> 
> While the agent is active, you can't set the `llm` parameter to a `RealtimeModel`. You also can't replace a `RealtimeModel` with a different model. Both calls raise a `RuntimeError`. A realtime model opens a session with the model provider at agent start. That session can't move to a different model. To change it, use [`update_agent`](#active-agent) and hand off to a new agent. The method checks the models before it changes them. If a call fails, the agent stays the same.

### Choosing a runtime update method

You can change models or options in three ways while a session runs. Each way applies at a different level. `Agent.update_options()` and a model's own `update_options()` have the same name, but they do different things. `Agent.update_options()` gives the agent a different model, for example a new TTS model. A model's own `update_options()` keeps the same model and changes its settings, for example the temperature of an LLM.

| Method | Scope | Use it to |
| `Agent.update_options()` | Same agent, different model | Replace the STT, VAD, LLM, or TTS on the active agent. |
| [`AgentSession.update_agent()`](#active-agent) | New agent instance | Hand off to a different agent, including its instructions and tools. |
| [`<model>.update_options()`](https://docs.livekit.io/reference/agents/inference-llm-parameters.md#updating-options-at-runtime) | Same model instance | Change provider options on a model, such as the temperature or model string on an `inference.LLM`. |

## Examples

These examples show how to build more complex workflows with multiple agents:

- **[Drive-thru agent](https://github.com/livekit/agents/tree/main/examples/drive_thru)**: A complex food ordering agent with tasks, tools, and a complete evaluation suite.

- **[Front-desk agent](https://github.com/livekit/agents/blob/main/examples/frontdesk)**: A calendar booking agent with tasks, tools, and evaluations.

- **[Medical Office Triage](https://github.com/livekit-examples/python-agents-examples/tree/main/complex-agents/medical_office_triage)**: Multi-agent triage system with agent-to-agent transfers and context preservation.

- **[Restaurant Agent](https://docs.livekit.io/reference/recipes/restaurant-agent.md)**: A multi-agent restaurant system using handoffs and shared state between agents.

## Additional resources

For more information on concepts covered in this topic, see the following related topics:

- **[Workflows](https://docs.livekit.io/agents/logic/workflows.md)**: Complete guide to defining and using workflows in your agents.

- **[Tool definition and use](https://docs.livekit.io/agents/logic/tools.md)**: Complete guide to defining and using tools in your agents.

- **[Tasks & task groups](https://docs.livekit.io/agents/build/tasks.md)**: Complete guide to defining and using tasks and task groups in your agent workflows.

- **[Nodes](https://docs.livekit.io/agents/build/nodes.md)**: Add custom behavior to any component of the voice pipeline.

- **[Agent speech](https://docs.livekit.io/agents/build/audio.md)**: Customize the speech output of your agents.

- **[Testing & evaluation](https://docs.livekit.io/agents/start/testing.md)**: Test every aspect of your agents with a custom test suite.

---

This document was rendered at 2026-08-28T04:22:12.015Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/agents-handoffs.md](https://docs.livekit.io/agents/logic/agents-handoffs.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-12"></a>
## Page 12: agents/logic/external-data/
**Original URL:** https://docs.livekit.io/agents/logic/external-data/  
**Source MD URL:** https://docs.livekit.io/agents/logic/external-data.md

LiveKit docs › Build Agents › Logic & Structure › External data & RAG

---

# External data and RAG

> Best practices for adding context and taking external actions.

## Overview

Your agent can connect to external data sources to retrieve information, store data, or take other actions. In general, you can install any Python package or add custom code to the agent to use any database or API that you need.

For instance, your agent might need to:

- Load a user's profile information from a database before starting a conversation.
- Search a private knowledge base for information to accurately answer user queries.
- Perform read/write/update operations on a database or service such as a calendar.
- Store conversation history or other data to a remote server.

This guide covers best practices and techniques for job initialization, retrieval-augmented generation (RAG), tool calls, and other techniques to connect your agent to external data sources and other systems.

## Initial context

By default, each `AgentSession` begins with an empty [chat context](https://docs.livekit.io/agents/logic/chat-context.md). You can load user or task-specific data into the agent's context before connecting to the room and starting the session. For instance, this agent greets the user by name based on the [job metadata](https://docs.livekit.io/agents/server/job.md#metadata).

**Python**:

```python
from livekit import agents
from livekit.agents import AgentServer, Agent, ChatContext, AgentSession

class Assistant(Agent):
    def __init__(self, chat_ctx: ChatContext) -> None:
        super().__init__(chat_ctx=chat_ctx, instructions="You are a helpful voice AI assistant.")

server = AgentServer()

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: agents.JobContext):
    # Simple lookup, but you could use a database or API here if needed
    metadata = json.loads(ctx.job.metadata)
    user_name = metadata["user_name"]

    session = AgentSession(
        # ... stt, llm, tts, vad, turn_detection, etc.
    )
    
    initial_ctx = ChatContext()
    initial_ctx.add_message(role="assistant", content=f"The user's name is {user_name}.")

    await session.start(
        room=ctx.room,
        agent=Assistant(chat_ctx=initial_ctx),
        # ... room_options, etc.
    )

    await session.generate_reply(
        instructions="Greet the user by name and offer your assistance."
    )

```

---

**Node.js**:

```typescript
import { voice, llm, defineAgent, type JobContext } from '@livekit/agents';

function createAssistant(chatCtx: llm.ChatContext) {
  return voice.Agent.create({
    chatCtx,
    instructions: 'You are a helpful voice AI assistant.',
  });
}

export default defineAgent({
  entry: async (ctx: JobContext) => {
    // Simple lookup, but you could use a database or API here if needed
    const metadata = JSON.parse(ctx.job.metadata);
    const userName = metadata.user_name;

    const session = new voice.AgentSession({
      // ... stt, llm, tts, vad, turnDetection, etc.
    });
    
    const initialCtx = llm.ChatContext.empty();
    initialCtx.addMessage({
      role: 'assistant',
      content: `The user's name is ${userName}.`,
    });

    await session.start({
      room: ctx.room,
      agent: createAssistant(initialCtx),
      // ... inputOptions, outputOptions, etc.
    });

    await session.generateReply({
      instructions: 'Greet the user by name and offer your assistance.',
    });
  },
});

```

> 💡 **Load time optimizations**
> 
> If your agent requires external data in order to start, the following tips can help minimize the impact to the user experience:
> 
> 1. For static data (not user-specific) load it in the [prewarm function](https://docs.livekit.io/agents/server/options.md#prewarm)
> 2. Send user specific data in the [job metadata](https://docs.livekit.io/agents/server/job.md#metadata), [room metadata](https://docs.livekit.io/transport/data/state/room-metadata.md), or [participant attributes](https://docs.livekit.io/transport/data/state/participant-attributes.md) rather than loading it in the entrypoint.
> 3. If you must make a network call in the entrypoint, do so before `ctx.connect()`. This ensures your frontend doesn't show the agent participant before it is listening to incoming audio.

## Tool calls

To achieve the highest degree of precision or take external actions, you can offer the LLM a choice of [tools](https://docs.livekit.io/agents/build/tools.md) to use in its response. These tools can be as generic or as specific as needed for your use case.

For instance, define tools for `search_calendar`, `create_event`, `update_event`, and `delete_event` to give the LLM complete access to the user's calendar. Use [participant attributes](https://docs.livekit.io/transport/data/state/participant-attributes.md) or [job metadata](https://docs.livekit.io/agents/server/job.md#metadata) to pass the user's calendar ID and access tokens to the agent.

- **[Tool definition and use](https://docs.livekit.io/agents/build/tools.md)**: Guide to defining and using custom tools in LiveKit Agents.

## Add context during conversation

You can use the [on_user_turn_completed node](https://docs.livekit.io/agents/build/nodes.md#on_user_turn_completed) to perform a RAG lookup based on the user's most recent turn, prior to the LLM generating a response. This method can be highly performant as it avoids the extra round-trips involved in tool calls, but it's only available for STT-LLM-TTS pipelines that have access to the user's turn in text form. Additionally, the results are only as good as the accuracy of the search function you implement.

For instance, you can use vector search to retrieve additional context relevant to the user's query and inject it into the chat context for the next LLM generation. Here is a simple example:

**Python**:

```python
from livekit.agents import ChatContext, ChatMessage

async def on_user_turn_completed(
    self, turn_ctx: ChatContext, new_message: ChatMessage,
) -> None:
    # RAG function definition omitted for brevity
    rag_content = await my_rag_lookup(new_message.text_content)
    turn_ctx.add_message(
        role="assistant", 
        content=f"Additional information relevant to the user's next message: {rag_content}"
    )

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  async onUserTurnCompleted(ctx, chatCtx, newMessage) {
    // RAG function definition omitted for brevity
    const ragContent = await myRagLookup(newMessage.textContent);
    chatCtx.addMessage({
      role: 'assistant',
      content: `Additional information relevant to the user's next message: ${ragContent}`,
    });
  },
});

```

## User feedback

It's important to provide users with direct feedback about status updates, for example, to explain a delay or failure. Here are a few example use cases:

- When an operation takes more than a few hundred milliseconds.
- When performing write operations such as sending an email or scheduling a meeting.
- When the agent is unable to perform an operation.

The following section describes various techniques to provide this feedback to the user.

> 💡 **Async tools**
> 
> For tools that run in the background with built-in progress updates, see [async tools](https://docs.livekit.io/agents/logic/tools/async.md). `AsyncToolset` handles progress delivery and reply timing automatically, without the manual `generate_reply()` pattern shown below.

### Verbal status updates

Use [Agent speech](https://docs.livekit.io/agents/build/speech.md) to provide verbal feedback to the user during a long-running tool call or other operation.

In the following example, the agent speaks a status update only if the call takes longer than a specified timeout. The update is dynamically generated based on the query, and could be extended to include an estimate of the remaining time or other information.

**Python**:

```python
import asyncio
from livekit.agents import function_tool, RunContext

@function_tool()
async def search_knowledge_base(
    self,
    context: RunContext,
    query: str,
) -> str:
    # Send a verbal status update to the user after a short delay
    async def _speak_status_update(delay: float = 0.5):
        await asyncio.sleep(delay)
        await context.session.generate_reply(instructions=f"""
            You are searching the knowledge base for \"{query}\" but it is taking a little while.
            Update the user on your progress, but be very brief.
        """)
    
    status_update_task = asyncio.create_task(_speak_status_update(0.5))

    # Perform search (function definition omitted for brevity)
    result = await _perform_search(query)
    
    # Cancel status update if search completed before timeout
    status_update_task.cancel()
    
    return result

```

---

**Node.js**:

```typescript
import { llm, Task } from '@livekit/agents';
import { z } from 'zod';

const searchKnowledgeBase = llm.tool({
  name: 'searchKnowledgeBase',
  description: 'Search the knowledge base for information',
  parameters: z.object({
    query: z.string(),
  }),
  execute: async ({ query }, { ctx, abortSignal }) => {
    // Send a verbal status update to the user after a short delay
    const speakStatusUpdate = async (controller: AbortController) => {
      await new Promise(resolve => setTimeout(resolve, 500));
      if (!controller.signal.aborted) {
        ctx.session.generateReply({
          instructions: `You are searching the knowledge base for "${query}" but it is taking a little while. Update the user on your progress, but be very brief.`,
        });
      }
    };

    const statusUpdateTask = Task.from(speakStatusUpdate);

		// Perform search (function definition omitted for brevity)
		const result = await performSearch(query);
		
		// Cancel status update if search completed before timeout
		statusUpdateTask.cancel()
		
		return result;
  },
});

```

For more information, see the following article:

- **[Agent speech](https://docs.livekit.io/agents/build/speech.md)**: Explore the speech capabilities and features of LiveKit Agents.

For fixed phrases like "let me check that for you," you can avoid TTS latency entirely by pre-synthesizing the audio once and replaying it from cache. See [Using cached TTS in a tool call](https://docs.livekit.io/agents/multimodality/audio/customization.md#cached-tts-in-tools) for a complete example that also shows how to cancel the hold message early if the API returns quickly.

### "Thinking" sounds

Add [background audio](https://docs.livekit.io/agents/multimodality/audio/background-audio.md) to play a "thinking" sound automatically when tool calls are ongoing. This can be useful to provide a more natural feel to the agent's responses.

**Python**:

```python
from livekit.agents import AgentServer, BackgroundAudioPlayer, AudioConfig, BuiltinAudioClip

server = AgentServer()

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: agents.JobContext):
    session = AgentSession(
        # ... stt, llm, tts, vad, turn_detection, etc.
    )

    await session.start(
        room=ctx.room,
        # ... agent, etc.
    )

    background_audio = BackgroundAudioPlayer(
        thinking_sound=[
            AudioConfig(BuiltinAudioClip.KEYBOARD_TYPING, volume=0.8),
            AudioConfig(BuiltinAudioClip.KEYBOARD_TYPING2, volume=0.7),
        ],
    )
    await background_audio.start(room=ctx.room, agent_session=session)

```

---

**Node.js**:

```typescript
import { type JobContext, defineAgent, log, voice } from '@livekit/agents';


export default defineAgent({
  entry: async (ctx: JobContext) => {
    const logger = log();

    await ctx.connect();
    logger.info('Connected to room');

    const agent = voice.Agent.create({
      instructions: 'You are a helpful assistant',
      // ... tools, etc.
    });

    const session = new voice.AgentSession({
      // ... stt, llm, tts, vad, turn_detection, etc.
    });
    await session.start({ agent, room: ctx.room });

    const backgroundAudio = new voice.BackgroundAudioPlayer({
      thinkingSound: [
        { source: voice.BuiltinAudioClip.KEYBOARD_TYPING, volume: 0.8, probability: 0.6 },
        { source: voice.BuiltinAudioClip.KEYBOARD_TYPING2, volume: 0.7, probability: 0.4 },
      ],
    });

    await backgroundAudio.start({ room: ctx.room, agentSession: session });

    // Play another audio file at any time using the play method:
    // backgroundAudio.play('filepath.ogg');
  },
});

```

For a complete example, see the following:

- **[Background audio](https://docs.livekit.io/agents/multimodality/audio/background-audio.md)**: Guide to playing background audio in your agent.

- **[Background audio](https://github.com/livekit/agents-js/blob/main/examples/src/background_audio.ts)**: Guide to using background audio in your agent in Node.js.

### Frontend UI

If your app includes a frontend, you can add custom UI to represent the status of the agent's operations. For instance, present a popup for a long-running operation that the user can optionally cancel:

**Python**:

```python
from livekit.agents import get_job_context
import json
import asyncio

@function_tool()
async def perform_deep_search(
    self,
    context: RunContext,
    summary: str,
    query: str,
) -> str:
    """
    Initiate a deep internet search that will reference many external sources to answer the given query. This may take 1-5 minutes to complete.

    Summary: A user-friendly summary of the query
    Query: the full query to be answered
    """
    async def _notify_frontend(query: str):
        room = get_job_context().room
        response = await room.local_participant.perform_rpc(
            destination_identity=next(iter(room.remote_participants)),
            # frontend method that shows a cancellable popup
            # (method definition omitted for brevity, see RPC docs)
            method='start_deep_search',
            payload=json.dumps({
                "summary": summary,
                "estimated_completion_time": 300,
            }),
            # Allow the frontend a long time to return a response
            response_timeout=500,
        )
        # In this example the frontend has a Cancel button that returns "cancelled"
        # to stop the task
        if response == "cancelled":
            deep_search_task.cancel()

    notify_frontend_task = asyncio.create_task(_notify_frontend(query))

    # Perform deep search (function definition omitted for brevity)
    deep_search_task = asyncio.create_task(_perform_deep_search(query))

    try:
        result = await deep_search_task
    except asyncio.CancelledError:
        result = "Search cancelled by user"
    finally:
        notify_frontend_task.cancel()
        return result

```

---

**Node.js**:

```typescript
import { llm, Task, getJobContext } from '@livekit/agents';
import { z } from 'zod';

const performDeepSearch = llm.tool({
  name: 'performDeepSearch',
  description: 'Initiate a deep internet search that will reference many external sources to answer the given query. This may take 1-5 minutes to complete.',
  parameters: z.object({
    summary: z.string(),
    query: z.string(),
  }),
  execute: async ({ summary, query }, { ctx }) => {
    // Notify frontend with cancellable popup
    const notifyFrontend = async (controller: AbortController) => {
      const room = getJobContext().room;
      const participant = Array.from(room.remoteParticipants.values())[0]!;
      
      const response = await room.localParticipant!.performRpc({
        destinationIdentity: participant.identity,
        // frontend method that shows a cancellable popup
        // (method definition omitted for brevity, see RPC docs)
        method: 'start_deep_search',
        payload: JSON.stringify({
          summary,
          estimated_completion_time: 300,
        }),
        // Allow the frontend a long time to return a response
        responseTimeout: 500000,
      });
      
      // In this example the frontend has a Cancel button that returns "cancelled"
      // to stop the task
      if (response === "cancelled") {
        deepResearchTask.cancel();
      }
    };

    const notifyTask = Task.from(notifyFrontend);

    // Perform deep search (function definition omitted for brevity)
    const deepResearchTask = Task.from((controller) => performDeepSearch(query, controller));
      
    let result = "";
    try {
			result = await deepResearchTask.result;
    } catch (error) {
      result = "Search cancelled by user";
    } finally {
	    notifyTask.cancel();
	    return result;
    }
  },
});

```

For more information and examples, see the following articles:

- **[Web and mobile frontends](https://docs.livekit.io/agents/start/frontend.md)**: Guide to building a custom web or mobile frontend for your agent.

- **[RPC](https://docs.livekit.io/transport/data/rpc.md)**: Learn how to use RPC to communicate with your agent from the frontend.

## Fine-tuned models

Sometimes the best way to get the most relevant results is to fine-tune a model for your specific use case. You can explore the available [LLM plugins](https://docs.livekit.io/agents/models/llm.md#plugins) to find a provider that supports fine-tuning, or use [Ollama](https://docs.livekit.io/agents/models/llm/ollama.md) to integrate a custom model.

## External services

Many providers offer services to provide memory or other capabilities to your agents. Some suggested services that work well with LiveKit Agents include:

- **[Letta plugin](https://docs.livekit.io/agents/models/llm/letta.md)**: Build and deploy stateful AI agents that maintain memory and context across long-running conversations.

- **[AgentMail](https://docs.agentmail.to/integrate-livekit-agents)**: Give your agents their own email inboxes.

- **[LlamaIndex](https://www.llamaindex.ai/)**: Framework for connecting custom data to LLMs.

- **[Mem0](https://mem0.ai)**: Self-improving memory layer for AI agents.

## Additional examples

The following examples show how to implement RAG and other techniques:

- **[LlamaIndex RAG](https://github.com/livekit/agents/tree/main/examples/voice_agents/llamaindex-rag)**: A voice AI agent that uses LlamaIndex for RAG to answer questions from a knowledge base.

---

This document was rendered at 2026-08-28T04:22:11.962Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/external-data.md](https://docs.livekit.io/agents/logic/external-data.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-13"></a>
## Page 13: agents/logic/fallback-strategies/
**Original URL:** https://docs.livekit.io/agents/logic/fallback-strategies/  
**Source MD URL:** https://docs.livekit.io/agents/logic/fallback-strategies.md

LiveKit docs › Build Agents › Logic & Structure › Fallback strategies

---

# Fallback strategies

> Configure fallback providers for STT, LLM, and TTS to handle model failures gracefully.

## Overview

In realtime voice conversations, a model API failure can leave the agent unable to continue. Fallback strategies let you define backup providers that automatically take over when the primary provider fails.

Both LiveKit fallback adapters trigger on any error from the primary provider, including connection failures, timeouts, HTTP errors (4xx, 5xx), and mid-stream disconnects.

The fallback adapters handle the following:

- Automatically resubmit the failed request to backup providers when the primary provider fails.
- Mark the failed provider as unhealthy and stop sending requests to it.
- Continue to use the backup providers, periodically probing the failed provider in the background and restoring it once it responds successfully.

When a fallback is triggered, `AgentSession` emits an [error event](https://docs.livekit.io/reference/agents/events.md#error-event-properties) you can use to log failures or notify the user.

LiveKit provides two fallback mechanisms:

- **Inference Fallback Adapter:** fallback logic runs server-side in the LiveKit Inference service. Supports STT and TTS only. Available in Python and Node.js.
- **Agent Fallback Adapter:** fallback logic runs in your agent code. Supports STT, TTS, and LLM. Available in Python and Node.js.

| Feature | Inference Fallback Adapter | Agent Fallback Adapter |
| Supported model types | STT, TTS | STT, TTS, LLM |
| Where fallback runs | Server-side in LiveKit Inference service | In your agent process |
| Python support | STT, TTS | STT, TTS, LLM |
| Node.js support | STT, TTS | STT, TTS, LLM |

## Inference Fallback Adapter

If you use [LiveKit Inference](https://docs.livekit.io/agents/models/inference.md), you can configure fallback models directly with the `fallback` parameter on `inference.STT` and `inference.TTS`. Fallback logic runs server-side in the LiveKit Inference service, so your agent code doesn't need to manage retries or health checks.

**Python**:

```python
from livekit.agents import AgentSession, inference

session = AgentSession(
    stt=inference.STT(
        model="deepgram/nova-3",
        language="en",
        fallback=[
            {"model": "assemblyai/universal-streaming"},
        ],
    ),
    tts=inference.TTS(
        model="inworld/inworld-tts-2",
        voice="Ashley",
        language="en",
        fallback=[
            {
                "model": "cartesia/sonic-3",
                "voice": "9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",
            },
        ],
    ),
    # ... llm, etc.
)

```

---

**Node.js**:

```typescript
import { inference, voice } from '@livekit/agents';

const session = new voice.AgentSession({
  stt: new inference.STT({
    model: 'deepgram/nova-3',
    language: 'en',
    fallback: [{ model: 'assemblyai/universal-streaming' }],
  }),
  tts: new inference.TTS({
    model: 'inworld/inworld-tts-2',
    voice: 'Ashley',
    language: 'en',
    fallback: [
      {
        model: 'cartesia/sonic-3',
        voice: '9626c31c-bec5-4cca-baa8-f8ba9e84c8bc',
      },
    ],
  }),
  // ... llm, etc.
});

```

The model in the top-level parameter is the primary. Models in `fallback` are tried in order if the primary fails.

### Behavior

The Inference Fallback Adapter treats any error as a reason to try the next provider in the chain, including errors during session creation, connection, and mid-stream. If the primary provider fails partway through streaming a response, the service switches to the next model and restarts the request from the beginning. The service only stops trying providers when all configured models have failed or the client disconnects.

> 💡 **Tip**
> 
> If you use [custom voices](https://docs.livekit.io/agents/multimodality/audio/custom-voices.md), TTS fallback across providers is automatic. Each cloned voice is cloned to more than one provider, so LiveKit Inference automatically falls back to another provider if the primary one is unavailable.

## Agent Fallback Adapter

The Agent Fallback Adapter runs fallback logic directly in your agent process using plugins. Use it when you need LLM fallback support, or when you're connecting to providers that aren't available through LiveKit Inference.

**Python**:

```python
from livekit.agents import llm, stt, tts
from livekit.plugins import assemblyai, cartesia, deepgram, inworld, openai

session = AgentSession(
    stt=stt.FallbackAdapter(
        [
            deepgram.STT(),
            assemblyai.STT(),
        ]
    ),
    llm=llm.FallbackAdapter(
        [
            openai.responses.LLM(model="gpt-4o"),
            openai.LLM.with_azure(model="gpt-4o", ...),
        ]
    ),
    tts=tts.FallbackAdapter(
        [
            cartesia.TTS(...),
            inworld.TTS(...),
        ]
    ),
)

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
  stt: new stt.FallbackAdapter({
    sttInstances: [new deepgram.STT(), new assemblyai.STT()],
  }),
  llm: new llm.FallbackAdapter({
    llms: [
      new openai.LLM({ model: 'gpt-4o' }),
      openai.LLM.withAzure({ model: 'gpt-4o' }),
    ],
  }),
  tts: new tts.FallbackAdapter({
    ttsInstances: [new cartesia.TTS(), new inworld.TTS()],
  }),
});

```

The first instance in each list is the primary. Subsequent instances are tried in order if it fails.

### Behavior

The Agent Fallback Adapter triggers on any error, but applies partial output guards to avoid disrupting output that the user has already started receiving:

- **STT**: no partial output guard. The adapter switches to the next provider on any error.
- **TTS**: if audio has already been pushed to the speaker, the adapter does not switch to a backup provider mid-utterance. Fallback is skipped and the partial audio plays through.
- **LLM**: if text or tool calls have already been streamed to the user, the adapter raises the error rather than restarting the response with a different model. Set `retry_on_chunk_sent=True` on `llm.FallbackAdapter` to override this and allow mid-stream fallback.

When a provider is restored after a failure, the Agent Fallback Adapter emits an availability-changed event (`stt_availability_changed`, `llm_availability_changed`, or `tts_availability_changed`) so you can observe the recovery from your agent code.

---

This document was rendered at 2026-08-28T04:22:11.967Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/fallback-strategies.md](https://docs.livekit.io/agents/logic/fallback-strategies.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-14"></a>
## Page 14: agents/prebuilt/tasks/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › Overview

---

# Prebuilt tasks

> Use prebuilt tasks to collect structured data or run workflows without implementing the logic yourself.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

LiveKit Agents includes a number of ready-made task components that you can use to reliably solve recurring problems in voice AI. These tasks have been tested and tuned based on real-world scenarios and can help you rapidly build your own voice AI applications.

> ℹ️ **Tasks overview**
> 
> Tasks are a way to break your agent's logic into well-scoped, reliable chunks. In addition to the prebuilt tasks, you can also easily build your own custom tasks to perform any job you need. For more information, see [Tasks and task groups](https://docs.livekit.io/agents/logic/tasks.md).

These tasks can be found in the [livekit.agents.beta.workflows](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/index.html.md) module.

LiveKit Agents for Python contains the following prebuilt tasks:

| Task | Description |
| [GetNameTask](https://docs.livekit.io/agents/prebuilt/tasks/get-name.md) | Collect and validate a user's name. Configurable first, middle, and last name parts with optional spelling verification. |
| [GetEmailTask](https://docs.livekit.io/agents/prebuilt/tasks/get-email.md) | Collect and validate an email address from the user. Handles noisy voice transcription and spoken patterns. |
| [GetAddressTask](https://docs.livekit.io/agents/prebuilt/tasks/get-address.md) | Collect and validate a complete mailing address. Supports international formats and spoken input. |
| [GetDOBTask](https://docs.livekit.io/agents/prebuilt/tasks/get-dob.md) | Collect and validate a date of birth. Handles spoken dates and optional time of birth. |
| [GetPhoneNumberTask](https://docs.livekit.io/agents/prebuilt/tasks/get-phone-number.md) | Collect and validate a phone number. Normalizes spoken digits and supports international formats. |
| [GetCreditCardTask](https://docs.livekit.io/agents/prebuilt/tasks/get-credit-card.md) | Collect complete credit card information. Runs a task group to gather cardholder name, card number, security code, and expiration date. |
| [GetDtmfTask](https://docs.livekit.io/agents/prebuilt/tasks/get-dtmf.md) | Collect keypad (DTMF) or spoken digits from callers. For IVR menus, PIN entry, and digit capture. |
| [WarmTransferTask](https://docs.livekit.io/agents/prebuilt/tasks/warm-transfer.md) | Execute an agent-assisted warm transfer. Dials the human agent via SIP, plays hold music, and hands off context. |

## Usage

Await a prebuilt task from within your agent, typically from a [function tool](https://docs.livekit.io/agents/logic/tools.md). The task runs until it completes and returns a result. You can run tasks inside a [task group](https://docs.livekit.io/agents/logic/tasks.md) to chain or sequence them.

## Customization

Prebuilt tasks support customization so you can adapt them to your use case. Use the `extra_instructions` parameter to append instructions to a task's default behavior. The task's LLM receives both the built-in instructions and your extra text, so you can steer prompts, add context, or change when to use optional tools. Some tasks also accept a `tools` parameter so you can add or substitute function tools. See each task's parameters section for details.

---

This document was rendered at 2026-08-28T04:22:12.041Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks.md](https://docs.livekit.io/agents/prebuilt/tasks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-15"></a>
## Page 15: agents/prebuilt/tools/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tools/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tools.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tools › Overview

---

# Prebuilt tools

> Use prebuilt tools so your agent can perform common actions without implementing them yourself.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

LiveKit Agents includes a number of ready-made tool components that you can use to reliably solve recurring problems in voice AI. These tools have been tested and tuned based on real-world scenarios and can help you rapidly build your own voice AI applications.

> ℹ️ **Tools overview**
> 
> Tools let your agent perform actions and call external logic in response to the conversation. In addition to the prebuilt tools, you can define your own function tools or use other tool types. For more information, see [Tool definition & use](https://docs.livekit.io/agents/logic/tools.md).

These tools can be found in the [livekit.agents.beta.tools](https://github.com/livekit/agents/tree/main/livekit-agents/livekit/agents/beta/tools) module.

LiveKit Agents for Python contains the following prebuilt tools:

| Tool | Description |
| [EndCallTool](https://docs.livekit.io/agents/prebuilt/tools/end-call-tool.md) | Gracefully end the call and disconnect from the room. Optionally deletes the room and runs custom goodbye instructions. |
| [send_dtmf_events](https://docs.livekit.io/agents/prebuilt/tools/send-dtmf-events.md) | Send DTMF tones to telephony providers. For navigating IVR menus and phone systems. |

## Usage

Add the prebuilt tool to your agent's `tools` list when constructing the agent. The LLM can then call it during the conversation when appropriate. See each tool's page for specific usage instructions.

## Customization

Prebuilt tools support customization so you can adapt them to your use case. Configure behavior via constructor parameters such as `extra_description` or `end_instructions`. See each tool's parameters section for details.

---

This document was rendered at 2026-08-28T04:22:12.039Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tools.md](https://docs.livekit.io/agents/prebuilt/tools.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-16"></a>
## Page 16: agents/server/startup-modes
**Original URL:** https://docs.livekit.io/agents/server/startup-modes  
**Source MD URL:** https://docs.livekit.io/agents/server/startup-modes.md

LiveKit docs › Build Agents › Agent Server › Startup modes

---

# Server startup modes

> Guide to different agent server modes for development, production, and more.

## Overview

The Agents SDK includes a CLI interface that makes it easy to start your agent server in various modes. Each mode is optimized for specific use cases and development stages, from local testing to production deployments.

Your agent server can be started in the following modes:

| Mode | Description |
| [`start`](#start-mode) | Production mode with graceful shutdown handling and optimized logging. |
| [`dev`](#dev-mode) | Development mode with auto-reload and detailed logging for fast iteration. |
| [`console`](#console-mode) | Local, single-session, terminal-based testing. |
| [`connect`](#connect-mode) | Single-session, direct connection to a specific LiveKit room for targeted debugging with live participants. |

## Authentication

You must set authentication credentials before you start your agent server in order to connect to LiveKit and LiveKit Inference. They can be set in environment variables or passed as command-line arguments.

> ℹ️ **Console mode**
> 
> Console mode doesn't use your credentials to connect to LiveKit, but it requires them for LiveKit Inference. Because console mode doesn't accept credentials as command-line arguments, you must provide them in environment variables.

| Argument | Description | Environment variable |
| `--url` | LiveKit server or Cloud project WebSocket URL | `LIVEKIT_URL` |
| `--api-key` | LiveKit API key | `LIVEKIT_API_KEY` |
| `--api-secret` | LiveKit API secret | `LIVEKIT_API_SECRET` |

### Set environment variables

Run the following [LiveKit CLI](https://docs.livekit.io/reference/developer-tools/livekit-cli.md) command to load your LiveKit Cloud API keys into a `.env.local` file:

```shell
lk app env -w

```

The file should look like this:

** Filename: `.env.local`**

```shell
LIVEKIT_API_KEY=<YOUR_API_KEY>
LIVEKIT_API_SECRET=<YOUR_API_SECRET>
LIVEKIT_URL=%{wsURL}%

```

** Filename: `.env.local`**

```shell
LIVEKIT_API_KEY=<YOUR_API_KEY>
LIVEKIT_API_SECRET=<YOUR_API_SECRET>
LIVEKIT_URL=%{wsURL}%

```

## Start mode

Start mode runs your agent server in production with proper error handling and graceful shutdown. This mode connects to LiveKit with settings optimized for production deployments.

Start mode provides the following features:

- **Production logging**: Log level defaults to `info` for clean output.
- **Graceful shutdown**: Drains active jobs before shutting down on `SIGINT` or `SIGTERM` signals.
- **Production optimizations**: Includes load balancing, overload protection, and pre-warmed idle processes to ensure high availability.

To start your agent server in production mode, use the following command:

```shell
lk agent start

```

> ℹ️ **Production mode**
> 
> A deployed agent starts with the command in its `Dockerfile`. The container image doesn't include the `lk` CLI, so a deployed agent can't use `lk agent start`. See [Builds and Dockerfiles](https://docs.livekit.io/deploy/agents/builds.md) for details.

#### Graceful shutdown

In production mode, when your agent server receives a shutdown signal (such as `SIGTERM` from a container orchestrator or `Ctrl+C`), it drains active jobs before closing:

1. Stops accepting new job assignments.
2. Waits for active jobs to complete, up to the drain timeout.
3. Closes all connections and cleans up resources.
4. Exits with appropriate status code.

Set the drain timeout with the `drain_timeout` (Python) or `drainTimeout` (Node.js) server option. See [Drain timeout](https://docs.livekit.io/agents/server/options.md#drain-timeout) for details.

### Parameters

The following parameters are available in production mode:

**Python**:

| Parameter | Description | Default |
| `--log-level` | Set the logging level (`trace`, `debug`, `info`, `warn`, `error`, `critical`) | `info` |

---

**Node.js**:

| Parameter | Description | Default |
| `--log-level` | Set the logging level (`trace`, `debug`, `info`, `warn`, `error`, `fatal`) | `info` |

## Dev mode

In `dev` mode, your agent server starts with features optimized for local development, including enhanced logging and automatic code reloading:

- **Debug logging**: Log level defaults to `debug` for detailed output.
- **Auto-reload**: In Python, auto-reloads when code changes are detected. For Node.js, use `tsx` for automatic TypeScript compilation and reloading.
- **Development optimizations**: No graceful shutdown drain period for faster iteration.

Start your agent server in dev mode with the following command:

```shell
lk agent dev

```

### Parameters

The following parameters are available in dev mode:

**Python**:

| Parameter | Description | Default |
| `--log-level` | Set the logging level (`trace`, `debug`, `info`, `warn`, `error`, `critical`) | `debug` |
| `--no-reload` | Disable auto-reload on file changes. | By default, auto-reload is enabled. |

---

**Node.js**:

| Parameter | Description | Default |
| `--log-level` | Set the logging level (`trace`, `debug`, `info`, `warn`, `error`, `fatal`) | `debug` |

## Console mode

Console mode runs your agent server in your terminal without connecting to LiveKit. This single-session mode simulates a full agent session entirely on your local machine for quick testing and debugging during development.

Console mode allows you to interact with your agent using text or voice, and offers the following features:

- **Audio I/O**: Choose which local audio devices to use for input and output.
- **Visual feedback**: Displays audio input using a real-time frequency visualizer.
- **Text mode**: Toggle between audio and text-only interaction.
- **Session recording**: Record sessions to disk for playback and analysis.

> ℹ️ **LiveKit Inference**
> 
> While console mode doesn't use LiveKit for media transport, if you're using [LiveKit Inference](https://docs.livekit.io/agents/models.md#inference), you must have your authentication credentials set as environment variables in order to test your agent. See the [Authentication](#authentication) section for more information.

Start your agent server in console mode with the following command:

```shell
lk agent console

```

You can speak to your agent with text or voice.

### Parameters

The following parameters are available in console mode:

| Parameter | Description |
| `--text` | Interact with your agent using only text input (no audio). You can also toggle between audio and text input using the shortcut `Ctrl+T`. |
| `--input-device` | Specify the input device to use for audio input using device ID or name substring. Use `--list-devices` to get the device IDs and names for available input devices. |
| `--output-device` | Specify the output device to use for audio output using device ID or name substring. Use `--list-devices` to get the device IDs and names for available output devices. |
| `--list-devices` | List all available input and output audio devices on your system. |
| `--record` | Record the agent session to disk. If enabled, saves the session to a JSON file named `console-recordings/session-<timestamp>/`. |

### Examples

Use these examples to run your agent in console mode with different configurations:

List available audio devices:

```shell
lk agent console --list-devices

```

Run your agent in text-only mode:

```shell
lk agent console --text

```

Specify input and output devices for audio:

```shell
lk agent console --input-device "Macbook Pro Microphone" --output-device "External Headphones"

```

Record the session to disk:

```shell
lk agent console --record

```

## Connect mode

Connect mode starts your agent server with a direct connection to a specific LiveKit room. This single-session mode is useful for testing with live participants or debugging specific room scenarios.

**Python**:

```shell
uv run src/agent.py connect --room my-test-room

```

Connect to a room with a specific participant identity:

```shell
uv run src/agent.py connect --room my-room --participant-identity my-agent-1

```

---

**Node.js**:

```shell
pnpm tsx agent.ts connect --room my-test-room

```

Connect to a room with a specific participant identity:

```shell
pnpm tsx agent.ts connect --room my-room --participant-identity my-agent-1

```

### Parameters

**Python**:

| Parameter | Description | Required |
| `--room` | Name of the room to connect to. If the room doesn't exist, it's automatically created. | Yes |
| `--participant-identity` | Identity to use for the agent participant. Autogenerated if not provided. | No |
| `--log-level` | Set the logging level. Valid values are: `trace`, `debug`, `info`, `warn`, `error`, `critical`. Default is `debug`. | No |

---

**Node.js**:

| Option | Description | Required |
| `--room` | Name of the room to connect to. | Yes |
| `--participant-identity` | Identity to use for the agent participant. Autogenerated if not provided. | No |
| `--log-level` | Set the logging level. Valid values are: `trace`, `debug`, `info`, `warn`, `error`, `fatal`. Default value is `debug` or the value set in the `LOG_LEVEL` environment variable. | No |

## Add scripts in Node.js

If you're using Node.js, you can add the following scripts to your `package.json` file to start your agent server in different modes using `pnpm`:

```json
{
  "scripts": {
    "dev": "lk agent dev",
    "build": "tsc",
    "start": "tsc && node agent.js start",
    "connect": "tsx agent.ts connect"
  }
}

```

The `start` script runs the built agent directly instead of through `lk agent start`, because your `Dockerfile` uses this script to start the deployed agent.

For example, to start the agent in development mode, execute the following command:

```shell
pnpm dev

```

---

This document was rendered at 2026-08-28T04:22:12.038Z.
For the latest version of this document, see [https://docs.livekit.io/agents/server/startup-modes.md](https://docs.livekit.io/agents/server/startup-modes.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-17"></a>
## Page 17: agents/server/lifecycle/
**Original URL:** https://docs.livekit.io/agents/server/lifecycle/  
**Source MD URL:** https://docs.livekit.io/agents/server/lifecycle.md

LiveKit docs › Build Agents › Agent Server › Server lifecycle

---

# Server lifecycle

> How agent servers register, receive requests, and manage jobs.

## Overview

When LiveKit server receives a dispatch request, it routes the request to an available agent server. The first available agent server accepts the job and starts the agent session. An overview of the server lifecycle is as follows:

1. **Agent server registration**: Your agent code registers itself as an "agent server" with LiveKit server, then waits on standby for requests.
2. **Job request**: A dispatch request is sent to LiveKit server — either explicitly via the [AgentDispatchService API](https://docs.livekit.io/agents/server/agent-dispatch.md#via-api) or automatically when a user connects to a room. LiveKit routes the request to an available agent server, which accepts it and starts a new process to handle the job. To learn more, see [agent dispatch](https://docs.livekit.io/agents/server/agent-dispatch.md).
3. **Job**: The job initiated by your entrypoint function. This is the bulk of the code and logic you write. To learn more, see [Job lifecycle](https://docs.livekit.io/agents/server/job.md).
4. **LiveKit session close**: By default, a room is automatically closed when the last non-agent participant leaves. Any remaining agents disconnect. You can also [end the session](https://docs.livekit.io/agents/server/job.md#session-shutdown) manually.

The following diagram shows the agent server lifecycle:

![Diagram describing the functionality of agent servers](/images/agents/agents-jobs-overview.svg)

## Server features

Some additional features of agent servers include the following:

- Agent servers automatically exchange availability and capacity information with LiveKit server, enabling load balancing of incoming requests.
- Each agent server can run multiple jobs simultaneously, running each in its own process for isolation. If one crashes, it doesn't affect others running on the same agent server.
- When you deploy updates, agent servers gracefully drain active LiveKit sessions before shutting down, ensuring sessions aren't interrupted.
- If an agent disconnects from an active room unexpectedly (for example, due to an out-of-memory error or crash), LiveKit server detects the disconnection within approximately 15 seconds and automatically dispatches a new agent to the room.

---

This document was rendered at 2026-08-28T04:22:12.068Z.
For the latest version of this document, see [https://docs.livekit.io/agents/server/lifecycle.md](https://docs.livekit.io/agents/server/lifecycle.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-18"></a>
## Page 18: agents/server/agent-dispatch/
**Original URL:** https://docs.livekit.io/agents/server/agent-dispatch/  
**Source MD URL:** https://docs.livekit.io/agents/server/agent-dispatch.md

LiveKit docs › Build Agents › Agent Server › Agent dispatch

---

# Agent dispatch

> Specifying how and when your agents are assigned to rooms.

## Dispatching agents

Dispatch is the process of assigning an agent to a room. LiveKit server manages this process as part of the [Server lifecycle](https://docs.livekit.io/agents/server/lifecycle.md). LiveKit optimizes dispatch for high concurrency and low latency, typically supporting hundreds of thousands of new connections per second with a max dispatch time under 150 ms.

Explicit dispatch is the recommended approach for most applications. It gives you full control over when and how agents join rooms and lets you pass job-specific metadata to each agent session.

## Dispatch name

The dispatch name is a unique identifier for an agent. Explicit dispatch uses it to route jobs to the right agent. It's the value of `agent_name` (Python) or `agentName` (Node.js) on `@server.rtc_session()` or `ServerOptions`.

The dispatch name is distinct from the agent's **display name** (`Participant.name`), which is set by the `name` parameter in `req.accept()` and shown to other participants in the room. The dispatch name targets the agent. The display name labels it. See [Request handler](https://docs.livekit.io/agents/server/options.md#request-handler) for setting the display name.

When you scaffold an agent with [`lk agent init`](https://docs.livekit.io/reference/developer-tools/livekit-cli/agent.md#init), the AGENT-NAME you provide becomes the dispatch name in the generated source. To change it later, edit the source code and redeploy.

To set the dispatch name in your server configuration:

**Python**:

In Python, set the agent name in the `@server.rtc_session` decorator:

```python
@server.rtc_session(agent_name="test-agent")
async def my_agent(ctx: JobContext):
    # Agent entrypoint code...

```

---

**Node.js**:

```ts
const opts = new ServerOptions({
  //...
  agentName: "test-agent",
});

```

With `agent_name` set, the agent is only assigned to rooms when explicitly dispatched using one of the following methods.

## Deployments

By default, dispatching an agent targets the `production` deployment. If an agent has [non-production deployments](https://docs.livekit.io/deploy/agents/deployments.md) (for example, `staging`), use the `deployment` parameter to route the dispatch to a specific deployment. On the worker side, registration is automatic: LiveKit Cloud sets `LIVEKIT_AGENT_DEPLOYMENT` on each deployment's containers, and the SDK registers under (`agent_name`, `deployment`). To learn more, see [Deployment environment variable](https://docs.livekit.io/agents/server/options.md#deployment-env-var).

To route a session to a specific deployment, use `deployment` with `agent_name` when you dispatch an agent:

- **Dispatch via API**: `CreateAgentDispatchRequest` accepts a `deployment` field alongside `agent_name`.
- **Dispatch via token**: `RoomAgentDispatch` (inside `RoomConfiguration.agents`) accepts a `deployment` field alongside `agent_name`.
- **SIP**: room agent dispatch on a SIP rule passes `deployment` through the same `RoomAgentDispatch` field.

For example, dispatch to the `staging` deployment from a token using the CLI:

```shell
lk token create --join --open meet --agent test-agent --deployment staging

```

If your app uses the [sandbox token server](https://docs.livekit.io/frontends/build/authentication/sandbox-token-server.md) or the `useSession` hook in a client SDK, pass `deployment` as an optional argument.

## Dispatch via API

You can explicitly dispatch an agent to a room using the `AgentDispatchService` [API](https://docs.livekit.io/reference/agents/agent-dispatch-service-api.md).

**LiveKit CLI**:

```shell
lk dispatch create \
  --agent-name test-agent \
  --room my-room \
  --metadata '{"user_id": "12345"}'

```

---

**Node.js**:

```ts
import { LiveKitAPI } from 'livekit-server-sdk';

const roomName = 'my-room';
const agentName = 'test-agent';

async function createExplicitDispatch() {
  const api = new LiveKitAPI();

  // create a dispatch request for an agent named "test-agent" to join "my-room"
  const dispatch = await api.agentDispatch.createDispatch(roomName, agentName, {
    metadata: '{"user_id": "12345"}',
    // deployment: 'staging', // Optional; empty = production
  });
  console.log('created dispatch', dispatch);

  const dispatches = await api.agentDispatch.listDispatch(roomName);
  console.log(`there are ${dispatches.length} dispatches in ${roomName}`);
}

```

---

**Python**:

```python
import asyncio
from livekit import api

room_name = "my-room"
agent_name = "test-agent"

async def create_explicit_dispatch():
    async with api.LiveKitAPI() as lkapi:
        dispatch = await lkapi.agent_dispatch.create_dispatch(
            api.CreateAgentDispatchRequest(
                agent_name=agent_name,
                room=room_name,
                metadata='{"user_id": "12345"}',
                # deployment="staging",  # Optional; empty = production
            )
        )
        print("created dispatch", dispatch)

        dispatches = await lkapi.agent_dispatch.list_dispatch(room_name)
        print(f"there are {len(dispatches)} dispatches in {room_name}")

asyncio.run(create_explicit_dispatch())

```

---

**Ruby**:

```ruby
require "livekit"

room_name = "my-room"
agent_name = "test-agent"

lkapi = LiveKit::LiveKitAPI.new

dispatch = lkapi.agent_dispatch.create_dispatch(
  room_name,
  agent_name,
  metadata: '{"user_id": "12345"}',
  # deployment: "staging", # Optional; empty = production
)

puts "successfully dispatched agent #{dispatch.agent_name} to #{dispatch.room}"

```

---

**Go**:

```go
func createAgentDispatch() {
	api, err := lksdk.NewLiveKitAPI()
	if err != nil {
		panic(err)
	}

	req := &livekit.CreateAgentDispatchRequest{
		Room:      "my-room",
		AgentName: "test-agent",
		Metadata:  "{\"user_id\": \"12345\"}",
		// Deployment: "staging", // Optional; empty = production
	}
	dispatch, err := api.AgentDispatch().CreateDispatch(context.Background(), req)
	if err != nil {
		panic(err)
	}
	fmt.Printf("Dispatch created: %v\n", dispatch)
}

```

---

**Kotlin**:

```kotlin
import io.livekit.server.LiveKitAPI

val roomName = "my-room"
val agentName = "test-agent"

fun createExplicitDispatch() {
    val api = LiveKitAPI.createClient()
    val response = api.agentDispatch.createDispatch(
        room = roomName,
        agentName = agentName,
        metadata = """{"user_id": "12345"}""",
    ).execute().body()
    if (response != null) {
        println("successfully dispatched agent ${response.agentName} to ${response.room}")
    } else {
        println("failed to create dispatch")
    }
}

```

---

**Rust**:

```rust
use livekit_api::services::LiveKitApi;
use livekit_protocol::CreateAgentDispatchRequest;

let api = LiveKitApi::new("https://my-livekit-host")?;
let dispatch = api
    .agent_dispatch()
    .create_dispatch(CreateAgentDispatchRequest {
        room: "my-room".to_string(),
        agent_name: "test-agent".to_string(),
        metadata: "{\"user_id\": \"12345\"}".to_string(),
        ..Default::default()
    })
    .await?;
println!("created dispatch {:?}", dispatch);

let dispatches = api.agent_dispatch().list_dispatch("my-room").await?;
println!("there are {} dispatches in my-room", dispatches.len());

```

The room, `my-room`, is automatically created during dispatch if it doesn't already exist, and the agent server assigns `test-agent` to it.

### Job metadata

Explicit dispatch allows you to pass metadata to the agent, available in the `JobContext`. This is useful for including details such as the user's ID, name, or phone number.

The metadata field is a string, limited to 512 KiB. LiveKit recommends using JSON to pass structured data.

The [examples](#via-api) in the previous section demonstrate how to pass job metadata during dispatch.

For information on consuming job metadata in an agent, see the following guide:

- **[Job metadata](https://docs.livekit.io/agents/server/job.md#metadata)**: Learn how to consume job metadata in an agent.

## Dispatch from inbound SIP calls

Agents can be explicitly dispatched for inbound SIP calls. [SIP dispatch rules](https://docs.livekit.io/telephony/accepting-calls/dispatch-rule.md) can define one or more agents using the `room_config.agents` field.

LiveKit recommends explicit agent dispatch for SIP inbound calls rather than automatic agent dispatch as it allows multiple agents within a single project.

## Dispatch via access token

You can include one or more agent dispatch entries in a participant's access token. When the first participant connects and creates the room, LiveKit dispatches the specified agents.

> ℹ️ **Applied on room creation only**
> 
> Agent dispatch from the token only occurs when the room is first created. If the room already exists, the token's dispatch configuration is ignored. Use a unique room name per session or [dispatch via API](#via-api) for more control.

The following example creates a token that dispatches the `test-agent` agent to the `my-room` room:

**LiveKit CLI**:

The following example assumes the environment variables `LIVEKIT_API_KEY` and `LIVEKIT_API_SECRET` are set:

```shell
lk token create \
  --identity "my-participant" \
  --room "my-room" \
  --agent "test-agent" \
  --join

```

---

**Node.js**:

```ts
import { RoomAgentDispatch, RoomConfiguration } from '@livekit/protocol';
import { AccessToken } from 'livekit-server-sdk';

const roomName = 'my-room';
const agentName = 'test-agent';

async function createTokenWithAgentDispatch(): Promise<string> {
  const at = new AccessToken();
  at.identity = 'my-participant';
  at.addGrant({ roomJoin: true, room: roomName });
  at.roomConfig = new RoomConfiguration({
    agents: [
      new RoomAgentDispatch({
        agentName: agentName,
        metadata: '{"user_id": "12345"}',
        // deployment: 'staging', // Optional; empty = production
      }),
    ],
  });
  return await at.toJwt();
}

```

---

**Python**:

```python
from livekit.api import (
  AccessToken,
  RoomAgentDispatch,
  RoomConfiguration,
  VideoGrants,
)

room_name = "my-room"
agent_name = "test-agent"

def create_token_with_agent_dispatch() -> str:
    token = (
        AccessToken()
        .with_identity("my_participant")
        .with_grants(VideoGrants(room_join=True, room=room_name))
        .with_room_config(
            RoomConfiguration(
                agents=[
                    RoomAgentDispatch(
                        agent_name="test-agent",
                        metadata='{"user_id": "12345"}',
                        # deployment="staging",  # Optional; empty = production
                    )
                ],
            ),
        )
        .to_jwt()
    )
    return token

```

---

**Ruby**:

```ruby
require "livekit"

roomName = "my-room"
agentName = "test-agent"

def create_token_with_agent_dispatch(roomName:, agentName:)
  token = LiveKit::AccessToken.new(
    api_key: ENV["LIVEKIT_API_KEY"],
    api_secret: ENV["LIVEKIT_API_SECRET"],
    identity: "my-participant",
  )
  token.video_grant = LiveKit::VideoGrant.new(roomJoin: true, room: roomName)
  token.room_config = LiveKit::Proto::RoomConfiguration.new(
    agents: [
      LiveKit::Proto::RoomAgentDispatch.new(
        agent_name: agentName,
        metadata: '{"user_id": "12345"}',
        # deployment: "staging", # Optional; empty = production
      ),
    ],
  )
  token.to_jwt
end

```

---

**Go**:

```go
func createTokenWithAgentDispatch() (string, error) {
	at := auth.NewAccessToken(
		os.Getenv("LIVEKIT_API_KEY"),
		os.Getenv("LIVEKIT_API_SECRET"),
	).
		SetIdentity("my-participant").
		SetName("Participant Name").
		SetVideoGrant(&auth.VideoGrant{
			Room:     "my-room",
			RoomJoin: true,
		}).
		SetRoomConfig(&livekit.RoomConfiguration{
			Agents: []*livekit.RoomAgentDispatch{
				{
					AgentName: "test-agent",
					Metadata:  "{\"user_id\": \"12345\"}",
					// Deployment: "staging", // Optional; empty = production
				},
			},
		})

	return at.ToJWT()
}

```

---

**Kotlin**:

```kotlin
import io.livekit.server.AccessToken
import io.livekit.server.RoomJoin
import io.livekit.server.RoomName
import livekit.LivekitAgentDispatch
import livekit.LivekitRoom.RoomConfiguration

val roomName = "my-room"
val agentName = "test-agent"

fun createTokenWithAgentDispatch(): String {
    val token = AccessToken(
        System.getenv("LIVEKIT_API_KEY")!!,
        System.getenv("LIVEKIT_API_SECRET")!!,
    )
    token.identity = "my-participant"
    token.addGrants(RoomJoin(true), RoomName(roomName))
    token.roomConfiguration = RoomConfiguration.newBuilder()
        .addAgents(
            LivekitAgentDispatch.RoomAgentDispatch.newBuilder()
                .setAgentName(agentName)
                .setMetadata("""{"user_id": "12345"}""")
                // .setDeployment("staging") // Optional; empty = production
                .build(),
        )
        .build()
    return token.toJwt()
}

```

---

**Rust**:

```rust
use livekit_api::access_token::{AccessToken, VideoGrants};
use livekit_protocol::{RoomAgentDispatch, RoomConfiguration};

fn create_token_with_agent_dispatch() -> Result<String, Box<dyn std::error::Error>> {
    let token = AccessToken::with_api_key(
        &std::env::var("LIVEKIT_API_KEY")?,
        &std::env::var("LIVEKIT_API_SECRET")?,
    )
    .with_identity("my-participant")
    .with_grants(VideoGrants { room_join: true, room: "my-room".to_string(), ..Default::default() })
    .with_room_config(RoomConfiguration {
        agents: vec![RoomAgentDispatch {
            agent_name: "test-agent".to_string(),
            metadata: "{\"user_id\": \"12345\"}".to_string(),
            ..Default::default()
        }],
        ..Default::default()
    })
    .to_jwt()?;
    Ok(token)
}

```

## Automatic agent dispatch

> 🔥 **Caution**
> 
> Automatic dispatch is not recommended for most applications. It dispatches an agent to every new room, regardless of whether one is needed, and doesn't support passing metadata to the agent session. Use one of the explicit dispatch methods described in this topic instead.

When `agent_name` is not set, an agent is automatically dispatched to each new room. This can be useful for simple prototypes where every room requires the same agent.

---

This document was rendered at 2026-08-28T04:22:12.048Z.
For the latest version of this document, see [https://docs.livekit.io/agents/server/agent-dispatch.md](https://docs.livekit.io/agents/server/agent-dispatch.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-19"></a>
## Page 19: agents/server/job/
**Original URL:** https://docs.livekit.io/agents/server/job/  
**Source MD URL:** https://docs.livekit.io/agents/server/job.md

LiveKit docs › Build Agents › Agent Server › Job lifecycle

---

# Job lifecycle

> Learn more about the entrypoint function and how to end and clean up LiveKit sessions.

## Lifecycle

When an [agent server](https://docs.livekit.io/agents/server.md) accepts a job request from LiveKit Cloud, it starts a new process and runs your agent code inside. Each job runs in a separate process to isolate agents from each other. If a session instance crashes, it doesn't affect other agents running on the same agent server. The job runs until all standard and SIP participants leave the room, or you explicitly shut it down.

## Entrypoint

The entrypoint is executed as the main function of the process for each new job run by the agent server, effectively handing control over to your code. You should load any necessary app-specific data and then execute your agent's logic.

> ℹ️ **Defining the entrypoint function**
> 
> In Python, the entrypoint function is decorated with `@server.rtc_session()`. In Node.js, the entrypoint function is defined as a property of the default export of the agent file.

> ⚠️ **Default entrypoint file path**
> 
> The default Dockerfile template generated by the LiveKit CLI assumes your agent entrypoint file is at `src/agent.py` (Python) or references the `start` script in `package.json` (Node.js). If you restructure your project, update your Dockerfile and startup command to match. See [Builds and Dockerfiles](https://docs.livekit.io/deploy/agents/builds.md) for details.

You can use the entrypoint function and Agents Framework without creating an `AgentSession`. This lets you take advantage of the framework's job context and lifecycle to build a programmatic participant that's automatically dispatched to rooms. To learn more, see [Server lifecycle](https://docs.livekit.io/agents/server/lifecycle.md).

> ℹ️ **Controlling connection**
> 
> If you use `AgentSession`, it connects to LiveKit automatically when started. If you're not using `AgentSession`, or if you need to control the precise timing or method of connection (for example, to enable [end-to-end encryption](https://docs.livekit.io/transport/encryption/agents.md)), use the `JobContext` [connect method](https://docs.livekit.io/reference/python/livekit/agents/index.html.md#livekit.agents.JobContext.connect).

### Connection options

Available in:
- [ ] Node.js
- [x] Python

`single_peer_connection` determines whether the agent uses a single `RTCPeerConnection` for both publishing and subscribing instead of separate connections. It defaults to `None` (separate connections). Pass it as a keyword argument to `ctx.connect()`, set to `True` to use a single peer connection:

```python
@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
    await ctx.connect(single_peer_connection=True)

```

### Examples

This example shows a simple entrypoint function that processes incoming audio tracks and publishes a text message to the room.

**Python**:

```python
async def do_something(track: rtc.RemoteAudioTrack):
    audio_stream = rtc.AudioStream(track)
    async for event in audio_stream:
        # Do something here to process event.frame
        pass
    await audio_stream.aclose()

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
    # an rtc.Room instance from the LiveKit Python SDK
    room = ctx.room

    # set up listeners on the room before connecting
    @room.on("track_subscribed")
    def on_track_subscribed(track: rtc.Track, *_):
        if track.kind == rtc.TrackKind.KIND_AUDIO:
            asyncio.create_task(do_something(track))

    # connect to room
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # when connected, room.local_participant represents the agent
    await room.local_participant.send_text('hello world', topic='hello-world')

    # iterate through currently connected remote participants
    for rp in room.remote_participants.values():
        print(rp.identity)

```

---

**Node.js**:

```typescript
async function doSomething(track: RemoteTrack) {
  for await (const frame of new AudioStream(track)) {
    // do something with the frame
  }
}

export default defineAgent({
  entry: async (ctx: JobContext) => {
    // an rtc.Room instance from the LiveKit Node.js SDK
    const room = ctx.room;

    // set up listeners on the room before connecting
    room.on(RoomEvent.TrackSubscribed, async (track: RemoteTrack) => {
      if (track.kind === TrackKind.KIND_AUDIO) {
        doSomething(track);
      }
    });

    await ctx.connect(undefined, AutoSubscribe.AUDIO_ONLY);

    // when connected, room.localParticipant represents the agent
    await room.localParticipant?.sendText('hello world', {
      topic: 'hello-world',
    });

    // iterate through currently connected remote participants
    for (const rp of ctx.room.remoteParticipants.values()) {
      console.log(rp.identity);
    }
  },
});

```

Working examples of LiveKit Agents for Node.js are available in the [repository](https://github.com/livekit/agents-js/tree/main/examples/src).

- **[Echo Agent](https://github.com/livekit/agents/blob/main/examples/primitives/echo-agent.py)**: This programmatic participant example demonstrates how to subscribe to audio tracks and play them back to the room.

For more LiveKit Agents examples, see the [GitHub repository](https://github.com/livekit/agents/tree/main/examples).

### Publishing and receiving tracks

To learn more about publishing and receiving tracks, see the following topics.

- **[Media tracks](https://docs.livekit.io/transport/media.md)**: Use the microphone, speaker, cameras, and screen share with your agent.

- **[Realtime text and data](https://docs.livekit.io/transport/data.md)**: Use text and data channels to communicate with your agent.

- **[Processing raw media tracks](https://docs.livekit.io/transport/media/raw-tracks.md)**: Use server-side SDKs to read, process, and publish raw media tracks and files.

### Participant entrypoint function

A participant entrypoint is a callback that runs once for every participant in the room. Register it on `JobContext` to execute per-participant logic, such as looking up user data, subscribing to specific tracks, or running a long-lived task scoped to that participant, without creating an `AgentSession`.

The callback runs for participants already in the room when you call `ctx.connect()`, and for every new participant that joins after. You can register multiple entrypoints and they run concurrently for each participant.

> ℹ️ **Register before connecting**
> 
> Call `add_participant_entrypoint` (Python) or `addParticipantEntrypoint` (Node.js) before `ctx.connect()`. If you register an entrypoint after the connection is established, it fires only for participants who join afterward, not for participants already in the room.

**Python**:

```python
@server.rtc_session()
async def entrypoint(ctx: JobContext):
    async def greet_participant(ctx: JobContext, p: rtc.RemoteParticipant):
        # Access participant identity, attributes, and metadata
        logger.info(f"participant joined: {p.identity}")

        # Filter out participants you don't need to handle
        if p.identity == "some-service-bot":
            return

        # Run participant-scoped work
        await ctx.room.local_participant.send_text(
            f"Hello, {p.identity}!", topic="greeting"
        )

    async def track_participant_audio(ctx: JobContext, p: rtc.RemoteParticipant):
        # Multiple entrypoints run concurrently for each participant
        logger.info(f"tracking audio for {p.identity}")
        await asyncio.sleep(60)

    # Register entrypoints before connecting
    ctx.add_participant_entrypoint(entrypoint_fnc=greet_participant)
    ctx.add_participant_entrypoint(entrypoint_fnc=track_participant_audio)

    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)

```

---

**Node.js**:

```typescript
export default defineAgent({
  entry: async (ctx: JobContext) => {
    const greetParticipant = async (ctx: JobContext, p: RemoteParticipant) => {
      // Access participant identity, attributes, and metadata
      console.log(`participant joined: ${p.identity}`);

      // Filter out participants you don't need to handle
      if (p.identity === 'some-service-bot') {
        return;
      }

      // Run participant-scoped work
      await ctx.room.localParticipant?.sendText(
        `Hello, ${p.identity}!`, { topic: 'greeting' }
      );
    };

    const trackParticipantAudio = async (ctx: JobContext, p: RemoteParticipant) => {
      // Multiple entrypoints run concurrently for each participant
      console.log(`tracking audio for ${p.identity}`);
      await new Promise((resolve) => setTimeout(resolve, 60_000));
    };

    // Register entrypoints before connecting
    ctx.addParticipantEntrypoint(greetParticipant);
    ctx.addParticipantEntrypoint(trackParticipantAudio);

    await ctx.connect(undefined, AutoSubscribe.SUBSCRIBE_ALL);
  },
});

```

In Python, `add_participant_entrypoint` accepts a `kind` parameter to restrict which participant types trigger the callback. By default, entrypoints run for standard, SIP, and connector participants. To run only for SIP participants, for example, pass `kind=rtc.ParticipantKind.PARTICIPANT_KIND_SIP`.

## Adding custom fields to agent logs

Available in:
- [ ] Node.js
- [x] Python

Each job outputs JSON-formatted logs that include the user transcript, turn detection data, job ID, process ID, and more. You can include custom fields in the logs using `ctx.log_context_fields` for additional diagnostic context.

The following example adds worker ID and room name to the logs:

```python
@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
    ctx.log_context_fields = {
      "worker_id": ctx.worker_id,
      "room_name": ctx.room.name,
    }

```

To learn more, see the reference documentation for [JobContext.log_context_fields](https://docs.livekit.io/reference/python/livekit/agents/index.html.md#livekit.agents.JobContext.log_context_fields).

## Passing data to a job

You can customize a job with user or job-specific data using either job metadata, room metadata, or participant attributes.

### Job metadata

Job metadata is a freeform string field defined in the [dispatch request](https://docs.livekit.io/agents/server/agent-dispatch.md#via-api) and consumed in the entrypoint function. Use JSON or similar structured data to pass complex information.

Job metadata is limited to 512 KiB. For payloads that exceed this limit, see [Reference large data by ID](https://docs.livekit.io/transport/data/state/room-metadata.md#reference-large-data-by-id).

The following example assumes your agent dispatch request includes the `user_id`, `user_name`, and `user_phone` fields in the metadata. You can access this data in the entrypoint function:

**Python**:

```python
import json

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
    metadata = json.loads(ctx.job.metadata)
    user_id = metadata["user_id"]
    user_name = metadata["user_name"]
    user_phone = metadata["user_phone"]
    # ...

```

---

**Node.js**:

```typescript
export default defineAgent({
  entry: async (ctx: JobContext) => {
    const metadata = JSON.parse(ctx.job.metadata);
    const userId = metadata.user_id;
    const userName = metadata.user_name;
    const userPhone = metadata.user_phone;
    // ...
  },
});

```

For more information on dispatch, see the following article:

- **[Agent dispatch](https://docs.livekit.io/agents/server/agent-dispatch.md#via-api)**: Learn how to dispatch an agent with custom metadata.

### Room metadata and participant attributes

You can also use properties such as the room's name, metadata, and participant attributes to customize agent behavior.

> 💡 **Telephony use case**
> 
> For outbound calling agents, use `wait_for_participant` with the SIP participant's `identity` to confirm they've joined the room before starting the agent session. For a complete example including call failure handling and voicemail detection, see [Handling call outcomes](https://docs.livekit.io/telephony/making-calls/outbound-calls.md#call-outcomes).

Here's an example showing how to access various properties:

**Python**:

```python
@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
  # connect to the room
  await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

  # wait for the first participant to arrive
  participant = await ctx.wait_for_participant()

  # customize behavior based on the participant
  print(f"connected to room {ctx.room.name} with participant {participant.identity}")

  # inspect the current value of the attribute
  language = participant.attributes.get("user.language")

  # listen to when the attribute is changed
  @ctx.room.on("participant_attributes_changed")
  def on_participant_attributes_changed(changed_attrs: dict[str, str], p: rtc.Participant):
      if p == participant:
        language = p.attributes.get("user.language")
        print(f"participant {p.identity} changed language to {language}")

```

---

**Node.js**:

```typescript
export default defineAgent({
  entry: async (ctx: JobContext) => {
    // connect to the room
    await ctx.connect(undefined, AutoSubscribe.AUDIO_ONLY);

    // wait for the first participant to arrive
    const participant = await ctx.waitForParticipant();

    // customize behavior based on the participant
    console.log(`connected to room ${ctx.room.name} with participant ${participant.identity}`);

    // inspect the current value of the attribute
    let language = participant.attributes['user.language'];

    // listen to when the attribute is changed
    ctx.room.on(
      'participantAttributesChanged',
      (changedAttrs: Record<string, string>, p: Participant) => {
        if (p === participant) {
          language = p.attributes['user.language'];
          console.log(`participant ${p.identity} changed language to ${language}`);
        }
      },
    );
  },
});

```

For more information, see the following topics:

- **[Room metadata](https://docs.livekit.io/transport/data/state/room-metadata.md)**: Learn how to set and use room metadata.

- **[Participant attributes & metadata](https://docs.livekit.io/transport/data/state/participant-attributes.md)**: Learn how to set and use participant attributes and metadata.

## Ending the session

Close the session and disconnect the agent from the room using the `shutdown()` method. This method waits for queued operations to complete, commits any remaining user transcripts, and closes all I/O connections. If the `drain` parameter is `True`, the session gracefully drains pending speech before closing.

Other participants in the LiveKit room can continue. Your [shutdown hooks](#post-processing-and-cleanup) run after the `shutdown` function.

**Python**:

In Python, use the `session.shutdown()` method to gracefully close the session and disconnect the agent from the room.

```python
# Graceful shutdown with draining
session.shutdown(drain=True)

# Or immediate close
await session.aclose()

```

---

**Node.js**:

In Node.js, use the `ctx.shutdown()` method to close the session and disconnect the agent from the room.

```typescript
export default defineAgent({
  entry: async (ctx: JobContext) => {
    // do some work...

    // Graceful shutdown with draining
    ctx.shutdown(drain=true);

    // Or immediate close
    await ctx.aclose();
  },
});

```

The difference between `shutdown()` and `aclose()` is as follows:

- `agent_session.shutdown()`: Takes an optional `drain` parameter that allows you to shutdown gracefully and drain pending speech before closing. It's a non-blocking call that executes in the background. The shutdown operations happen asynchronously while your code continues executing.
- `agent_session.aclose()`: Executes the shutdown operation immediately. It's an awaitable method (async) that pauses the current coroutine execution until the close operation is finished. Your code doesn't proceed until `aclose()` completes.

After you shutdown the session, you can delete the room if it's no longer needed.

### Delete the room

You can configure the agent session to automatically delete the room on session end by setting the `delete_room_on_close` parameter to `True`. To learn more, see [Delete room when session ends](https://docs.livekit.io/agents/logic/sessions.md#delete_room_on_close).

Alternatively, you can delete the room manually. If the session should end for everyone, use the server API [deleteRoom](https://docs.livekit.io/intro/basics/rooms-participants-tracks/rooms.md#delete-a-room) to end the session. This disconnects all participants from the room.

When the room is removed from the server, a `disconnected` [room event](https://docs.livekit.io/intro/basics/rooms-participants-tracks/webhooks-events.md#sdk-events) is emitted.

**Python**:

```python
async def entrypoint(ctx: JobContext):
    # do some work
    ...

    await ctx.delete_room()

```

---

**Node.js**:

```typescript
import { LiveKitAPI } from 'livekit-server-sdk';

export default defineAgent({
  entry: async (ctx: JobContext) => {
    // do some work...

    const api = new LiveKitAPI();
    await api.room.deleteRoom(ctx.job.room.name);
  },
});

```

## Post-processing and cleanup

After a session ends, you can perform post-processing or cleanup tasks using shutdown hooks. For example, you might want to save user state in a database.

**Python**:

```python
async def entrypoint(ctx: JobContext):
    async def my_shutdown_hook():
        # save user state
        ...
    ctx.add_shutdown_callback(my_shutdown_hook)

```

---

**Node.js**:

```typescript
export default defineAgent({
  entry: async (ctx: JobContext) => {
    ctx.addShutdownCallback(() => {
      // save user state...
    });
  },
});

```

> ℹ️ **Note**
> 
> Shutdown hooks should complete within a short amount of time. By default, the framework waits 10 seconds before forcefully terminating the process. You can adjust this timeout using the `shutdown_process_timeout` parameter in [agent server options](https://docs.livekit.io/agents/server/options.md).

---

This document was rendered at 2026-08-28T04:22:12.095Z.
For the latest version of this document, see [https://docs.livekit.io/agents/server/job.md](https://docs.livekit.io/agents/server/job.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-20"></a>
## Page 20: agents/server/options/
**Original URL:** https://docs.livekit.io/agents/server/options/  
**Source MD URL:** https://docs.livekit.io/agents/server/options.md

LiveKit docs › Build Agents › Agent Server › Server options

---

# Server options

> Learn about the options available for creating an agent server.

## Options

The constructor for `AgentServer` includes some parameters for configuring the agent server. The following includes some of the available parameters. For the complete list, see the [AgentServer reference](https://docs.livekit.io/reference/python/livekit/agents/index.html.md#livekit.agents.AgentServer).

> ℹ️ **Python and Node.js differences**
> 
> In Python, the `@server.rtc_session()` decorator is used to define some options for the agent server. In Node.js, these options are set up using the `ServerOptions` class.

> 💡 **Use the quickstart first**
> 
> You can edit the agent created in the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md) to try out the code samples in this topic.

**Python**:

```python
server = AgentServer(
    # Whether the agent can subscribe to tracks, publish data, update metadata, etc.
    permissions,
    # Amount of time to wait for existing jobs to finish when SIGTERM or SIGINT is received
    drain_timeout,
    # The maximum value of load_fnc, above which no new processes will spawn
    load_threshold,
    # A function to perform any necessary initialization before the job starts.
    setup_fnc,
    # Function to determine the current load of the worker. Should return a value between 0 and 1.
    load_fnc,
    # The log level for the agent server and its job processes. Defaults to 'info'.
    log_level,
)

# start the agent server
cli.run_app(server)

```

While `AgentServer` supports the `setup_fnc` and `load_fnc` properties, LiveKit recommends assigning them directly on the `AgentServer` instance:

```python
server.setup_fnc = my_prewarm_function

```

Using setters avoids having to define initialization logic as part of the constructor and makes the server configuration easier to read and compose.

See the [Prewarm function](#prewarm) section for a complete example.

---

**Node.js**:

```ts
const opts = new ServerOptions({
  // path to the agent module, which must export a default Agent object (usually the current file)
  agent: fileURLToPath(import.meta.url),
  // the agent name, used for explicit dispatch
  agentName: 'my-agent',
  // inspect the request and decide if the current agent server should handle it.
  requestFunc,
  // whether the agent can subscribe to tracks, publish data, update metadata, etc.
  permissions,
  // milliseconds to wait for existing jobs to finish when SIGTERM or SIGINT is received
  drainTimeout,
  // the type of agent server to create, either JT_ROOM or JT_PUBLISHER. Defaults to JT_ROOM.
  serverType: JobType.JT_ROOM,
  // a function that reports the current load of the agent server. returns a value between 0-1.
  loadFunc,
  // the maximum value of loadFunc, above which agent server is marked as unavailable.
  loadThreshold,
  // the log level for the agent server and its job processes. defaults to 'info'.
  logLevel: 'info',
})

// start the agent server
cli.runApp(opts);

```

> 🔥 **Caution**
> 
> For security purposes, set the LiveKit API key and secret as environment variables rather than as `ServerOptions` parameters.

### Entrypoint function

The entrypoint function is the main function called for each new job, and is the core of your agent app. To learn more, see the [entrypoint documentation](https://docs.livekit.io/agents/server/job.md#entrypoint) in the job lifecycle topic.

**Python**:

In Python, the entrypoint function is defined using the `@server.rtc_session()` decorator on the agent function:

```python
@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
    # connect to the room

    # handle the session
    ...

```

---

**Node.js**:

In Node.js, the entrypoint function is defined as a property of the default export of the agent file:

```ts
export default defineAgent({
  entry: async (ctx: JobContext) => {
    // connect to the room
    await ctx.connect();
    // handle the session
  },
});

```

### Request handler

The `on_request` function runs each time the server has a job for the agent. The framework expects agent servers to explicitly accept or reject each job request. If the agent server accepts the request, your [entrypoint function](#entrypoint) is called. If the request is rejected, it's sent to the next available agent server. A rejection indicates that the agent server is unable to handle the job, not that the job itself is invalid. The framework simply reassigns it to another agent server.

If `on_request` is not defined, the default behavior is to automatically accept all requests dispatched to the agent server.

**Python**:

```python
async def request_fnc(req: JobRequest):
    # accept the job request
    await req.accept(
        # the agent's name (Participant.name), defaults to ""
        name="agent",
        # the agent's identity (Participant.identity), defaults to "agent-<jobid>"
        identity="identity",
        # attributes to set on the agent participant upon join
        attributes={"myagent": "rocks"},
    )

    # or reject it
    # await req.reject()

server = AgentServer()

@server.rtc_session(agent_name="my-agent", on_request=request_fnc)
async def my_agent(ctx: JobContext):
    # set up entrypoint function
    # handle the session
    ...

```

---

**Node.js**:

```ts
const requestFunc = async (req: JobRequest) => {
  // accept the job request
  await req.accept(
    // the agent's name (Participant.name), defaults to ""
    'my-agent',
    // the agent's identity (Participant.identity), defaults to "agent-<jobid>"
    'identity',
  );
};

const opts = new ServerOptions({
  requestFunc,
});

```

The `name` parameter is the agent's display name (`Participant.name`), used to identify the agent in the room. It defaults to the agent's identity, and is separate from the agent's [dispatch name](https://docs.livekit.io/agents/server/agent-dispatch.md#dispatch-name) used for explicit dispatch.

### Prewarm function

For isolation and performance reasons, the framework runs each agent job in its own process. Agents often need access to model files that take time to load. To address this, you can use a `prewarm` function to warm up the process before assigning any jobs to it. You can control the number of processes to keep warm using the `num_idle_processes` parameter.

In production, the default number of idle processes is based on the available CPU count:

- **Python**: `math.ceil(cpu_count)`
- **Node.js**: `Math.min(os.availableParallelism(), 4)`

Both SDKs read cgroup CPU limits when computing these defaults, so containers with limited CPU allocations pre-warm fewer processes than the host machine has cores. The Node.js default caps at 4 to limit memory from pre-warmed child processes on large machines. In development mode, both SDKs default to 0 (no pre-warming).

**Python**:

In Python, set the `setup_fnc` for `AgentServer` to your prewarm function:

```python
server = AgentServer()

def prewarm(proc: JobProcess):
    # load silero weights and store to process userdata
    proc.userdata["vad"] = silero.VAD.load()


server.setup_fnc = prewarm

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
    # access the loaded silero instance
    vad: silero.VAD = ctx.proc.userdata["vad"]


```

---

**Node.js**:

In Node.js, the prewarm function is defined as a property of the default export of the agent file:

```ts
export default defineAgent({
  prewarm: async (proc: JobProcess) => {
    // load silero weights and store to process userdata
    proc.userData.vad = await silero.VAD.load();
  },
  entry: async (ctx: JobContext) => {
    // access the loaded silero instance
    const vad = ctx.proc.userData.vad! as silero.VAD;
  },
});

```

> ℹ️ **The default pipeline doesn't need prewarming**
> 
> `AgentSession` provisions a bundled [Silero VAD](https://docs.livekit.io/agents/logic/turns/vad.md) automatically, so the default voice pipeline needs no prewarming. Use `prewarm` for models or other assets you load yourself that are slow to initialize.

### Agent server load

In [custom deployments](https://docs.livekit.io/deploy/custom/deployments.md), you can configure the conditions under which the agent server stops accepting new jobs through the `load_fnc` and `load_threshold` parameters.

- `load_fnc`: A function that returns the current load of the agent server as a float between 0 and 1.0.
- `load_threshold`: The maximum load value at which the agent server still accepts new jobs.

The default `load_fnc` is the agent server's average CPU utilization over a 5-second window. The default `load_threshold` is `0.7`.

**Python**:

The following example shows how to define a custom load function that limits the agent server to 9 concurrent jobs, independent of CPU usage:

```python
from livekit.agents import AgentServer

server = AgentServer(
    load_threshold=0.9,
)

def compute_load(agent_server: AgentServer) -> float:
    return min(len(agent_server.active_jobs) / 10, 1.0)

server.load_fnc=compute_load

```

---

**Node.js**:

```ts
import { type AgentServer, ServerOptions } from '@livekit/agents';

const computeLoad = (server: AgentServer): Promise<number> => {
  return Math.min(server.activeJobs.length / 10, 1.0);
};

const opts = new ServerOptions({
  agent: fileURLToPath(import.meta.url),
  loadFunc: computeLoad,
  loadThreshold: 0.9,
});

```

> ℹ️ **Not available in LiveKit Cloud**
> 
> The `load_fnc` and `load_threshold` parameters cannot be changed in LiveKit Cloud deployments.

### Health check endpoint

The agent server automatically runs a local HTTP server that serves as a health check endpoint. The health check returns a `200` status when the agent server is connected to LiveKit server and operating normally, or a `503` status if there's a problem (for example, the inference process isn't running or the server isn't connected).

The endpoint is available at the root path (`/`) of the HTTP server. By default, it listens on all network interfaces (`0.0.0.0`) on port `8081` in production mode and a random available port in development mode. No configuration is needed for most deployments.

To customize the host or port, pass the `host` and `port` parameters:

**Python**:

```python
server = AgentServer(
    host="0.0.0.0",  # default: all interfaces
    port=9090,        # default: 8081 in production, random in dev
)

```

---

**Node.js**:

```ts
const opts = new ServerOptions({
  agent: fileURLToPath(import.meta.url),
  host: '0.0.0.0',  // default: all interfaces
  port: 9090,        // default: 8081 in production, random in dev
});

```

> ℹ️ **Health checks in LiveKit Cloud**
> 
> LiveKit Cloud uses this endpoint during [rolling deployments](https://docs.livekit.io/deploy/agents/managing-deployments.md#health-checks) to verify that new agent instances are healthy before routing traffic to them.

### Drain timeout

Agent sessions are stateful and should **not** be terminated abruptly. The Agents framework supports graceful termination: when a `SIGTERM` or `SIGINT` signal is received, the agent server enters a `draining` state. In this state, it stops accepting new jobs but allows existing ones to complete, up to a configured timeout.

The `drain_timeout` (Python) or `drainTimeout` (Node.js) parameter sets the maximum time to wait for active jobs to finish. It defaults to one hour. Python takes the value in seconds and Node.js takes it in milliseconds.

### Permissions

By default, agents can both publish to and subscribe from the other participants in the same room. However, you can customize these permissions by setting the `permissions` parameter. To see the full list of parameters, see the [WorkerPermissions reference](https://docs.livekit.io/reference/python/livekit/agents/index.html.md#livekit.agents.WorkerPermissions).

**Python**:

```python
server = AgentServer(
    ...
    permissions=WorkerPermissions(
        can_publish=True,
        can_subscribe=True,
        can_publish_data=True,
        # when set to true, the agent won't be visible to others in the room.
        # when hidden, it will also not be able to publish tracks to the room as it won't be visible.
        hidden=False,
    ),
)

```

---

**Node.js**:

```ts
const opts = new ServerOptions({
  agent: fileURLToPath(import.meta.url),
  permissions: {
    canPublish: true,
    canPublishData: true,
    canPublishSources: [],
    canSubscribe: true,
    canUpdateMetadata: true,
    // when set to true, the agent won't be visible to others in the room.
    // when hidden, it will also not be able to publish tracks to the room as it won't be visible
    hidden: false,
  },
});

```

### Agent server type

You can choose to start a new instance of the agent for each room or for each publisher in the room. This can be set when you register your agent server:

**Python**:

In Python, the agent server type can be set using the `type` parameter for the `@server.rtc_session()` decorator:

```python
@server.rtc_session(agent_name="my-agent", type=ServerType.ROOM)
async def my_agent(ctx: JobContext):
    # ...

```

---

**Node.js**:

```ts
const opts = new ServerOptions({
  // path to the agent module, which must export a default Agent object
  agent: fileURLToPath(import.meta.url),
  // when omitted, the default is JobType.JT_ROOM
  serverType: JobType.JT_ROOM,
});

```

The `ServerType` enum has two options:

- `ROOM`: Create a new instance of the agent for each room.
- `PUBLISHER`: Create a new instance of the agent for each publisher in the room.

If the agent is performing resource-intensive operations in a room that could potentially include multiple publishers (for example, processing incoming video from a set of security cameras), you can set `agent server_type` to `JT_PUBLISHER` to ensure that each publisher has its own instance of the agent.

For `PUBLISHER` jobs, call the entrypoint function once for each publisher in the room. The `JobContext.publisher` object contains a `RemoteParticipant` representing that publisher.

## Starting the agent server

To spin up an agent server with the configuration defined in the `AgentServer` constructor, call the CLI:

**Python**:

```python
if __name__ == "__main__":
    cli.run_app(server)

```

---

**Node.js**:

```ts
cli.runApp(opts);

```

The Agents agent server CLI provides two subcommands: `start` and `dev`. The former outputs raw JSON data to stdout, and is recommended for production. `dev` is recommended to use for development, as it outputs human-friendly colored logs, and supports hot reloading on Python.

## Log levels

By default, your agent server and all of its job processes output logs at the `info` level or higher. Configure the log level in any of the following ways:

- Set the `LIVEKIT_LOG_LEVEL` (Python) or `LOG_LEVEL` (Node.js) environment variable.
- Pass `log_level` to `AgentServer` in Python.
- Use the `--log-level` CLI flag when starting the agent server.

The CLI flag takes precedence over the environment variable, which takes precedence over the value set in code.

### Environment variable

Set the environment variable to configure the log level without changing your code or startup command. This is useful for deployment environments where you want to adjust log verbosity without rebuilding your agent. The agent reads the variable when it starts directly, from your terminal or a `Dockerfile`:

**Python**:

```shell
LIVEKIT_LOG_LEVEL=debug uv run src/agent.py start

```

---

**Node.js**:

```shell
LOG_LEVEL=debug node dist/main.js start

```

> ℹ️ **Python log level configuration**
> 
> For Python agents, the `lk agent` commands don't read `LIVEKIT_LOG_LEVEL`. Use the `--log-level` flag with the CLI instead. Node.js agents read `LOG_LEVEL` in both cases.

You can also add it to your `.env.local` file alongside your other LiveKit credentials:

**Python**:

```shell
LIVEKIT_LOG_LEVEL=debug

```

---

**Node.js**:

```shell
LOG_LEVEL=debug

```

### Server options parameter

Available in:
- [ ] Node.js
- [x] Python

Pass `log_level` to `AgentServer` to set the log level in code:

```python
server = AgentServer(
    log_level="debug",
)

```

This applies when you start the agent server directly. The `lk agent` commands set the log level themselves, so use the `--log-level` flag with the CLI.

In Node.js, `cli.runApp` always applies its own log level, so `logLevel` in `ServerOptions` has no effect. Use the environment variable or the CLI flag instead.

### CLI flag

Pass `--log-level` when starting the agent server to override the log level at startup:

```shell
lk agent start --log-level=debug

```

### Available log levels

The following log levels are available:

- `trace`: Very detailed tracing information.
- `debug`: Detailed information for debugging.
- `info`: Default level for general information.
- `warn`: Warning messages.
- `error`: Error messages.
- `critical` (Python) or `fatal` (Node.js): Critical error messages.

## Deployment environment variable

LiveKit Cloud sets the `LIVEKIT_AGENT_DEPLOYMENT` environment variable on every agent's containers, regardless of which [deployment](https://docs.livekit.io/deploy/agents/deployments.md) it runs in. Your worker registers under the right deployment automatically — no code change is required.

The value tells you which deployment the agent is running in:

- **Production**: `LIVEKIT_AGENT_DEPLOYMENT` is set to an **empty string** (and is unset when running locally).
- **Non-production deployment**: `LIVEKIT_AGENT_DEPLOYMENT` is set to the deployment name, for example `staging`.

Use this variable to branch on the current deployment at runtime. To learn more and for example code, see [Branch on deployment name at runtime](https://docs.livekit.io/deploy/agents/deployments.md#env-var).

---

This document was rendered at 2026-08-28T04:22:12.074Z.
For the latest version of this document, see [https://docs.livekit.io/agents/server/options.md](https://docs.livekit.io/agents/server/options.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-21"></a>
## Page 21: agents/logic/tools/definition/#interruptions
**Original URL:** https://docs.livekit.io/agents/logic/tools/definition/#interruptions  
**Source MD URL:** https://docs.livekit.io/agents/logic/tools/definition.md

LiveKit docs › Build Agents › Logic & Structure › Tool definition & use › Function tools

---

# Function tools

> How to design and register custom tools for your agent.

## Overview

The LLM has access to any tools you add to your agent class. This page covers how to define them, call HTTP APIs, use RunContext, handle speech and interruptions, add tools dynamically, and surface errors.

## Tool definition

**Python**:

Add tools to your agent class with the `@function_tool` decorator.

```python
from typing import Any
from livekit.agents import function_tool, Agent, RunContext

class MyAgent(Agent):
    @function_tool()
    async def lookup_weather(
        self,
        context: RunContext,
        location: str,
    ) -> dict[str, Any]:
        """Look up weather information for a given location.

        Args:
            location: The location to look up weather information for.
        """

        return {"weather": "sunny", "temperature_f": 70}

```

---

**Node.js**:

Add tools to your agent class with the `llm.tool` function. This example uses [Zod](https://zod.dev) to make it easy to provide a typed, annotated tool definition.

```typescript
import { voice, llm } from '@livekit/agents';
import { z } from 'zod';

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  tools: [
    llm.tool({
      name: 'lookupWeather',
      description: 'Look up weather information for a given location.',
      parameters: z.object({
        location: z.string().describe("The location to look up weather information for.")
      }),
      execute: async ({ location }, { ctx }) => {
        return { weather: "sunny", temperatureF: 70 };
      },
    }),
  ],
});


```

You can also define the tool parameters as a [JSON schema](https://json-schema.org/). For example, the tool in the example above can be defined as follows:

```typescript
parameters: {
  type: "object",
  properties: {
    location: {
      type: "string",
      description: "The location to look up weather information for."
    }
  }
}

```

When using Zod, `parameters` must be a `z.object({...})` — other top-level types like `z.discriminatedUnion()` aren't supported because LLM tool-calling APIs require a JSON object. Use optional or nullable fields within the object to model variant behavior. If you use OpenAI with strict mode, prefer `.nullable()` over `.optional()`.

> 💡 **Best practices**
> 
> A good tool definition is key to reliable tool use from your LLM. Be specific about what the tool does, when it should or should not be used, what the arguments are for, and what type of return value to expect.

> ℹ️ **Note**
> 
> In Node.js, `tool`, `Agent`, and the other `voice` / `llm` exports are available directly from `@livekit/agents` (for example `import { Agent, tool } from '@livekit/agents'`), so the `voice.` / `llm.` prefixes are optional. The namespaced form shown throughout these docs works too.

### Decorator parameters

Tool decorators transform regular functions into tools the LLM can call. The `@function_tool` decorator in Python and `llm.tool()` function in Node.js accept optional parameters to control how a tool is presented to the LLM and when it's available:

**Python**:

| Parameter | Type | Default | Description |
| `name` | `str` | `None` | Override the tool name sent to the LLM. Defaults to the function name. |
| `description` | `str` | `None` | Override the tool description sent to the LLM. Defaults to the function docstring. |
| `raw_schema` | `dict` | `None` | A raw JSON function-calling schema. See [Creating tools from raw schema](#creating-tools-from-raw-schema). |
| `flags` | `ToolFlag` | `ToolFlag.NONE` | Behavior flags that control when the tool is available. See [Tool flags](#tool-flags). |

---

**Node.js**:

| Parameter | Type | Default | Description |
| `name` | `string` | — | The tool name sent to the LLM. Required. |
| `description` | `string` | — | The tool description sent to the LLM. Required. |
| `parameters` | `ZodSchema` or `JSONSchema` | — | Schema for the tool's input parameters. |
| `execute` | `Function` | — | The function called when the LLM invokes the tool. |
| `flags` | `number` | `ToolFlag.NONE` | Behavior flags that control when the tool is available. See [Tool flags](#tool-flags). |

### Tool flags

Tool flags control how a tool behaves at runtime. Set them using the `flags` parameter.

| Flag | Description |
| `NONE` | Default. No special behavior. |
| `IGNORE_ON_ENTER` | Excludes the tool from any `generate_reply` calls made inside the agent's `on_enter` method. |
| `CANCELLABLE` | Lets the LLM cancel the tool while it's running. See [Cancellation](https://docs.livekit.io/agents/logic/tools/async.md#cancellation). |

`IGNORE_ON_ENTER` is useful for tools that shouldn't be called during the agent's initial greeting. For example, a "confirm address" tool should not be available until the user has actually provided an address:

**Python**:

```python
from livekit.agents import Agent, RunContext, function_tool
from livekit.agents.llm.tool_context import ToolFlag


class AddressAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You help users provide their address.",
        )

    async def on_enter(self) -> None:
        self.session.generate_reply(
            instructions="Ask the user to provide their address."
        )

    @function_tool(flags=ToolFlag.IGNORE_ON_ENTER)
    async def confirm_address(self, ctx: RunContext) -> None:
        """Confirm the address provided by the user."""
        # This tool is NOT available during on_enter,
        # preventing the LLM from confirming before the user speaks.
        ...

```

---

**Node.js**:

```typescript
import { voice, llm } from '@livekit/agents';
import { z } from 'zod';

const addressAgent = voice.Agent.create({
  instructions: 'You help users provide their address.',
  tools: [
    llm.tool({
      name: 'confirmAddress',
      description: 'Confirm the address provided by the user.',
      flags: llm.ToolFlag.IGNORE_ON_ENTER,
      execute: async (_, { ctx }) => {
        // This tool is NOT available during onEnter,
        // preventing the LLM from confirming before the user speaks.
      },
    }),
  ],
  onEnter(ctx) {
    ctx.session.generateReply({
      instructions: 'Ask the user to provide their address.',
    });
  },
});

```

> ℹ️ **Note**
> 
> In Node.js, the `tools: [ ... ]` array syntax is preferred and is required for Toolsets and provider tools. For backward compatibility, function tools can also use the legacy object syntax (`tools: { lookupWeather: llm.tool({ ... }) }`); in that form, the object key supplies the tool name internally.

### Tool IDs

Available in:
- [x] Node.js
- [x] Python

Every tool has a stable `id` property that uniquely identifies it. For function tools, the ID defaults to the function name or the explicit `name` parameter:

**Python**:

```python
@function_tool()
async def lookup_weather(context: RunContext, location: str) -> str:
    """Look up weather for a location."""
    return "sunny"

lookup_weather.id  # "lookup_weather"

@function_tool(name="get_weather")
async def my_func(context: RunContext, location: str) -> str:
    return "sunny"

my_func.id  # "get_weather"

```

---

**Node.js**:

```typescript
const lookupWeather = llm.tool({
  name: 'lookupWeather',
  description: 'Look up weather for a location.',
  parameters: z.object({
    location: z.string(),
  }),
  execute: async ({ location }) => {
    return 'sunny';
  },
});

lookupWeather.id; // "lookupWeather"

```

For `FunctionTool` in Node.js, `id === name`. Provider tools also expose IDs so they can be added, removed, and tracked consistently. Use `agent.toolCtx.hasTool(id)` to check whether a tool is currently available. Tool names must be unique across an agent's tool context; registering two different function tools with the same name raises an error.

Tool IDs are used for deduplication when calling `update_tools()` or `updateTools()`. IDs also enable tracking tool changes in conversation history through [`AgentConfigUpdate`](#tracking-configuration-changes).

### Arguments

Tool arguments are automatically inferred from the function signature. Parameter names and type hints are sent to the LLM as part of the tool schema.

To provide additional information about arguments beyond the type hints, include it in the tool description or use `raw_schema` for full control over the [argument schema](#creating-tools-from-raw-schema).

### Return value

The tool return value is automatically converted to a string before being sent to the LLM. The LLM generates a new reply or additional tool calls based on the return value. Return `None` or nothing at all to complete the tool silently without requiring a reply from the LLM.

You can use the return value to initiate a [handoff](https://docs.livekit.io/agents/logic/agents-handoffs.md#tool-handoff) to a different Agent within a workflow. Optionally, you can return a tool result to the LLM as well. The tool call and subsequent LLM reply are completed prior to the handoff.

In Python, return a tuple that includes both the `Agent` instance and the result. If there is no tool result, you can return the new `Agent` instance by itself.

In Node.js, return an instance of `llm.handoff`, which specifies the new `Agent` instance and the tool's return value, if any.

When a handoff occurs, prompt the LLM to inform the user:

**Python**:

```python
@function_tool()
async def my_tool(context: RunContext):
    return SomeAgent(), "Transferring the user to SomeAgent"

```

---

**Node.js**:

```typescript
const myTool = llm.tool({
  name: 'myTool',
  description: 'Example tool that hands off to another agent',
  execute: async (_, { ctx }) => {
    return llm.handoff({
      agent: createSomeAgent(),
      returns: 'Transferring the user to SomeAgent',
    });
  },
});

```

### Structured output

Some LLMs can return structured JSON payloads that define behavior like TTS style separately from the spoken text.

In this example, the LLM streams a JSON object that has both TTS style directives and a spoken response. The TTS style is applied once per message and the spoken response is stripped out for downstream processing. The example contains two code blocks: the format of the JSON and the parsing logic, and an implementation example in an agent workflow.

> 💡 **Tip**
> 
> This example uses a `cast` for the LLM and TTS instances. It's specifically built to work with OpenAI (or OpenAI-compatible) APIs. Read more in the [OpenAI Structured Outputs docs](https://developers.openai.com/docs/guides/structured-outputs).

#### Core components: Definition and parsing

This code block has two components: the `ResponseEmotion` schema definition and the `process_structured_output` parsing function.

- `ResponseEmotion`: Defines the structure of the JSON object, with both the TTS style directives (`voice_instructions`) and the spoken `response`.
- `process_structured_output`: Incrementally parses the JSON object, optionally applies a callback for TTS style directives, and only streams the spoken `response`.

```python
class ResponseEmotion(TypedDict):
    voice_instructions: Annotated[
        str,
        Field(..., description="Concise TTS directive for tone, emotion, intonation, and speed"),
    ]
    response: str

async def process_structured_output(
    text: AsyncIterable[str],
    callback: Optional[Callable[[ResponseEmotion], None]] = None,
) -> AsyncIterable[str]:
    last_response = ""
    acc_text = ""
    async for chunk in text:
        acc_text += chunk
        try:
            resp: ResponseEmotion = from_json(acc_text, allow_partial="trailing-strings")
        except ValueError:
            continue

        if callback:
            callback(resp)

        if not resp.get("response"):
            continue

        new_delta = resp["response"][len(last_response) :]
        if new_delta:
            yield new_delta
        last_response = resp["response"]

```

#### Agent method implementation

This agent implementation example overrides default behavior with custom logic using the LLM and TTS nodes: [`llm_node`](https://docs.livekit.io/agents/build/nodes.md#llm_node) and [`tts_node`](https://docs.livekit.io/agents/build/nodes.md#tts_node).

- `llm_node`: Casts the LLM instance to the OpenAI type, streams the output using the `ResponseEmotion` schema, and parses it into structured JSON.
- `tts_node`: Processes the streamed JSON with a callback that applies the TTS style directives (`voice_instructions`), then streams the audio from the `response`.

```python
async def llm_node(
    self, chat_ctx: ChatContext, tools: list[FunctionTool], model_settings: ModelSettings
):
    # not all LLMs support structured output, so we need to cast to the specific LLM type
    llm = cast(openai.LLM, self.llm)
    tool_choice = model_settings.tool_choice if model_settings else NOT_GIVEN
    async with llm.chat(
        chat_ctx=chat_ctx,
        tools=tools,
        tool_choice=tool_choice,
        response_format=ResponseEmotion,
    ) as stream:
        async for chunk in stream:
            yield chunk

async def tts_node(self, text: AsyncIterable[str], model_settings: ModelSettings):
    instruction_updated = False

    def output_processed(resp: ResponseEmotion):
        nonlocal instruction_updated
        if resp.get("voice_instructions") and resp.get("response") and not instruction_updated:
            # when the response isn't empty, we can assume voice_instructions is complete.
            # (if the LLM sent the fields in the right order)
            instruction_updated = True
            logger.info(
                f"Applying TTS instructions before generating response audio: "
                f'"{resp["voice_instructions"]}"'
            )

            tts = cast(openai.TTS, self.tts)
            tts.update_options(instructions=resp["voice_instructions"])

    # process_structured_output strips the TTS instructions and only synthesizes the verbal part
    # of the LLM output
    return Agent.default.tts_node(
        self, process_structured_output(text, callback=output_processed), model_settings
    )

```

### RunContext

Tools include support for a special `context` argument. This contains access to the current `session`, `function_call`, `speech_handle`, and `userdata`. Consult the documentation on [speech](https://docs.livekit.io/agents/build/audio.md) and [state within workflows](https://docs.livekit.io/agents/logic/workflows.md) for more information about how to use these features.

### Using speech in tool calls

You can generate agent speech from within a tool using `session.say()` or `session.generate_reply()` like normal. Use `ctx.wait_for_playout()` to wait for any pre-tool speech to finish.

**Python**:

```python
@function_tool()
async def process_order(self, context: RunContext, order_id: str):
    """Process an order and notify the user."""

    # Generate speech and await it
    await self.session.generate_reply(
        instructions=f"Processing order {order_id}. This may take a moment."
    )

    # Now perform the actual order processing
    result = await process_order_internal(order_id)
    return result

```

---

**Node.js**:

```typescript
const processOrder = llm.tool({
  name: 'processOrder',
  description: 'Process an order and notify the user.',
  parameters: z.object({
    orderId: z.string(),
  }),
  execute: async ({ orderId }, { ctx }) => {
    // Notify the user and wait for speech to finish
    await ctx.session.generateReply({
      instructions: `Processing order ${orderId}. This may take a moment.`,
    });

    // Now perform the actual order processing
    const result = await processOrderInternal(orderId);
    return result;
  },
});

```

### Interruptions

By default, tools can be interrupted if the user speaks. A tool continues running in the background until it returns; interrupting the agent doesn't cancel the work.

A tool that finishes before the interruption keeps both the call and the result in the chat history, so the model doesn't call it again on the next turn. Recording the result doesn't prompt a reply, so the agent doesn't speak.

An interrupted agent handoff never takes effect, and the two SDKs record the interruption differently. Python keeps the call and answers it with an error. Node.js removes the call from the chat history. In neither case does the agent switch.

This default works for most tools. For a tool that blocks the agent's turn (for example, a tool whose result the agent must wait for before responding), you can either handle the interruption by canceling in-flight work when the user speaks, or prevent the interruption by keeping the tool running and the agent engaged for actions that can't be rolled back.

> 💡 **Tip**
> 
> For work that takes more than a few seconds, don't block the turn at all. Use an [async tool](https://docs.livekit.io/agents/logic/tools/async.md) so the agent can keep talking and send progress updates while the tool runs.

#### Handle interruptions

To regain control when the user interrupts so you can cancel your in-flight work instead of letting it finish: in Python, call `speech_handle.wait_if_not_interrupted()` to wait for your task, then check `speech_handle.interrupted` to decide whether to return the result or cancel it. In Node.js, use the `abortSignal` passed to `execute`, which is aborted when the tool is interrupted. Forward it to your async work so the work is cancelled too. Both approaches suit a short, read-only lookup whose result the agent needs before it can respond, such as checking an order status or account balance:

**Python**:

```python
import asyncio

from livekit.agents import Agent, RunContext, function_tool


class MyAgent(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a voice agent.")

    @function_tool
    async def get_order_status(self, order_id: str, run_ctx: RunContext) -> str | None:
        """Look up the status of an order when the user asks about it.

        Args:
            order_id: The ID of the order to look up.
        """
        # Start the lookup and wait for it to finish or be interrupted
        wait_for_result = asyncio.ensure_future(self._lookup_order(order_id))
        await run_ctx.speech_handle.wait_if_not_interrupted([wait_for_result])

        if run_ctx.speech_handle.interrupted:
            # The user spoke first: cancel the lookup and skip the reply by returning None.
            # Returning None records an empty result for the call and asks for no reply.
            wait_for_result.cancel()
            return None

        # The lookup finished without interruption: return its result to the LLM
        return wait_for_result.result()

    async def _lookup_order(self, order_id: str) -> str:
        # Simulate a short lookup, such as a database or API query
        await asyncio.sleep(2)
        return f"Order {order_id} shipped and arrives tomorrow"

```

---

**Node.js**:

```typescript
const getOrderStatus = llm.tool({
  name: 'getOrderStatus',
  description: 'Look up the status of an order when the user asks about it.',
  parameters: z.object({ orderId: z.string() }),
  execute: async ({ orderId }, { abortSignal }) => {
    // The abortSignal is aborted if the user interrupts. Forwarding it to
    // fetch cancels the request instead of letting it run to completion.
    const response = await fetch(
      `https://api.example.com/orders/${encodeURIComponent(orderId)}`,
      { signal: abortSignal },
    );
    return await response.json();
  },
});

```

In Python, because the work isn't canceled for you, cancel it explicitly when an interruption occurs, as the example does before returning `None`. Otherwise the lookup runs to completion in the background after the tool has returned `None`, and produces a result that can no longer reach the agent. In Node.js, the `abortSignal` is always provided, so you don't need to guard it with `if (abortSignal)`. It's currently aborted only on the main voice pipeline. Tool calls on other paths receive a signal that never aborts.

#### Prevent interruptions

If your tool takes external actions that can't be rolled back, disable interruptions by calling `run_ctx.disallow_interruptions()` (Python) or `ctx.disallowInterruptions()` (Node.js) at the start of your tool so user speech won't interrupt the agent's task.

For best practices on providing feedback to the user during long-running tool calls, see the section on [user feedback](https://docs.livekit.io/agents/build/external-data.md#user-feedback) in the External data and RAG guide.

To play a pre-synthesized hold message (such as "let me check that for you") while a tool executes, see [Using cached TTS in a tool call](https://docs.livekit.io/agents/multimodality/audio/customization.md#cached-tts-in-tools). This avoids TTS latency during tool execution and lets you cancel the message early if the external API returns quickly.

### Calling HTTP APIs

Most tools call an external HTTP API to fetch data or trigger actions. In Python, use the shared `aiohttp` session described below. In Node.js, use the built-in `fetch` API.

#### Best practices

Keep these recommendations in mind when calling external APIs from tools:

- **Reuse the shared HTTP session (Python).** Call `utils.http_context.http_session()` to get a shared session that's bound to the job, pools and reuses connections across calls, and closes automatically when the job ends. Outside a job context (tests or scripts), it raises `RuntimeError`. Wrap that code in `async with utils.http_context.open():` or pass your own session. (Node.js needs no equivalent: the global `fetch` already reuses connections.)
- **Disable interruptions for mutating calls.** By default, tools can be [interrupted](#interruptions) by user speech. For read-only requests this is fine, because a completed lookup keeps its result in the chat history. But if your tool writes data (placing an order, scheduling an appointment, sending a message), an interruption can leave the operation partially complete with no way to roll back. Call `context.disallow_interruptions()` (Python) or `ctx.disallowInterruptions()` (Node.js) at the start of any tool that mutates external state.
- **Raise `ToolError` on failure.** This returns the error message to the LLM so it can inform the user rather than crashing the tool. See [error handling](#error-handling) for more details.
- **Store credentials in environment variables.** For APIs that require authentication, pass headers to your request and load API keys from environment variables rather than hard-coding them.
- **Set timeouts.** External services can be slow or unresponsive. Set explicit timeouts on your HTTP requests to avoid blocking the agent indefinitely. See the section on [user feedback](https://docs.livekit.io/agents/build/external-data.md#user-feedback) for ways to keep the user informed during long-running calls.

#### Example: Fetching data from an API

The following example defines a tool that fetches a realtime stock quote from an external API. The tool takes a ticker symbol as input, makes a GET request, and returns structured data to the LLM:

**Python**:

```python
from livekit.agents import Agent, RunContext, function_tool, utils
from livekit.agents.llm import ToolError

class StockAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a helpful stock market assistant.",
        )

    @function_tool()
    async def get_stock_price(
        self,
        context: RunContext,
        symbol: str,
    ) -> dict:
        """Get the current stock price for a given ticker symbol.

        Args:
            symbol: The stock ticker symbol, for example AAPL or GOOGL.
        """
        url = f"https://livekit-stock-api.vercel.app/api/quote?symbol={symbol}"
        session = utils.http_context.http_session()
        async with session.get(url) as response:
            if response.status != 200:
                raise ToolError(f"Could not fetch stock price for {symbol}.")
            data = await response.json()
            return {
                "symbol": data["symbol"],
                "price": data["price"],
                "volume": data["volume"],
                "latest_trading_day": data["latestTradingDay"],
            }

```

---

**Node.js**:

```typescript
import { voice, llm } from '@livekit/agents';
import { z } from 'zod';

const stockAgent = voice.Agent.create({
  instructions: 'You are a helpful stock market assistant.',
  tools: [
    llm.tool({
      name: 'getStockPrice',
      description: 'Get the current stock price for a given ticker symbol.',
      parameters: z.object({
        symbol: z.string().describe('The stock ticker symbol, for example AAPL or GOOGL.'),
      }),
      execute: async ({ symbol }) => {
        const url = `https://livekit-stock-api.vercel.app/api/quote?symbol=${encodeURIComponent(symbol)}`;
        const response = await fetch(url);
        if (!response.ok) {
          throw new llm.ToolError(`Could not fetch stock price for ${symbol}.`);
        }
        const data = await response.json();
        return {
          symbol: data.symbol,
          price: data.price,
          volume: data.volume,
          latestTradingDay: data.latestTradingDay,
        };
      },
    }),
  ],
});

```

#### Example: Mutating an external API

When a tool performs a write operation such as placing an order or updating a record, disable interruptions to prevent partial execution:

**Python**:

```python
@function_tool()
async def place_order(
    self,
    context: RunContext,
    item: str,
    quantity: int,
) -> str:
    """Place an order for an item.

    Args:
        item: The item to order.
        quantity: The number of items to order.
    """
    # Prevent user speech from interrupting this tool mid-request
    context.disallow_interruptions()

    session = utils.http_context.http_session()
    async with session.post(
        "https://api.example.com/orders",
        json={"item": item, "quantity": quantity},
        headers={"Authorization": f"Bearer {os.environ['API_KEY']}"},
    ) as response:
        if response.status != 201:
            raise ToolError("Failed to place order. Please try again.")
        data = await response.json()
        return f"Order {data['order_id']} placed successfully."

```

---

**Node.js**:

```typescript
const placeOrder = llm.tool({
  name: 'placeOrder',
  description: 'Place an order for an item.',
  parameters: z.object({
    item: z.string().describe('The item to order.'),
    quantity: z.number().describe('The number of items to order.'),
  }),
  execute: async ({ item, quantity }, { ctx }) => {
    // Prevent user speech from interrupting this tool mid-request
    ctx.disallowInterruptions();

    const response = await fetch('https://api.example.com/orders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.API_KEY}`,
      },
      body: JSON.stringify({ item, quantity }),
    });
    if (!response.ok) {
      throw new llm.ToolError('Failed to place order. Please try again.');
    }
    const data = await response.json();
    return `Order ${data.orderId} placed successfully.`;
  },
});

```

### Adding tools dynamically

You can exercise more control over the tools available by setting the `tools` argument directly.

To share a tool between multiple agents, define it outside of their class and then provide it to each. The `RunContext` is especially useful for this purpose to access the current session, agent, and state.

Tools set in the `tools` value are available alongside any registered within the class using the `@function_tool` decorator.

**Python**:

```python
from livekit.agents import function_tool, Agent, RunContext

@function_tool()
async def lookup_user(
    context: RunContext,
    user_id: str,
) -> dict:
    """Look up a user's information by ID."""

    return {"name": "John Doe", "email": "john.doe@example.com"}


class AgentA(Agent):
    def __init__(self):
        super().__init__(
            tools=[lookup_user],
            # ...
        )


class AgentB(Agent):
    def __init__(self):
        super().__init__(
            tools=[lookup_user],
            # ...
        )

```

---

**Node.js**:

```typescript
import { voice, llm } from '@livekit/agents';
import { z } from 'zod';

const lookupUser = llm.tool({
  name: 'lookupUser',
  description: 'Look up a user\'s information by ID.',
  parameters: z.object({
    userId: z.string(),
  }),
  execute: async ({ userId }, { ctx }) => {
    return { name: "John Doe", email: "john.doe@example.com" };
  },
});

const agentA = voice.Agent.create({
  tools: [lookupUser],
  // ...
});

const agentB = voice.Agent.create({
  tools: [lookupUser],
  // ...
});

```

Use `agent.update_tools()` (Python) or `agent.updateTools()` (Node.js) to update available tools after creating an agent. This replaces _all_ tools, including those registered automatically within the agent class. To reference existing tools before replacement, access `agent.tools` in Python or `agent.toolCtx.tools` in Node.js:

**Python**:

```python
# add a tool
await agent.update_tools(agent.tools + [tool_a])

# remove a tool
await agent.update_tools([t for t in agent.tools if t.id != tool_a.id])

# replace all tools
await agent.update_tools([tool_a, tool_b])

```

---

**Node.js**:

```typescript
// add a tool
await agent.updateTools([...agent.toolCtx.tools, toolA])

// remove a tool
await agent.updateTools(agent.toolCtx.tools.filter((t) => t.id !== 'toolA'))

// replace all tools
await agent.updateTools([toolA, toolB])

```

### Creating tools programmatically

To create a tool on the fly, use `function_tool` as a function rather than as a decorator. You must supply a name, description, and callable function. This is useful to compose specific tools based on the same underlying code or load them from external sources such as a database or Model Context Protocol (MCP) server.

In the following example, the app has a single function to set any user profile field but gives the agent one tool per field for improved reliability:

**Python**:

```python
from livekit.agents import function_tool, RunContext

class Assistant(Agent):
    def _set_profile_field_func_for(self, field: str):
        async def set_value(context: RunContext, value: str):
            # custom logic to set input
            return f"field {field} was set to {value}"

        return set_value

    def __init__(self):
        super().__init__(
            tools=[
                function_tool(self._set_profile_field_func_for("phone"),
                              name="set_phone_number",
                              description="Call this function when user has provided their phone number."),
                function_tool(self._set_profile_field_func_for("email"),
                              name="set_email",
                              description="Call this function when user has provided their email."),
                # ... other tools ...
            ],
            # instructions, etc ...
        )

```

---

**Node.js**:

```typescript
import { voice, llm } from '@livekit/agents';
import { z } from 'zod';

function createSetProfileFieldTool(name: string, field: string) {
  return llm.tool({
    name,
    description: `Call this function when user has provided their ${field}.`,
    parameters: z.object({
      value: z.string().describe(`The ${field} value to set`),
    }),
    execute: async ({ value }, { ctx }) => {
      // custom logic to set input
      return `field ${field} was set to ${value}`;
    },
  });
}

const assistant = voice.Agent.create({
  tools: [
    createSetProfileFieldTool('setPhoneNumber', 'phone number'),
    createSetProfileFieldTool('setEmail', 'email'),
    // ... other tools ...
  ],
  // instructions, etc ...
});

```

### Creating tools from raw schema

For advanced use cases, you can create tools directly from a [raw function calling schema](https://developers.openai.com/docs/guides/function-calling?api-mode=responses). This is useful when integrating with existing function definitions, loading tools from external sources, or working with schemas that don't map cleanly to Python function signatures.

Use the `raw_schema` parameter in the `@function_tool` decorator to provide the full function schema:

**Python**:

```python
from livekit.agents import function_tool, RunContext

raw_schema = {
    "type": "function",
    "name": "get_weather",
    "description": "Get weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country e.g. New York"
            }
        },
        "required": [
            "location"
        ],
        "additionalProperties": False
    }
}

@function_tool(raw_schema=raw_schema)
async def get_weather(raw_arguments: dict[str, object], context: RunContext):
    location = raw_arguments["location"]

    # Your implementation here
    return f"The weather of {location} is ..."

```

---

**Node.js**:

```typescript
import { voice, llm } from '@livekit/agents';

const rawSchema = {
  type: 'object',
  properties: {
    location: {
      type: 'string',
      description: 'City and country e.g. New York'
    }
  },
  required: ['location'],
  additionalProperties: false
};

const getWeather = llm.tool({
  name: 'getWeather',
  description: 'Get weather for a given location.',
  parameters: rawSchema,
  execute: async ({ location }, { ctx }) => {
    // Your implementation here
    return `The weather of ${location} is ...`;
  },
});

```

When using raw schemas, function parameters are passed to your handler as a dictionary named `raw_arguments`. You can extract values from this dictionary using the parameter names defined in your schema.

You can also create tools programmatically using `function_tool` as a function with raw schemas:

**Python**:

```python
from livekit.agents import function_tool

def create_database_tool(table_name: str, operation: str):
    schema = {
        "type": "function",
        "name": f"{operation}_{table_name}",
        "description": f"Perform {operation} operation on {table_name} table",
        "parameters": {
            "type": "object",
            "properties": {
                "record_id": {
                    "type": "string",
                    "description": f"ID of the record to {operation}"
                }
            },
            "required": ["record_id"]
        }
    }

    async def handler(raw_arguments: dict[str, object], context: RunContext):
        record_id = raw_arguments["record_id"]
        # Perform database operation
        return f"Performed {operation} on {table_name} for record {record_id}"

    return function_tool(handler, raw_schema=schema)

# Create tools dynamically
user_tools = [
    create_database_tool("users", "read"),
    create_database_tool("users", "update"),
    create_database_tool("users", "delete")
]

class DataAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a database assistant.",
            tools=user_tools,
        )

```

---

**Node.js**:

```typescript
import { voice, llm } from '@livekit/agents';
import { z } from 'zod';

function createDatabaseTool(name: string, tableName: string, operation: string) {
  return llm.tool({
    name,
    description: `Perform ${operation} operation on ${tableName} table`,
    parameters: z.object({
      recordId: z.string().describe(`ID of the record to ${operation}`),
    }),
    execute: async ({ recordId }, { ctx }) => {
      // Perform database operation
      return `Performed ${operation} on ${tableName} for record ${recordId}`;
    },
  });
}

// Create tools dynamically
const dataAgent = voice.Agent.create({
  instructions: 'You are a database assistant.',
  tools: [
    createDatabaseTool('readUsers', 'users', 'read'),
    createDatabaseTool('updateUsers', 'users', 'update'),
    createDatabaseTool('deleteUsers', 'users', 'delete'),
  ],
});

```

## Toolsets

To bundle related tools under a single ID and add or remove them as a group, use a [Toolset](https://docs.livekit.io/agents/logic/tools/toolsets.md). Python also includes the built-in [MCPToolset](https://docs.livekit.io/agents/logic/tools/mcp.md) and beta `ToolSearchToolset` and `ToolProxyToolset` for [dynamic tool discovery](https://docs.livekit.io/agents/logic/tools/toolsets.md#dynamic-tool-discovery), which are built on this primitive.

## Tracking configuration changes

Available in:
- [x] Node.js
- [x] Python

When an agent starts with configured tools or instructions, or when you update an agent's tools or instructions at runtime, an `AgentConfigUpdate` is automatically added to the conversation history. This record includes:

- **`instructions`**: The updated instructions, if changed.
- **`tools_added` / `toolsAdded`**: Names of any tools that were added.
- **`tools_removed` / `toolsRemoved`**: Names of any tools that were removed.

**Python**:

```python
# Tool changes are tracked automatically
await agent.update_tools([new_tool_a, new_tool_b])

# Instruction changes are also tracked
await agent.update_instructions("You are now a support agent.")

```

---

**Node.js**:

```typescript
// Tool changes are tracked automatically
await agent.updateTools([newToolA, newToolB]);

// Instruction changes are also tracked
await agent.updateInstructions('You are now a support agent.');

```

This gives the LLM visibility into configuration changes, which is useful in [multi-agent workflows](https://docs.livekit.io/agents/logic/workflows.md) where agents switch and have different tool sets. For example, after the calls above, the conversation history includes records like:

**Python**:

```python
# agent.chat_ctx.items
[
    ChatMessage(role="user", content=["What's the weather?"]),
    ChatMessage(role="assistant", content=["Let me check..."]),
    AgentConfigUpdate(
        tools_added=["new_tool_a", "new_tool_b"],
        tools_removed=["old_tool"],
    ),
    AgentConfigUpdate(
        instructions="You are now a support agent.",
    ),
]

```

---

**Node.js**:

```typescript
const configUpdates = session.history.items.filter(
  (item) => item.type === 'agent_config_update',
);

for (const item of configUpdates) {
  console.log(item.toolsAdded, item.toolsRemoved, item.instructions);
}

```

To exclude configuration updates when copying or serializing conversation history, use `exclude_config_update` (Python) or `excludeConfigUpdate` (Node.js):

**Python**:

```python
ctx_copy = chat_ctx.copy(exclude_config_update=True)

```

---

**Node.js**:

```typescript
const ctxCopy = chatCtx.copy({ excludeConfigUpdate: true });

```

## Error handling

Raise the `ToolError` exception to return an error to the LLM in place of a response. You can include a custom message to describe the error and/or recovery options.

**Python**:

```python
@function_tool()
async def lookup_weather(
    self,
    context: RunContext,
    location: str,
) -> dict:
    if location == "mars":
        raise ToolError("This location is coming soon. Please join our mailing list to stay updated.")
    else:
        return {"weather": "sunny", "temperature_f": 70}

```

---

**Node.js**:

```typescript
import { llm } from '@livekit/agents';
import { z } from 'zod';

const lookupWeather = llm.tool({
  name: 'lookupWeather',
  description: 'Look up weather information for a location',
  parameters: z.object({
    location: z.string().describe('The location to get weather for'),
  }),
  execute: async ({ location }, { ctx }) => {
    if (location === "mars") {
      throw new llm.ToolError("This location is coming soon. Please join our mailing list to stay updated.");
    }
    return { weather: "sunny", temperatureF: 70 };
  },
});

```

If a tool raises an unexpected exception, the framework returns a generic internal-error message to the LLM instead, so server-side details don't leak into the conversation. It still logs the original error for you to debug.

If the LLM calls a tool with arguments that fail parsing or schema validation, the framework forwards the failure to the LLM as a `ToolError`, including the tool name and the validator's message. The LLM can correct the call and retry without any handling on your part.

---

This document was rendered at 2026-08-28T04:22:12.401Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/tools/definition.md](https://docs.livekit.io/agents/logic/tools/definition.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-22"></a>
## Page 22: agents/logic/tools/toolsets/
**Original URL:** https://docs.livekit.io/agents/logic/tools/toolsets/  
**Source MD URL:** https://docs.livekit.io/agents/logic/tools/toolsets.md

LiveKit docs › Build Agents › Logic & Structure › Tool definition & use › Toolsets

---

# Toolsets

> Group related tools and add or remove them as a unit.

Available in:
- [x] Node.js
- [x] Python

## Overview

A `Toolset` bundles related tools under a single ID so you can add or remove them as a group.

**Python**:

Pass a list of tools to the `Toolset` constructor:

```python
from livekit.agents import Agent, function_tool, RunContext
from livekit.agents.llm import Toolset

@function_tool()
async def lookup_user(context: RunContext, user_id: str) -> dict:
    """Look up a user by ID."""
    return {"name": "Jane Doe", "email": "jane@example.com"}

@function_tool()
async def update_user(context: RunContext, user_id: str, email: str) -> str:
    """Update a user's email address."""
    return f"Updated email for {user_id}."

class MyAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a helpful assistant.",
            tools=[
                Toolset(id="user-management", tools=[lookup_user, update_user])
            ],
        )

```

---

**Node.js**:

Pass an array of tools to the `Toolset` constructor:

```typescript
import { llm, voice } from '@livekit/agents';
import { z } from 'zod';

const lookupUser = llm.tool({
  name: 'lookupUser',
  description: 'Look up a user by ID.',
  parameters: z.object({ userId: z.string() }),
  execute: async ({ userId }) => {
    return { name: 'Jane Doe', email: 'jane@example.com' };
  },
});

const updateUser = llm.tool({
  name: 'updateUser',
  description: "Update a user's email address.",
  parameters: z.object({ userId: z.string(), email: z.string() }),
  execute: async ({ userId }) => {
    return `Updated email for ${userId}.`;
  },
});

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  tools: [new llm.Toolset({ id: 'user-management', tools: [lookupUser, updateUser] })],
});

```

Toolsets are flattened automatically when sent to the LLM. You can add or remove a toolset as a group using `update_tools()` in Python or `updateTools()` in Node.js. In Node.js, `llm.isToolset(value)` checks whether a value is a toolset.

> ℹ️ **Note**
> 
> Tool names must be unique across all tools and toolsets. If a toolset and a standalone tool, or two toolsets, share a tool with the same name, the agent raises an error.

## Custom toolsets

Use a custom toolset when you need custom initialization, teardown, or dynamic tool loading. Setup and close hooks are called automatically by `AgentSession`.

**Python**:

Subclass `Toolset` and override `setup()` and `aclose()`:

```python
from livekit.agents import Agent, RunContext, function_tool
from livekit.agents.llm import Toolset
from typing_extensions import Self

class WeatherToolset(Toolset):
    def __init__(self):
        super().__init__(id="weather_tools")

        self._lookup = function_tool(
            self._lookup_weather,
            name="lookup_weather",
            description="Look up current weather for a location.",
        )
        self._forecast = function_tool(
            self._get_forecast,
            name="get_forecast",
            description="Get a multi-day weather forecast.",
        )
        self._tools = [self._lookup, self._forecast]

    async def setup(self) -> Self:
        await super().setup()
        # initialize external connections, load config, etc.
        return self

    async def aclose(self) -> None:
        await super().aclose()
        # close connections, release resources

    async def _lookup_weather(self, context: RunContext, location: str) -> str:
        return f"The weather in {location} is sunny."

    async def _get_forecast(
        self, context: RunContext, location: str, days: int = 3
    ) -> str:
        return f"{days}-day forecast for {location}: sunny."


class MyAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a helpful weather assistant.",
            tools=[WeatherToolset()],
        )

```

---

**Node.js**:

Use `llm.Toolset.create()` with `setup` and `aclose` hooks:

```typescript
import { llm, voice } from '@livekit/agents';
import { z } from 'zod';

const lookupWeather = llm.tool({
  name: 'lookupWeather',
  description: 'Look up current weather for a location.',
  parameters: z.object({ location: z.string() }),
  execute: async ({ location }) => {
    return `The weather in ${location} is sunny.`;
  },
});

const getForecast = llm.tool({
  name: 'getForecast',
  description: 'Get a multi-day weather forecast.',
  parameters: z.object({ location: z.string(), days: z.number().default(3) }),
  execute: async ({ location, days }) => {
    return `${days}-day forecast for ${location}: sunny.`;
  },
});

const weatherToolset = llm.Toolset.create({
  id: 'weather_tools',
  tools: [],
  setup: async (ctx) => {
    // initialize external connections, load config, etc.
    ctx.updateTools([lookupWeather, getForecast]);
  },
  aclose: async () => {
    // close connections, release resources
  },
});

const agent = voice.Agent.create({
  instructions: 'You are a helpful weather assistant.',
  tools: [weatherToolset],
});

```

The built-in [MCP Toolset](https://docs.livekit.io/agents/logic/tools/mcp.md) is Python-specific. It connects to an MCP server on `setup()` and disconnects on `aclose()`.

## Dynamic tool discovery

Available in (BETA):
- [ ] Node.js
- [x] Python

Agents with many tools can suffer from degraded LLM accuracy and wasted tokens. Dynamic tool discovery solves this by loading tool definitions on demand instead of all at once. Two kinds of toolsets are available:

- `ToolSearchToolset` exposes a single `tool_search` function. When the LLM calls it, matching tools are added to the LLM's native tool list for the next turn. May be simpler for the model to understand.
- `ToolProxyToolset` exposes exactly two fixed tools, `tool_search` and `call_tool`. The tool list never changes, so providers like OpenAI and Anthropic can reuse their prompt cache across turns. May be better for many tools or cost-sensitive workloads.

Both accept toolsets (including `MCPToolset`), function tools, and standalone tools:

```python
from livekit.agents import Agent, RunContext, function_tool
from livekit.agents.beta.toolsets import ToolProxyToolset
from livekit.agents.llm import Toolset

class WeatherToolset(Toolset):
    def __init__(self):
        super().__init__(id="weather")

    @function_tool()
    async def get_weather(self, context: RunContext, location: str) -> str:
        """Get current weather for a location."""
        return f"Sunny, 72F in {location}"

class FlightToolset(Toolset):
    def __init__(self):
        super().__init__(id="flights")

    @function_tool()
    async def search_flights(self, context: RunContext, origin: str, destination: str) -> str:
        """Search for available flights."""
        return f"Found 3 flights from {origin} to {destination}"

@function_tool()
async def convert_currency(context: RunContext, amount: float, code: str) -> str:
    """Convert an amount to the given currency code."""
    return f"{amount} converted to {code}"

class TravelAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a travel planning assistant. Use tool_search to find the right tools.",
            tools=[
                ToolProxyToolset(
                    id="travel_tools",
                    tools=[
                        WeatherToolset(),
                        FlightToolset(),
                        convert_currency,
                    ],
                    max_results=3,
                )
            ],
        )

```

Swap `ToolProxyToolset` for `ToolSearchToolset` to use native tool calls instead of the proxy pattern. Both classes share the same core arguments.

The default search strategy uses BM25 ranking, which returns tools ordered by relevance to the query rather than by literal pattern match. For simpler regex-based matching, pass a `KeywordSearchStrategy`:

```python
from livekit.agents.beta.toolsets.tool_search import KeywordSearchStrategy

toolset = ToolProxyToolset(
    id="my_tools",
    tools=[...],
    search_strategy=KeywordSearchStrategy(),
)

```

You can also implement your own strategy by conforming to the `SearchStrategy` protocol.

## Additional resources

The following articles provide more information about the topics discussed in this guide:

- **[Function tools](https://docs.livekit.io/agents/logic/tools/definition.md)**: Define individual tools with decorators, RunContext, and dynamic registration.

- **[Async tools](https://docs.livekit.io/agents/logic/tools/async.md)**: Run long-running tools in the background so the agent can keep talking.

- **[Model Context Protocol (MCP)](https://docs.livekit.io/agents/logic/tools/mcp.md)**: Use `MCPToolset` to expose tools from an MCP server to your agent.

- **[Workflows](https://docs.livekit.io/agents/logic/workflows.md)**: Hand off control between agents that each carry their own toolsets.

---

This document was rendered at 2026-08-28T04:22:13.003Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/tools/toolsets.md](https://docs.livekit.io/agents/logic/tools/toolsets.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-23"></a>
## Page 23: agents/logic/tools/async/
**Original URL:** https://docs.livekit.io/agents/logic/tools/async/  
**Source MD URL:** https://docs.livekit.io/agents/logic/tools/async.md

LiveKit docs › Build Agents › Logic & Structure › Tool definition & use › Async tools

---

# Async tools

> Handle long-running tools so agents can keep talking.

## Overview

Tools that take more than a few seconds block the conversation until they return. The agent stops talking, the user hears silence, and a regular tool can't send progress updates, be cancelled, or stop the LLM from calling the same tool twice.

Use async tools for anything that takes more than a few seconds, such as booking a flight, running a web search, or processing a document.

In Node.js, you define a normal `llm.tool(...)`. The tool becomes non-blocking the first time its `execute` function calls `await ctx.update(...)`. Forward the provided `abortSignal` to long-running work so interruptions and cancellation can stop it promptly.

## Updating the user

Use `ctx.update(message)` to send progress to the user while the tool keeps running. It adds a status to the chat context, the LLM reads it, voices something natural to the user, and the conversation continues. Use this for information the LLM should know about, such as a partial result or a phase change.

`RunContext` also provides filler speech to play audio directly through `session.say()`, bypassing the LLM. Use this for filler like "hang on a sec" or "still working on it" during work the LLM doesn't need to track. In Python this is `ctx.with_filler(...)`; in Node.js this is `ctx.filler(...)`.

### Progress updates

Define a regular function tool. Inside, call `ctx.update(message)` whenever you want to share progress, and `return` the final result when the tool is done:

**Python**:

```python
from livekit.agents import Agent, RunContext, function_tool


class TravelAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a travel assistant.")

    @function_tool()
    async def book_flight(
        self, ctx: RunContext, origin: str, destination: str, date: str
    ) -> str:
        """Book a flight for the user.

        Args:
            origin: Departure city or airport code.
            destination: Arrival city or airport code.
            date: Travel date (YYYY-MM-DD).
        """
        await ctx.update(f"Searching flights from {origin} to {destination} on {date}.")
        # agent says: "Sure, let me look up flights from New York to Tokyo on April 15th."

        flights = await search_flights(origin, destination, date)
        await ctx.update(f"Found {len(flights)} options. Booking the best one now.")
        # agent says: "I found 3 options. Booking the best one for you now."

        booking = await confirm_booking(flights[0])
        return f"Booked! Confirmation number: {booking.id}"
        # agent says: "All set. Your booking confirmation number is FL-847293."

```

---

**Node.js**:

```typescript
import { llm } from '@livekit/agents';
import { z } from 'zod';

const bookFlight = llm.tool({
  name: 'bookFlight',
  description: 'Book a flight for the user.',
  parameters: z.object({
    origin: z.string().describe('Departure city or airport code.'),
    destination: z.string().describe('Arrival city or airport code.'),
    date: z.string().describe('Travel date (YYYY-MM-DD).'),
  }),
  execute: async ({ origin, destination, date }, { ctx, abortSignal }) => {
    await ctx.update(`Searching flights from ${origin} to ${destination} on ${date}.`);
    // agent says: "Sure, let me look up flights from New York to Tokyo on April 15th."

    const flights = await searchFlights(origin, destination, date, { signal: abortSignal });
    await ctx.update(`Found ${flights.length} options. Booking the best one now.`);
    // agent says: "I found 3 options. Booking the best one for you now."

    const booking = await confirmBooking(flights[0], { signal: abortSignal });
    return `Booked! Confirmation number: ${booking.id}`;
    // agent says: "All set. Your booking confirmation number is FL-847293."
  },
});

```

The agent waits for the first `ctx.update()` from each tool that calls it, so the user hears acknowledgement immediately. Tools that never call `ctx.update()` behave like regular synchronous tools. Later updates are added to the agent's chat context as they arrive, and the agent generates a new reply once it's idle.

### Filler speech

Open a filler scope around a long-running operation, and the filler plays once the session has been continuously idle for `delay` seconds. Fillers only play during quiet pauses, so they don't talk over the user or pile up behind other agent speech.

**Python**:

```python
from livekit.agents import Agent, RunContext, function_tool


class TravelAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a travel assistant.")

    @function_tool()
    async def book_flight(
        self, ctx: RunContext, origin: str, destination: str, date: str
    ) -> str:
        """Book a flight."""
        # Plays "Still searching..." once the session has been idle for 5 seconds.
        async with ctx.with_filler("Still searching, hang on a sec.", delay=5):
            return await book_flight_api(origin, destination, date)

```

---

**Node.js**:

```typescript
import { llm } from '@livekit/agents';
import { z } from 'zod';

const bookFlight = llm.tool({
  name: 'bookFlight',
  description: 'Book a flight.',
  parameters: z.object({
    origin: z.string(),
    destination: z.string(),
    date: z.string(),
  }),
  execute: async ({ origin, destination, date }, { ctx, abortSignal }) => {
    // Plays "Still searching..." once the session has been idle for 5 seconds.
    return await ctx.filler(
      'Still searching, hang on a sec.',
      { delay: 5000, signal: abortSignal },
      () => bookFlightApi(origin, destination, date, { signal: abortSignal }),
    );
  },
});

```

The following parameters are available on `with_filler` (Python) or `filler` (Node.js):

- **`source`** _(str | Callable)_: The filler to play. Pass a string for a fixed line, or a callable that receives the iteration count. A callable returning `None` (Python) or `null` / `undefined` (Node.js) skips that round and retries on the next interval. The step counter only advances when audio plays, so a series of empty returns doesn't count against `max_steps` / `maxSteps`.

- **`delay`** _(float)_ (optional) - Default: `0`: Continuous session-idle required before each play. Python uses seconds. Node.js uses milliseconds.

- **`interval`** _(float | None)_ (optional) - Default: `None`: Time between plays. Python uses seconds. Node.js uses milliseconds. `None` / omitted plays at most once.

- **`max_steps`** _(int | None)_ (optional) - Default: `None`: Maximum number of times the filler plays. Python uses `max_steps`; Node.js uses `maxSteps`. `None` means no limit.

- **`signal`** _(AbortSignal)_ (optional): Available in:
- [x] Node.js
- [ ] Python

Optional external cancellation signal for the filler scheduler.

### Combining both

Most long-running tools use both channels: `ctx.update()` for key events (start, phase change, final result) and filler speech for the gaps between them. The following example uses both channels in a single tool:

**Python**:

```python
from livekit.agents import Agent, RunContext, function_tool


class TravelAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a travel assistant.")

    @function_tool()
    async def book_flight(
        self, ctx: RunContext, origin: str, destination: str, date: str
    ) -> str:
        """Book a flight."""
        # One real update. The LLM voices a natural intro to the user.
        await ctx.update(
            f"Searching flights from {origin} to {destination} on {date}. "
            "This will take a couple of minutes."
        )

        # Phase 1: searching. Single acoustic filler if the user stays quiet for 5s.
        async with ctx.with_filler("Still searching, hang on a sec.", delay=5):
            flights = await search_flights(origin, destination, date)

        # Phase 2: confirming. Rotating fillers, up to 3 plays with 10s between them.
        followups = [
            "Almost there, just confirming.",
            "Still working on it, won't be long.",
            "Hang tight, almost done.",
        ]
        async with ctx.with_filler(
            lambda step: followups[step], delay=5, interval=10, max_steps=len(followups)
        ):
            booking = await confirm_booking(flights[0])

        # The final return is voiced as a follow-up reply when the agent is
        # next idle. No extra ctx.update() needed.
        return f"Booked! Confirmation number: {booking.id}"

```

---

**Node.js**:

```typescript
const bookFlight = llm.tool({
  name: 'bookFlight',
  description: 'Book a flight.',
  parameters: z.object({
    origin: z.string(),
    destination: z.string(),
    date: z.string(),
  }),
  execute: async ({ origin, destination, date }, { ctx, abortSignal }) => {
    await ctx.update(
      `Searching flights from ${origin} to ${destination} on ${date}. ` +
        'This will take a couple of minutes.',
    );

    const flights = await ctx.filler(
      'Still searching, hang on a sec.',
      { delay: 5000, signal: abortSignal },
      () => searchFlights(origin, destination, date, { signal: abortSignal }),
    );

    const followups = [
      'Almost there, just confirming.',
      "Still working on it, won't be long.",
      'Hang tight, almost done.',
    ];
    const booking = await ctx.filler(
      (step) => followups[step],
      { delay: 5000, interval: 10000, maxSteps: followups.length, signal: abortSignal },
      () => confirmBooking(flights[0], { signal: abortSignal }),
    );

    return `Booked! Confirmation number: ${booking.id}`;
  },
});

```

The two channels stay separate. `ctx.update()` adds to the chat context (the LLM reads it on its next turn). `ctx.with_filler()` / `ctx.filler()` plays audio directly without going through the chat context. The LLM keeps full context for the events that matter, and the user keeps hearing the agent during long operations.

## Pausing for user input

Sometimes a background tool needs to talk to the user mid-run before it can finish, such as collecting a missing detail, confirming a decision, or running a [prebuilt task](https://docs.livekit.io/agents/prebuilt/tasks.md) like `GetEmailTask`.

Wrap this interactive work in a `ctx.foreground()` block. It first plays any reply the tool has already queued, waits for the session to be idle, then prevents other agent speech for the duration of the block. This keeps the exchange clean and matches what the user hears to the order of your code.

**Python**:

```python
from livekit.agents import Agent, RunContext, function_tool
from livekit.agents.beta.workflows import GetEmailTask, WorkflowInstructions


class TravelAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a travel assistant.")
        self._user_email: str | None = None

    @function_tool()
    async def book_flight(
        self, ctx: RunContext, origin: str, destination: str, date: str
    ) -> str:
        """Book a flight."""
        await ctx.update(
            f"Searching flights from {origin} to {destination} on {date}. "
            "This will take a couple of minutes."
        )
        flights = await search_flights(origin, destination, date)

        # Collect the email before confirming. foreground() ensures the
        # email task doesn't collide with the agent's other speech.
        if self._user_email is None:
            async with ctx.foreground():
                result = await GetEmailTask(
                    chat_ctx=self.chat_ctx,
                    instructions=WorkflowInstructions(
                        extra="Tell the user you need their email to confirm the booking."
                    ),
                )
            self._user_email = result.email_address

        booking = await confirm_booking(flights[0], email=self._user_email)
        return f"Booked! Confirmation number: {booking.id}"

```

---

**Node.js**:

Node.js has no prebuilt email task, so build the interactive step with `AgentTask` and run it inside the `foreground()` callback:

```typescript
import { llm, voice } from '@livekit/agents';
import { z } from 'zod';

let userEmail: string | null = null;

function createEmailTask(): voice.AgentTask<{ emailAddress: string }> {
  const task = voice.AgentTask.create<{ emailAddress: string }>({
    instructions:
      'Collect the user email address to confirm the booking. ' +
      'As soon as you have it, call saveEmail.',
    tools: [
      llm.tool({
        name: 'saveEmail',
        description: 'Save the user email address.',
        parameters: z.object({
          emailAddress: z.string().describe('The user email address.'),
        }),
        execute: async ({ emailAddress }) => {
          task.complete({ emailAddress });
          return `Saved email address ${emailAddress}.`;
        },
      }),
    ],
    onEnter: (ctx) => {
      ctx.session.generateReply({
        instructions: 'Ask the user for their email address in one short sentence, then call saveEmail.',
      });
    },
  });
  return task;
}

const bookFlight = llm.tool({
  name: 'bookFlight',
  description: 'Book a flight.',
  parameters: z.object({
    origin: z.string(),
    destination: z.string(),
    date: z.string(),
  }),
  execute: async ({ origin, destination, date }, { ctx }) => {
    await ctx.update(
      `Searching flights from ${origin} to ${destination} on ${date}. ` +
        'This will take a couple of minutes.',
    );
    const flights = await searchFlights(origin, destination, date);

    // Collect the email before confirming. foreground() ensures the
    // email task doesn't collide with the agent's other speech.
    if (!userEmail) {
      const email = await ctx.foreground(async () => {
        ctx.session.say('I need your email to confirm the booking.');
        return createEmailTask().run();
      });
      userEmail = email.emailAddress;
    }

    const booking = await confirmBooking(flights[0], userEmail);
    return `Booked! Confirmation number: ${booking.id}`;
  },
});

```

Use `ctx.foreground()` to wrap any interactive step inside a long-running tool: an `await AgentTask()`, a direct `session.say()`, or a group of calls that must run together without a reply landing between them.

## Cancellation

By default, async tools finish what they're doing regardless of what the user does. To let the LLM cancel a running tool, opt in with the `CANCELLABLE` flag:

**Python**:

```python
from livekit.agents import RunContext, function_tool
from livekit.agents.llm import ToolFlag


@function_tool(flags=ToolFlag.CANCELLABLE)
async def book_flight(ctx: RunContext, origin: str, destination: str, date: str) -> str:
    return ""  # implementation

```

---

**Node.js**:

```typescript
const bookFlight = llm.tool({
  name: 'bookFlight',
  description: 'Book a flight for the user.',
  flags: llm.ToolFlag.CANCELLABLE,
  parameters: z.object({
    origin: z.string(),
    destination: z.string(),
    date: z.string(),
  }),
  execute: async ({ origin, destination, date }, { abortSignal }) => {
    return await bookFlightApi(origin, destination, date, { signal: abortSignal });
  },
});

```

When any cancellable tool is registered, two companion tools are automatically exposed to the LLM:

- `get_running_tasks()` / `lk_agents_get_running_tasks` returns the cancellable calls that are currently running.
- `cancel_task(call_id)` / `lk_agents_cancel_task` cancels one of them by ID. In Python this raises `asyncio.CancelledError` inside the tool. In Node.js, pass `abortSignal` to long-running work so it can stop when the operation is aborted.

Cancellation is opt-in because most tools (orders, writes, payments) aren't safe to interrupt partway through. Make sure cancellable tools can be safely stopped at any point.

If a cancellable tool calls `ctx.disallow_interruptions()` in Python or `ctx.disallowInterruptions()` in Node.js, calling the cancellation tool on it raises `ToolError` instead of cancelling the tool.

MCP tools opt into the same flag through `MCPToolOptions`. See [Per-tool options](https://docs.livekit.io/agents/logic/tools/mcp.md#tool-options).

## Duplicate-call handling

When the LLM calls a tool that's already running, the framework handles the duplicate based on the `on_duplicate` argument to `@function_tool` in Python or the `onDuplicate` option to `llm.tool()` in Node.js. Duplicates are detected by tool name only, not by arguments.

| Mode | Description |
| `allow` | Default. Runs the duplicate without restriction. |
| `reject` | Rejects the duplicate and tells the LLM to cancel via `cancel_task` instead. |
| `replace` | Cancels the running call and starts a new one. Requires the running tool to opt into [cancellation](#cancellation), otherwise the duplicate call raises a `ToolError`. |
| `confirm` | Sends the name and arguments of the running call back to the LLM and asks it to re-call with explicit confirmation if a duplicate is needed. |

For example, to require LLM confirmation before a duplicate runs:

**Python**:

```python
@function_tool(on_duplicate="confirm")
async def book_flight(ctx: RunContext, origin: str, destination: str, date: str) -> str:
    return ""  # implementation

```

---

**Node.js**:

```typescript
const bookFlight = llm.tool({
  name: 'bookFlight',
  description: 'Book a flight for the user.',
  onDuplicate: 'confirm',
  parameters: z.object({
    origin: z.string(),
    destination: z.string(),
    date: z.string(),
  }),
  execute: async ({ origin, destination, date }) => {
    return await bookFlightApi(origin, destination, date);
  },
});

```

## Agent handoffs

By default, async tools belong to the `Agent` they're attached to. Tools placed on `Agent(tools=...)` (or bound as `@function_tool` methods on the agent class) belong to that agent, and any pending updates from them are dropped during an [agent handoff](https://docs.livekit.io/agents/logic/agents-handoffs.md).

To keep a tool running across handoffs, so its final result and any updates go to whichever agent is active when the tool finishes, bundle it into an `AsyncToolset` and pass that to the `AgentSession`:

**Python**:

```python
from livekit.agents import AgentSession, RunContext, function_tool
from livekit.agents.llm.async_toolset import AsyncToolset


@function_tool()
async def book_flight(ctx: RunContext, origin: str, destination: str, date: str) -> str:
    return ""  # implementation


session = AgentSession(
    # ... stt, llm, tts, etc.
    tools=[AsyncToolset(id="booking", tools=[book_flight])],
)

```

---

**Node.js**:

```typescript
const bookFlight = llm.tool({
  name: 'bookFlight',
  description: 'Book a flight for the user.',
  parameters: z.object({
    origin: z.string(),
    destination: z.string(),
    date: z.string(),
  }),
  execute: async ({ origin, destination, date }, { ctx }) => {
    await ctx.update('Searching flights.');
    return await bookFlightApi(origin, destination, date);
  },
});

const session = new voice.AgentSession({
  // ... stt, llm, tts, etc.
  tools: [llm.AsyncToolset.create({ id: 'booking', tools: [bookFlight] })],
});

```

An `AsyncToolset` keeps its tools alive across handoffs, including any pending updates from tools that are still running. Plain function tools passed directly to `AgentSession(tools=[...])` aren't carried across handoffs on their own. Only tools wrapped inside an `AsyncToolset` are. Use `llm.AsyncToolset.create({ id, tools, toolHandling })` when you need a lifecycle scope or custom prompt handling; a normal `llm.tool()` is enough for basic async behavior.

## Prompt templates

The framework sends the LLM a short instruction template around each async tool event: a `ctx.update()` call, a duplicate rejection, or a follow-up reply after a tool finishes. The defaults are tuned for natural agent responses, but you can override any of them by passing a `tool_handling` mapping with an `async_options` block in Python or `toolHandling.asyncOptions` in Node.js.

**Python**:

```python
from livekit.agents import AgentSession


session = AgentSession(
    # ... stt, llm, tts, etc.
    tool_handling={
        "async_options": {
            "update_template": (
                "Background tool `{function_name}` reports: {message}. "
                "Acknowledge briefly. Don't summarize results that aren't in the message."
            ),
        },
    },
)

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
  // ... stt, llm, tts, etc.
  toolHandling: {
    asyncOptions: {
      updateTemplate:
        'Background tool `{functionName}` reports: {message}. ' +
        "Acknowledge briefly. Don't summarize results that aren't in the message.",
    },
  },
});

```

The available `async_options` keys are:

| Python key | Node.js key | Sent to the LLM when |
| `update_template` | `updateTemplate` | A `ctx.update(message)` call is being delivered to the LLM. |
| `duplicate_reject_template` | `duplicateRejectTemplate` | A duplicate call is blocked by `on_duplicate="reject"` or `onDuplicate: 'reject'`. |
| `duplicate_confirm_template` | `duplicateConfirmTemplate` | A duplicate call needs LLM confirmation under `on_duplicate="confirm"` or `onDuplicate: 'confirm'`. |
| `reply_at_tail_template` | `replyAtTailTemplate` | A follow-up reply runs while the pending update is still the latest chat item. |
| `reply_maybe_covered_template` | `replyMaybeCoveredTemplate` | A follow-up reply runs after newer messages have arrived in the chat context. |

Unspecified keys fall back to defaults. Each value can be a template string or a callable. Both forms receive the same named variables for that template. Set `tool_handling` / `toolHandling` on an `AsyncToolset`, on an `Agent`, or on an `AgentSession`. The framework resolves templates from `AsyncToolset` first, then the `Agent`, then the `AgentSession`, falling back to defaults for any key you don't override.

## Additional resources

For more information on concepts covered in this topic, see the following related topics:

- **[Interruptions](https://docs.livekit.io/agents/logic/tools/definition.md#interruptions)**: Handle or prevent interruptions in a blocking tool with `wait_if_not_interrupted` and `disallow_interruptions()`.

- **[User feedback](https://docs.livekit.io/agents/logic/external-data.md#user-feedback)**: Manual techniques for status updates during tool execution.

---

This document was rendered at 2026-08-28T04:22:12.990Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/tools/async.md](https://docs.livekit.io/agents/logic/tools/async.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-24"></a>
## Page 24: agents/logic/tools/mcp/
**Original URL:** https://docs.livekit.io/agents/logic/tools/mcp/  
**Source MD URL:** https://docs.livekit.io/agents/logic/tools/mcp.md

LiveKit docs › Build Agents › Logic & Structure › Tool definition & use › Model Context Protocol (MCP)

---

# Model Context Protocol (MCP)

> Use MCP servers to expose tools to your agent.

Available in:
- [ ] Node.js
- [x] Python

## Overview

LiveKit Agents has first-class support for [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers.

To use MCP, install the optional dependencies:

```shell
uv add livekit-agents[mcp]~=1.5

```

Wrap an MCP server in an `MCPToolset` and pass it to the agent's `tools` parameter:

```python
from livekit.agents import Agent, mcp

class MyAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a helpful assistant.",
            tools=[
                mcp.MCPToolset(
                    id="my-mcp-server",
                    mcp_server=mcp.MCPServerHTTP("https://your-mcp-server.com/mcp"),
                )
            ],
        )

```

> 🔥 **Caution**
> 
> The `mcp_servers` parameter on `AgentSession` and `Agent` is deprecated and will be removed in a future version. Use `MCPToolset` in the `tools` parameter instead. When `mcp_servers` is used, the SDK auto-generates toolset IDs that aren't stable across sessions, so switching to explicit `MCPToolset` gives you predictable IDs.

## HTTP servers

Use `MCPServerHTTP` to connect to a remote MCP server over HTTP:

```python
from livekit.agents import AgentSession, mcp

session = AgentSession(
    # ... other arguments ...
    tools=[
        mcp.MCPToolset(
            id="my-api",
            mcp_server=mcp.MCPServerHTTP(
                "https://your-mcp-server.com/tools",
                transport_type="streamable_http",
            ),
        )
    ],
)

```

> 💡 **Tip**
> 
> The transport type is auto-detected from the URL path: URLs ending in `/mcp` use streamable HTTP transport, and URLs ending in `/sse` use Server-Sent Events transport. To override auto-detection, pass `transport_type` explicitly as shown above.

## Local servers (stdio)

Use `MCPServerStdio` to launch a local MCP server process and communicate over stdin/stdout. This is useful for MCP servers distributed as CLI tools:

```python
from livekit.agents import AgentSession, mcp

session = AgentSession(
    # ... other arguments ...
    tools=[
        mcp.MCPToolset(
            id="filesystem",
            mcp_server=mcp.MCPServerStdio(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"],
            ),
        )
    ],
)

```

The `env` and `cwd` parameters let you customize the child process environment and working directory.

## Authentication

Pass authentication headers to an MCP server with the `headers` parameter:

```python
import os
from livekit.agents import AgentSession, mcp

session = AgentSession(
    # ... other arguments ...
    tools=[
        mcp.MCPToolset(
            id="zapier",
            mcp_server=mcp.MCPServerHTTP(
                "https://actions.zapier.com/mcp/sse",
                headers={
                    "Authorization": f"Bearer {os.environ['ZAPIER_API_KEY']}"
                },
            ),
        )
    ],
)

```

## Filtering tools

Limit which tools from an MCP server are exposed to the LLM. Use [server-level filtering](#server-level-filtering) when you know the exact tool names, or [toolset-level filtering](#toolset-level-filtering) when you need to inspect tools after they load.

### Server-level filtering

Use the `allowed_tools` parameter on the MCP server to filter by tool name. Tools not in the list are excluded.

The following example creates an `MCPToolset`, wrapping `MCPServerHTTP` with `allowed_tools=["search_products", "get_product_details"]`. Only those two tools are available, and everything else the server exposes is excluded.

```python
from livekit.agents import AgentSession, mcp

session = AgentSession(
    # ... other arguments ...
    tools=[
        mcp.MCPToolset(
            id="products",
            mcp_server=mcp.MCPServerHTTP(
                "https://your-mcp-server.com/mcp",
                allowed_tools=["search_products", "get_product_details"],
            ),
        )
    ],
)

```

### Toolset-level filtering

Use `MCPToolset.filter_tools()` for more control. It accepts a predicate function and filters tools in-place after setup.

The following example creates an `MCPToolset`, manually calls `setup()` to connect and fetch tools, then calls `filter_tools()` with a lambda that only keeps tools with IDs containing "search".

```python
from livekit.agents import mcp

toolset = mcp.MCPToolset(
    id="my-api",
    mcp_server=mcp.MCPServerHTTP("https://your-mcp-server.com/mcp"),
)

# When using outside of AgentSession, call setup() manually
await toolset.setup()
toolset.filter_tools(lambda tool: "search" in tool.id)

```

## Transforming tool results

Use the `tool_result_resolver` parameter to transform MCP tool results before they reach the LLM. The resolver receives an `MCPToolResultContext` with `tool_name`, `arguments`, and `result`. It can be sync or async.

By default, the SDK serializes content items to JSON. This example truncates large results instead:

```python
import json
from livekit.agents import mcp

MAX_CHARS = 4000

async def truncating_resolver(ctx: mcp.MCPToolResultContext) -> str:
    """Truncate large MCP tool results to avoid excessive LLM context usage."""
    if len(ctx.result.content) == 1:
        text = str(ctx.result.content[0].model_dump_json())
    elif len(ctx.result.content) > 1:
        text = json.dumps([item.model_dump() for item in ctx.result.content])
    else:
        return "Tool returned no content."

    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS] + "\n... [truncated]"
    return text

session = AgentSession(
    # ... other arguments ...
    tools=[
        mcp.MCPToolset(
            id="my-api",
            mcp_server=mcp.MCPServerHTTP(
                "https://your-mcp-server.com/mcp",
                tool_result_resolver=truncating_resolver,
            ),
        )
    ],
)

```

The resolver is available on all MCP server types and is only called for successful tool calls. Errors raise a `ToolError` before the resolver runs.

## Per-tool options

`MCPToolset` is an [async toolset](https://docs.livekit.io/agents/logic/tools/async.md), so you can configure individual MCP tools the same way you configure a function tool. Pass `tool_options`, a dictionary keyed by tool name, with an `MCPToolOptions` value for each tool you want to configure. Tools you don't list run as plain blocking calls.

The following example makes a long-running `book_flight` tool cancellable, requires confirmation before a duplicate call runs, and forwards the server's progress notifications to the user:

```python
from livekit.agents import AgentSession, mcp
from livekit.agents.llm import ToolFlag

session = AgentSession(
    # ... other arguments ...
    tools=[
        mcp.MCPToolset(
            id="mcp",
            mcp_server=mcp.MCPServerHTTP(
                "https://your-mcp-server.com/mcp",
                # book_flight runs longer than the default per-request timeout.
                client_session_timeout_seconds=120,
            ),
            tool_options={
                "book_flight": mcp.MCPToolOptions(
                    flags=ToolFlag.CANCELLABLE,
                    on_duplicate="confirm",
                    report_progress=True,
                ),
            },
        )
    ],
)

```

`MCPToolOptions` accepts three independent options:

- **`flags`** _(ToolFlag)_ (optional) - Default: `ToolFlag.NONE`: Tool flags, mirroring the `@function_tool` decorator. Use `ToolFlag.CANCELLABLE` to let the LLM cancel the tool while it runs, or `ToolFlag.IGNORE_ON_ENTER` to skip the tool during `on_enter`.

When any tool is `ToolFlag.CANCELLABLE`, the `lk_agents_get_running_tasks` and `lk_agents_cancel_task` tools are automatically exposed to the LLM so it can list and cancel running calls. See [Cancellation](https://docs.livekit.io/agents/logic/tools/async.md#cancellation) for details.

- **`on_duplicate`** _(DuplicateMode)_ (optional) - Default: `allow`: Controls how duplicate calls to a running tool are handled. Valid values are: `allow`, `reject`, `replace`, or `confirm`. Uses the same values as the `@function_tool` decorator. To learn more, see [Duplicate-call handling](https://docs.livekit.io/agents/logic/tools/async.md#duplicate-calls).

- **`report_progress`** _(bool)_ (optional) - Default: `False`: When `true`, forwards the MCP server's `report_progress` notifications to `ctx.update()`. The tool runs in the background so the agent can narrate progress while it works. See [Progress updates](https://docs.livekit.io/agents/logic/tools/async.md#progress-updates).

For a complete example, including an MCP server that emits progress notifications, see [`examples/voice_agents/mcp/`](https://github.com/livekit/agents/tree/main/examples/voice_agents/mcp).

## Multiple servers

Pass multiple `MCPToolset` instances in the `tools` list. You can combine different server types, and all servers are initialized in parallel:

```python
from livekit.agents import AgentSession, mcp

session = AgentSession(
    # ... other arguments ...
    tools=[
        mcp.MCPToolset(
            id="api-server",
            mcp_server=mcp.MCPServerHTTP("https://api.example.com/mcp"),
        ),
        mcp.MCPToolset(
            id="filesystem",
            mcp_server=mcp.MCPServerStdio(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-filesystem", "/data"],
            ),
        ),
    ],
)

```

If an individual server fails to connect, the error is logged but does not prevent the agent from starting.

## Combining MCP tools with function tools

Your agent can use both MCP-provided tools and locally defined function tools. Pass them together in the `tools` list.

In the following example, the LLM can call both the MCP server's tools and the `save_note` function tool.

```python
from livekit.agents import Agent, function_tool, RunContext, mcp

class MyAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a helpful assistant with access to a knowledge base and local tools.",
            tools=[
                mcp.MCPToolset(
                    id="knowledge-base",
                    mcp_server=mcp.MCPServerHTTP("https://your-mcp-server.com/sse"),
                )
            ],
        )

    @function_tool()
    async def save_note(self, context: RunContext, text: str) -> str:
        """Save a note for the user.

        Args:
            text: The note content to save.
        """
        # your custom logic here
        return "Note saved successfully."

```

In this example, the LLM can call both the MCP server's tools and the `save_note` function tool.

## Agent vs AgentSession placement

`MCPToolset` follows the same `tools` override pattern as other tools. If an `Agent` specifies `tools`, those tools **replace** (not merge with) any tools set on the `AgentSession`. The toolset lifecycle depends on where you place it. Agent toolsets close when switching to a different agent, and session toolsets close when the session ends. See [Toolsets](https://docs.livekit.io/agents/logic/tools/toolsets.md) for details.

> 💡 **Tip**
> 
> Set toolsets on the `AgentSession` for shared defaults across multiple agents in a workflow. Set toolsets on a specific `Agent` only when that agent needs a different set of tools. This is the same override pattern used by `stt`, `llm`, `tts`, and other agent properties.

- **[MCP Agent](https://docs.livekit.io/reference/recipes/http_mcp_client.md)**: A voice AI agent with an integrated Model Context Protocol (MCP) client for the LiveKit API.

- **[Shopify voice shopper](https://github.com/livekit-examples/python-agents-examples/tree/main/complex-agents/shopify-voice-shopper)**: Advanced example combining MCP with function tools and dynamic agent switching.

---

This document was rendered at 2026-08-28T04:22:12.994Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/tools/mcp.md](https://docs.livekit.io/agents/logic/tools/mcp.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-25"></a>
## Page 25: agents/logic/tools/forwarding/
**Original URL:** https://docs.livekit.io/agents/logic/tools/forwarding/  
**Source MD URL:** https://docs.livekit.io/agents/logic/tools/forwarding.md

LiveKit docs › Build Agents › Logic & Structure › Tool definition & use › Forwarding to the frontend

---

# Forwarding to the frontend

> Fulfill tool calls via RPC from the client.

## Overview

Forward tool calls to a frontend app using [RPC](https://docs.livekit.io/transport/data/rpc.md). This is useful when the data needed to fulfill the function call is only available at the frontend. You may also use RPC to trigger actions or UI updates in a structured way.

For instance, the following sections include a function that accesses the user's live location from their web browser.

### Agent implementation

**Python**:

```python
from livekit.agents import function_tool, get_job_context, RunContext

@function_tool()
async def get_user_location(
    context: RunContext,
    high_accuracy: bool
):
    """Retrieve the user's current geolocation as lat/lng.
    
    Args:
        high_accuracy: Whether to use high accuracy mode, which is slower but more precise
    
    Returns:
        A dictionary containing latitude and longitude coordinates
    """
    try:
        room = get_job_context().room
        participant_identity = next(iter(room.remote_participants))
        response = await room.local_participant.perform_rpc(
            destination_identity=participant_identity,
            method="getUserLocation",
            payload=json.dumps({
                "highAccuracy": high_accuracy
            }),
            response_timeout=10.0 if high_accuracy else 5.0,
        )
        return response
    except Exception:
        raise ToolError("Unable to retrieve user location")

```

---

**Node.js**:

```typescript
import { llm, getJobContext } from '@livekit/agents';
import { z } from 'zod';

const getUserLocation = llm.tool({
  name: 'getUserLocation',
  description: 'Retrieve the user\'s current geolocation as lat/lng.',
  parameters: z.object({
    highAccuracy: z.boolean().describe('Whether to use high accuracy mode, which is slower but more precise'),
  }),
  execute: async ({ highAccuracy }, { ctx }) => {
    try {
      const room = getJobContext().room;
      const participant = Array.from(room.remoteParticipants.values())[0]!;
      
      const response = await room.localParticipant!.performRpc({
        destinationIdentity: participant.identity,
        method: 'getUserLocation',
        payload: JSON.stringify({ highAccuracy }),
        responseTimeout: highAccuracy ? 10000 : 5000,
      });
      
      return response;
    } catch (error) {
      throw new llm.ToolError("Unable to retrieve user location");
    }
  },
});

```

### Frontend implementation

The following example uses the JavaScript SDK. The same pattern works for other SDKs. For more examples, see the [RPC documentation](https://docs.livekit.io/transport/data/rpc.md).

```typescript
import { RpcError, RpcInvocationData } from 'livekit-client';

localParticipant.registerRpcMethod(
    'getUserLocation',
    async (data: RpcInvocationData) => {
        try {
            let params = JSON.parse(data.payload);
            const position: GeolocationPosition = await new Promise((resolve, reject) => {
                navigator.geolocation.getCurrentPosition(resolve, reject, {
                    enableHighAccuracy: params.highAccuracy ?? false,
                    timeout: data.responseTimeout,
                });
            });

            return JSON.stringify({
                latitude: position.coords.latitude,
                longitude: position.coords.longitude,
            });
        } catch (error) {
            throw new RpcError(1, "Could not retrieve user location");
        }
    }
);

```

## Additional resources

- **[RPC](https://docs.livekit.io/transport/data/rpc.md)**: Complete documentation on function calling between LiveKit participants.

- **[Frontends](https://docs.livekit.io/frontends.md)**: Build the client app that registers RPC methods and connects to the room.

- **[Sessions (frontend)](https://docs.livekit.io/frontends/build/sessions.md)**: Connect to rooms and access the participant for RPC registration.

- **[Function tool definition](https://docs.livekit.io/agents/logic/tools/definition.md)**: Define the agent-side tool and use RunContext, speech, and error handling.

- **[Tool definition & use](https://docs.livekit.io/agents/logic/tools.md)**: Overview of tools, types, and related topics.

---

This document was rendered at 2026-08-28T04:22:13.003Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/tools/forwarding.md](https://docs.livekit.io/agents/logic/tools/forwarding.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-26"></a>
## Page 26: agents/logic/tools/design/
**Original URL:** https://docs.livekit.io/agents/logic/tools/design/  
**Source MD URL:** https://docs.livekit.io/agents/logic/tools/design.md

LiveKit docs › Build Agents › Logic & Structure › Tool definition & use › Tool loop design

---

# Tool loop design

> Design tool loops that pick the right tool, return useful results, and stay fast under voice latency constraints.

## Overview

LiveKit agents with [tools](https://docs.livekit.io/agents/logic/tools/definition.md) run an iterative loop: the LLM reasons about what to do, calls a tool, observes the results, then either calls another tool or replies. The framework runs this loop automatically, so most developers don't think about it until something goes wrong: the agent picks the wrong tool, responds incorrectly, or takes too long. This guide covers how to design tool loops that pick the right tool, return useful results, and stay fast.

## Focus the toolset

The model picks from your tool list on every turn and the list is part of every prompt. Long lists increase token usage, slow the loop, and can lead to incorrect tool selection. Aim for 5 to 10 tools per agent. Beyond 10 tools, incorrect selections become more common, and past 20, the model often struggles to choose reliably.

Use the following approaches to keep the set focused:

- **Consolidate overlapping tools.** Two tools that share a purpose perform better as one tool with a parameter. `search_customer(query, kind: 'name' | 'id')` beats `search_customer_by_name` plus `search_customer_by_id`. One clear tool with a parameter is easier to pick than two with similar names.
- **Expose actions, not endpoints.** API endpoints expose CRUD; tools should expose capabilities. Prefer `search_contact(query)` over `list_contacts()`. The first returns the one record the agent wants. The second hands it 50 entries to reason through as text. Filter, sort, and format in code. Hand the agent only what it needs.
- **Namespace tools by service, then resource.** When several tools cover the same domain, prefix them by service (`linear_search`, `asana_search`) and then by resource (`linear_issues_search`, `linear_teams_search`). Consistent prefixes signal scope to the model, making it easier to pick the right tool from a long list.
- **Filter MCP server tools.** A single MCP server can add 30 or more tools at once. Use [server-level filtering](https://docs.livekit.io/agents/logic/tools/mcp.md#filter-server) or [toolset-level filtering](https://docs.livekit.io/agents/logic/tools/mcp.md#filter-toolset) to narrow what's exposed to the agent on any given turn.
- **Dynamically register tools.** For very large or rarely used capability sets, register tools at runtime instead of statically. See [Adding tools dynamically](https://docs.livekit.io/agents/logic/tools/definition.md#adding-tools-dynamically) and [Toolsets](https://docs.livekit.io/agents/logic/tools/toolsets.md).
- **Split across agents past the limit.** Past ~10 tools per agent, divide responsibility across agents using [handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md) or the [supervisor pattern](https://docs.livekit.io/agents/logic/supervisor-pattern.md) instead of overloading one agent.

## Design tools for the model

Every tool you expose is text the model reads: the description as it picks the tool, the parameter list as it fills in arguments, and the return as it composes its next reply. The model can't see the implementation. Treat what it can see (descriptions, parameter names, return formats) the way you'd treat onboarding docs for a new hire: state what the tool does, when to call it, what to pass, and what to expect back.

### Write descriptions the model can act on

A good tool description states what the tool does, when to call it, and when **not** to call it. Be explicit about constraints, provide examples, and call out boundaries with related tools.

**Python**:

```python
# Avoid: vague description, no parameter guidance, no return contract.
@function_tool
async def get_data(date: str) -> str:
    """Gets data."""
    ...

# Prefer: specific trigger, parameter formats, return shape, exclusion rule.
@function_tool
async def check_availability(date: str, party_size: int) -> str:
    """Check open reservation slots for a given date.

    Call this when the user asks about reservations. Don't call it
    until you have both the date and the party size.

    Args:
        date: Reservation date in YYYY-MM-DD format.
        party_size: Number of guests, between 1 and 12.

    Returns:
        A speech-ready summary of available times.
    """
    ...

```

---

**Node.js**:

```typescript
// Avoid: vague description, no parameter guidance, no return contract.
const checkAvailability = llm.tool({
  name: 'checkAvailability',
  description: 'Gets data.',
  parameters: z.object({ date: z.string() }),
  execute: async ({ date }) => { /* ... */ },
});

// Prefer: specific trigger, parameter formats, return shape, exclusion rule.
const checkAvailability = llm.tool({
  name: 'checkAvailability',
  description:
    "Check open reservation slots for a given date. Call this when the user " +
    "asks about reservations. Don't call it until you have both the date " +
    "and the party size. Returns a speech-ready summary of available times.",
  parameters: z.object({
    date: z.string().describe('Reservation date in YYYY-MM-DD format.'),
    partySize: z.number().int().min(1).max(12)
      .describe('Number of guests, between 1 and 12.'),
  }),
  execute: async ({ date, partySize }) => {
    // Return a speech-ready summary.
  },
});

```

### Pin down parameter values

State valid values in the description, not just the type. Even when the type is enforceable (`Literal["lunch", "dinner"]`, `z.enum(['lunch', 'dinner'])`), the model reads the description more carefully than the schema, so spelling out `Meal must be "lunch" or "dinner".` prevents a bad call instead of relying on the framework to reject one. For formats a type can't express (date strings, currency codes, casing rules), prose is the only signal, so give the format and an example.

### Shape returns for the agent, not the API

Tools return data to the LLM, not to a frontend. In voice especially, the model often incorporates the return value into its spoken response with minimal rewording, so format for speech rather than for screens. Return values the model can incorporate into its next response without a second formatting pass:

- **Return speech-ready strings, not raw payloads.** Prefer `"3 slots available at 1 PM, 2:30 PM, and 4 PM"` over `[{time: "13:00"}, ...]`. A raw payload forces extra reasoning before the agent can speak.
- **Return semantic identifiers, not opaque ones.** LLMs are trained on human language, so they reason far better over `"Reservation #R-1842 (Friday 7 PM, party of 3)"` than `"550e8400-e29b-41d4-a716-446655440000"`. Use names, dates, and short codes the agent can repeat back to a user.
- **Return only high-value information.** A tool isn't an API endpoint, so don't return the full record just because you can. If the agent needs the party size and time, return those, not the full reservation.
- **Offer a verbosity parameter when both lengths are useful.** A `response_format: "concise" | "detailed"` parameter lets the agent ask for what it needs. For a reservation lookup, `concise` returns `"Friday at 7:45 PM, party of 3"` (speech-ready); `detailed` returns party size, time, special requests, and notes (useful when the model needs to reason about whether to suggest changes). See the Anthropic [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) guide for the pattern.
- **Keep return values small.** Paginate, summarize, or hand the result ID to a follow-up tool when the data is large. Long returns bloat the context window, slow inference, and degrade reasoning quality.

## Control the loop from code

The model is non-deterministic. Push correctness into your code rather than the prompt.

### Bound the loop

Set a hard limit on consecutive tool calls per LLM turn with `max_tool_steps` on `AgentSession`. The default is 3. When the loop hits this limit, the framework makes one final LLM call with tool use disabled and the agent replies with whatever context it has. Increase the limit for agents that legitimately chain calls (for example, a lookup followed by an action). Decrease it for agents whose tools should rarely fire more than once per turn.

**Python**:

```python
session = AgentSession(
    stt=...,
    llm=...,
    tts=...,
    max_tool_steps=5,  # default is 3
)

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
  stt: ...,
  llm: ...,
  tts: ...,
  maxToolSteps: 5, // default is 3
});

```

Most LLM providers also let the model propose multiple tool calls in a single step that run concurrently. Concurrent calls are faster when independent (looking up two records, for example). When one tool's result must feed the next, disable parallelism so the loop runs serially:

**Python**:

```python
from livekit.agents import inference

llm = inference.LLM(
    model="openai/gpt-4.1-mini",
    extra_kwargs={"parallel_tool_calls": False},
)

```

---

**Node.js**:

```typescript
import { openai } from '@livekit/agents-plugin-openai';

const llm = new openai.LLM({
  model: 'gpt-4.1-mini',
  parallelToolCalls: false,
});

```

### Raise actionable errors

A tool error message becomes part of the next prompt the model sees, and in voice the agent often reads it back to the user. A bare exception becomes "the tool failed" in the model's view, which leads to retries or apologies that aren't grounded in the actual problem. Raise `ToolError` with a reason the model can communicate or recover from.

**Python**:

```python
from livekit.agents.llm import ToolError

@function_tool
async def lookup_reservation(self, confirmation: str) -> str:
    """Look up a reservation by its confirmation code."""
    reservation = await reservations_api.get(confirmation)
    if reservation is None:
        raise ToolError(
            "No reservation matches that confirmation code. "
            "Ask the user to double-check the code or look in their email."
        )
    return f"Reservation #{reservation.id} for {reservation.party_size} on {reservation.date} at {reservation.time}."

```

---

**Node.js**:

```typescript
import { llm } from '@livekit/agents';

const lookupReservation = llm.tool({
  name: 'lookupReservation',
  description: 'Look up a reservation by its confirmation code.',
  parameters: z.object({ confirmation: z.string() }),
  execute: async ({ confirmation }) => {
    const reservation = await reservationsApi.get(confirmation);
    if (!reservation) {
      throw new llm.ToolError(
        'No reservation matches that confirmation code. ' +
        'Ask the user to double-check the code or look in their email.',
      );
    }
    return `Reservation #${reservation.id} for ${reservation.partySize} on ${reservation.date} at ${reservation.time}.`;
  },
});

```

### Gate critical actions

When a turn must end with a specific action, such as confirming a booking, completing a task, or recording consent, don't trust the model to fire the right tool at the right time. Track state in code and require the model to confirm before the action runs.

A self-reporting parameter makes the model's intent visible so your code can enforce it. For a booking confirmation, the agent should always read the details back to the user before the reservation is written:

**Python**:

```python
@function_tool
async def confirm_reservation(
    self,
    date: str,
    time: str,
    party_size: int,
    read_back: bool,
) -> str:
    """Book the reservation. Only call this after reading the details back to the user.

    Args:
        date: Reservation date in YYYY-MM-DD format.
        time: Reservation time in 24-hour HH:MM format.
        party_size: Number of guests, between 1 and 12.
        read_back: Set to True only after you have read the date, time,
            and party size back to the user and they have confirmed.
    """
    if not read_back:
        return "Read the date, time, and party size back to the user first, then call this tool again."
    booking = await reservations_api.book(date, time, party_size)
    return f"Booked. Confirmation code is {booking.confirmation}."

```

---

**Node.js**:

```typescript
const confirmReservation = llm.tool({
  name: 'confirmReservation',
  description:
    'Book the reservation. Only call this after reading the details back to the user.',
  parameters: z.object({
    date: z.string().describe('Reservation date in YYYY-MM-DD format.'),
    time: z.string().describe('Reservation time in 24-hour HH:MM format.'),
    partySize: z.number().int().min(1).max(12)
      .describe('Number of guests, between 1 and 12.'),
    readBack: z.boolean().describe(
      'Set to true only after you have read the date, time, and party size ' +
      'back to the user and they have confirmed.',
    ),
  }),
  execute: async ({ date, time, partySize, readBack }) => {
    if (!readBack) {
      return 'Read the date, time, and party size back to the user first, then call this tool again.';
    }
    const booking = await reservationsApi.book(date, time, partySize);
    return `Booked. Confirmation code is ${booking.confirmation}.`;
  },
});

```

This pattern prevents the agent from writing the reservation before the user has actually confirmed the details.

### Disable interruptions on writes

By default, user speech can interrupt a running tool. For read-only tools that's fine. For tools that write data (placing an order, sending a message, charging a card), an interruption can leave the operation half-done. Call `run_ctx.disallow_interruptions()` (Python) or `ctx.disallowInterruptions()` (Node.js) at the start of any mutating tool. See [Interruptions](https://docs.livekit.io/agents/logic/tools/definition.md#interruptions) for the full API.

## Manage loop latency

Even an optimized loop takes time, and in voice that time results in silence on the user's end. The techniques below help you mask dead air, bound how slow a tool can be, and skip a handoff you don't need.

### Speak during long tool calls

If a tool can take more than a second, start speaking before it finishes. Use `session.say()` inside the tool to play a short, pre-determined filler line.

**Python**:

```python
@function_tool
async def find_alternative_times(
    self,
    run_ctx: RunContext,
    date: str,
    party_size: int,
) -> str:
    """Find available reservation times on a given date when the user's first choice is full."""
    run_ctx.session.say("Let me see what else is open.")
    result = await reservations_api.search_times(date, party_size)
    return result.speech_summary

```

---

**Node.js**:

```typescript
const findAlternativeTimes = llm.tool({
  name: 'findAlternativeTimes',
  description:
    "Find available reservation times on a given date when the user's first choice is full.",
  parameters: z.object({
    date: z.string().describe('Reservation date in YYYY-MM-DD format.'),
    partySize: z.number().int().min(1).max(12),
  }),
  execute: async ({ date, partySize }, { ctx }) => {
    ctx.session.say('Let me see what else is open.');
    const result = await reservationsApi.searchTimes(date, partySize);
    return result.speechSummary;
  },
});

```

For repeat-use fillers, pre-render the audio. See [Cached TTS in tools](https://docs.livekit.io/agents/multimodality/audio/customization.md#cached-tts-in-tools).

### Bound tools with a timeout

Tools that call external systems should have a timeout. A backend that hangs blocks the session: the close callback doesn't run and the next turn never starts.

**Python**:

```python
import asyncio
from livekit.agents.llm import ToolError

@function_tool
async def lookup_reservation_status(self, confirmation: str) -> str:
    """Look up the status of a reservation by its confirmation code."""
    try:
        async with asyncio.timeout(5):
            return await reservations_api.get_status(confirmation)
    except asyncio.TimeoutError as err:
        raise ToolError(
            "Reservation lookup is slow right now. Ask the user to try again in a moment."
        ) from err

```

---

**Node.js**:

```typescript
const lookupReservationStatus = llm.tool({
  name: 'lookupReservationStatus',
  description: 'Look up the status of a reservation by its confirmation code.',
  parameters: z.object({ confirmation: z.string() }),
  execute: async ({ confirmation }) => {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 5000);
    try {
      return await reservationsApi.getStatus(confirmation, { signal: controller.signal });
    } catch (err) {
      throw new llm.ToolError(
        'Reservation lookup is slow right now. Ask the user to try again in a moment.',
      );
    } finally {
      clearTimeout(timeoutId);
    }
  },
});

```

### Update in place instead of handing off

A full agent handoff adds a reasoning step before the new agent speaks. When the only thing changing is the prompt or available tools, mutate the current agent instead:

- **Update instructions**: `agent.update_instructions(new_text)` in Python, `agent.updateInstructions(newText)` in Node.js.
- **Update tools**: `agent.update_tools(new_tool_list)` in Python, `agent.updateTools(newTools)` in Node.js. See [Adding tools dynamically](https://docs.livekit.io/agents/logic/tools/definition.md#adding-tools-dynamically) for the full API.

For example, after a reservation agent verifies a caller's account, it can grant access to authenticated tools without handing off:

**Python**:

```python
@function_tool
async def verify_user(self, email: str) -> str:
    """Verify the user so they can manage their account."""
    user = await users_api.lookup(email)
    if user is None:
        return "No account found with that email."

    await self.update_tools(
        self.tools + [lookup_my_reservations, cancel_my_reservation]
    )
    await self.update_instructions(
        self.instructions + f" The user is verified as {user.name}."
    )
    return f"Got it, {user.name}. How can I help with your account?"

```

---

**Node.js**:

```typescript
const verifyUser = llm.tool({
  name: 'verifyUser',
  description: 'Verify the user so they can manage their account.',
  parameters: z.object({ email: z.string() }),
  execute: async ({ email }, { ctx }) => {
    const user = await usersApi.lookup(email);
    if (!user) return 'No account found with that email.';

    const agent = ctx.session.currentAgent;
    await agent.updateTools([
      ...agent.toolCtx.tools,
      lookupMyReservations,
      cancelMyReservation,
    ]);
    await agent.updateInstructions(
      `${agent.instructions} The user is verified as ${user.name}.`,
    );
    return `Got it, ${user.name}. How can I help with your account?`;
  },
});

```

Use [agent handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md) when the conversational role changes, not for configuration-only changes.

## Example: a reservation agent

The agent below showcases the principles from this guide. It exposes three tools (`check_availability`, `find_alternatives`, and `book_reservation`) and uses them to take a restaurant reservation end to end.

**Python**:

```python
import asyncio
from typing import Literal

from livekit.agents import Agent, AgentSession, RunContext, function_tool
from livekit.agents.llm import ToolError


class ReservationAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You take restaurant reservations. Confirm the date, time, "
                "and party size with the user before booking. Always read "
                "the details back before calling book_reservation."
            ),
        )

    @function_tool
    async def check_availability(
        self,
        date: str,
        party_size: int,
        meal: Literal["lunch", "dinner"],
    ) -> str:
        """Check open reservation slots for a given date and meal.

        Call this when the user asks about availability. Don't call it
        until you have the date, party size, and meal (must be "lunch"
        or "dinner").

        Args:
            date: Reservation date in YYYY-MM-DD format.
            party_size: Number of guests, between 1 and 12.
            meal: Either "lunch" or "dinner".

        Returns:
            A speech-ready summary of available times.
        """
        try:
            async with asyncio.timeout(5):
                slots = await reservations_api.check(date, party_size, meal)
        except asyncio.TimeoutError as err:
            raise ToolError(
                "Availability lookup is slow. Ask the user to try again in a moment."
            ) from err
        if not slots:
            return f"No {meal} availability on {date} for a party of {party_size}."
        return f"{len(slots)} {meal} slots open on {date}: {', '.join(slots)}."

    @function_tool
    async def find_alternatives(
        self,
        run_ctx: RunContext,
        date: str,
        party_size: int,
    ) -> str:
        """Find nearby dates with availability when the requested date is full."""
        run_ctx.session.say("Let me check what else is open.")
        try:
            async with asyncio.timeout(8):
                result = await reservations_api.search_nearby(date, party_size)
        except asyncio.TimeoutError as err:
            raise ToolError(
                "Alternative search is slow. Ask the user to try again."
            ) from err
        return result.speech_summary

    @function_tool
    async def book_reservation(
        self,
        run_ctx: RunContext,
        date: str,
        time: str,
        party_size: int,
        read_back: bool,
    ) -> str:
        """Book a reservation. Only call after reading the details back to the user.

        Args:
            date: Reservation date in YYYY-MM-DD format.
            time: Reservation time in 24-hour HH:MM format.
            party_size: Number of guests, between 1 and 12.
            read_back: Set to True only after you have read the date, time,
                and party size back to the user and they have confirmed.
        """
        if not read_back:
            return (
                "Read the date, time, and party size back to the user first, "
                "then call this tool again."
            )
        run_ctx.disallow_interruptions()
        booking = await reservations_api.book(date, time, party_size)
        return (
            f"Booked for {party_size} on {date} at {time}. "
            f"Confirmation #{booking.code}."
        )


session = AgentSession(
    stt=...,
    llm=...,
    tts=...,
    max_tool_steps=5,
)

```

---

**Node.js**:

```typescript
import { llm, voice } from '@livekit/agents';
import { z } from 'zod';

const reservationAgent = voice.Agent.create({
  instructions:
    'You take restaurant reservations. Confirm the date, time, and ' +
    'party size with the user before booking. Always read the details ' +
    'back before calling bookReservation.',
  tools: [
    llm.tool({
      name: 'checkAvailability',
      description:
        'Check open reservation slots for a given date and meal. Call ' +
        "this when the user asks about availability. Don't call it until " +
        'you have the date, party size, and meal (must be "lunch" or "dinner"). ' +
        'Returns a speech-ready summary of available times.',
      parameters: z.object({
        date: z.string().describe('Reservation date in YYYY-MM-DD format.'),
        partySize: z.number().int().min(1).max(12)
          .describe('Number of guests, between 1 and 12.'),
        meal: z.enum(['lunch', 'dinner'])
          .describe('Either "lunch" or "dinner".'),
      }),
      execute: async ({ date, partySize, meal }) => {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 5000);
        try {
          const slots = await reservationsApi.check(date, partySize, meal, {
            signal: controller.signal,
          });
          if (slots.length === 0) {
            return `No ${meal} availability on ${date} for a party of ${partySize}.`;
          }
          return `${slots.length} ${meal} slots open on ${date}: ${slots.join(', ')}.`;
        } catch {
          throw new llm.ToolError(
            'Availability lookup is slow. Ask the user to try again in a moment.',
          );
        } finally {
          clearTimeout(timeoutId);
        }
      },
    }),

    llm.tool({
      name: 'findAlternatives',
      description:
        'Find nearby dates with availability when the requested date is full.',
      parameters: z.object({
        date: z.string().describe('Reservation date in YYYY-MM-DD format.'),
        partySize: z.number().int().min(1).max(12),
      }),
      execute: async ({ date, partySize }, { ctx }) => {
        ctx.session.say('Let me check what else is open.');
        const result = await reservationsApi.searchNearby(date, partySize);
        return result.speechSummary;
      },
    }),

    llm.tool({
      name: 'bookReservation',
      description:
        'Book a reservation. Only call after reading the details back to the user.',
      parameters: z.object({
        date: z.string().describe('Reservation date in YYYY-MM-DD format.'),
        time: z.string().describe('Reservation time in 24-hour HH:MM format.'),
        partySize: z.number().int().min(1).max(12)
          .describe('Number of guests, between 1 and 12.'),
        readBack: z.boolean().describe(
          'Set to true only after you have read the date, time, and ' +
          'party size back to the user and they have confirmed.',
        ),
      }),
      execute: async ({ date, time, partySize, readBack }, { ctx }) => {
        if (!readBack) {
          return 'Read the date, time, and party size back to the user first, then call this tool again.';
        }
        ctx.disallowInterruptions();
        const booking = await reservationsApi.book(date, time, partySize);
        return `Booked for ${partySize} on ${date} at ${time}. Confirmation #${booking.code}.`;
      },
    }),
  ],
});

const session = new voice.AgentSession({
  stt: ...,
  llm: ...,
  tts: ...,
  maxToolSteps: 5,
});

```

The agent integrates each principle from this guide:

- **Focused tool set.** Three tools, well under the [5-10 target](#focus-the-toolset).
- **Pinned parameter values.** `meal` is constrained in both the type (`Literal`/`z.enum`) and the docstring. The schema stops the type checker from accepting an invalid value; the prose stops the model from inventing one. See [Design tools for the model](#design-tools-for-the-model).
- **Bounded external calls.** Each API call has an `asyncio.timeout` and a `ToolError` with a recovery message the agent can pass to the user. See [Control the loop from code](#control-the-loop-from-code).
- **Confirmation gate.** `book_reservation` takes a `read_back` parameter the model must set to `True` only after speaking the details aloud. If `read_back` is false, the tool returns a reminder. See [Control the loop from code](#control-the-loop-from-code).
- **Interruption block on writes.** `disallow_interruptions()` (Python) or `disallowInterruptions()` (Node.js) guards the booking call so a barge-in can't leave a half-finished write. See [Control the loop from code](#control-the-loop-from-code).
- **Masked latency.** `find_alternatives` uses `session.say()` so the user hears something while the search runs. See [Manage loop latency](#manage-loop-latency).
- **Step limit.** The session sets `max_tool_steps=5`, capping how many tool calls can chain per turn. See [Control the loop from code](#control-the-loop-from-code).

## Test and debug

Run the agent to verify your tools work well. You can surface issues by running evaluations and reviewing sessions:

- **Run evaluations:** write a small set of input-output pairs that capture the tool calls you expect. For example, "Do you have a table for 3 on Friday?" should produce a `check_availability` call with `party_size=3`. Use real, varied data rather than a synthetic happy path. Run the set on every change. See [Testing and evaluation](https://docs.livekit.io/agents/start/testing.md).
- **Run simulations:** exercise the tools in LLM-driven conversations with an [agent simulation](https://docs.livekit.io/agents/start/testing/simulations.md). Because the simulated user drives the conversation instead of following a script you wrote, this surfaces tool problems on paths you didn't anticipate, like redundant calls or wrong arguments several turns in.

Available in (BETA):
- [ ] Node.js
- [x] Python
- **Watch real sessions:** use the [Agents Console](https://docs.livekit.io/agents/start/console.md) during development and [Agent Observability](https://docs.livekit.io/deploy/observability/insights.md) in production. Look for turns where the model called a tool with the wrong arguments, chained more tool calls than the typical depth, or read a hold message after the tool had already returned.

When you find a failure, the kind of failure usually tells you what to fix:

- **Redundant tool calls** typically mean return values include too little or too much data. This forces the agent to call the tool again because it didn't get what it needed the first time. Simplify the returned data or split the tool so each call delivers something concrete.
- **Invalid arguments** typically mean the parameter description isn't clear enough and forces the agent to guess. Spell out the format and enumerate valid values in the description, not just the type.
- **Wrong tool selection** typically means descriptions overlap or boundaries aren't explicit. Tighten the "when to call" and "when not to call" lines.

## Additional resources

These resources cover what the loop can call, how multiple agents compose, and how to validate the result. For broader context on the pattern this guide builds on, see the LiveKit blog post on [the ReAct pattern in voice agents](https://livekit.com/blog/react-pattern-voice-agents).

- **[Function tools](https://docs.livekit.io/agents/logic/tools/definition.md)**: Define and register the tools your agent calls.

- **[Toolsets](https://docs.livekit.io/agents/logic/tools/toolsets.md)**: Group related tools and swap them as a unit at runtime.

- **[MCP servers](https://docs.livekit.io/agents/logic/tools/mcp.md)**: Connect to Model Context Protocol servers and filter the tools they expose.

- **[Agents and handoffs](https://docs.livekit.io/agents/logic/agents-handoffs.md)**: Transfer control between agents with different instructions or tools.

- **[Supervisor pattern](https://docs.livekit.io/agents/logic/supervisor-pattern.md)**: Keep one agent in control while delegating focused work to specialist tasks.

- **[Testing and evaluation](https://docs.livekit.io/agents/start/testing.md)**: Run representative tasks against your agent and iterate on what fails.

---

This document was rendered at 2026-08-28T04:22:13.012Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/tools/design.md](https://docs.livekit.io/agents/logic/tools/design.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-27"></a>
## Page 27: agents/logic/turns/turn-detector/
**Original URL:** https://docs.livekit.io/agents/logic/turns/turn-detector/  
**Source MD URL:** https://docs.livekit.io/agents/logic/turns/turn-detector.md

LiveKit docs › Build Agents › Logic & Structure › Turn detection & interruptions › Turn detector

---

# LiveKit turn detector

> Audio-based end-of-turn detection for voice AI.

## Overview

The LiveKit turn detector improves end-of-turn detection in voice AI apps by adding signals on top of voice activity detection (VAD).

Traditional VAD models are effective at determining the presence or absence of speech, but without understanding the meaning of speech they can provide a poor user experience. For instance, a user might say "I need to think about that for a moment" and then take a long pause. The user has more to say but a VAD-only system interrupts them anyway. A turn detector model can predict that they have more to say and wait for them to finish before responding.

## Audio turn detector

LiveKit's `TurnDetector` is an audio model that encodes user audio directly, capturing both _what_ is said and _how_ it's said. By combining semantic understanding with acoustic cues like intonation, pitch, and rhythm, it reaches state-of-the-art end-of-turn accuracy without relying on a transcript.

The following capture shows two sessions running side by side on the same audio. The text model is tricked by the mid-turn pauses and commits the turn early, while the audio model waits for the true end of turn:

**Turn detection comparison** (interactive timeline, not available in text):

[Listen to the audio sample](/audio/turns/eot-flight-booking.mp3).

- The audio end-of-turn model commits the user's turn at: 6.41s.
- The text (STT-based) end-of-turn model commits the turn at: 2.76s, 4.88s, 6.40s.

Transcript chunks (arrival time → text):

- 2.53s: "Hi. I'd like to book a flight"
- 4.85s: "from Dublin to New York."
- 6.14s: "This Friday."

The detector comes in two versions:

- **`v1`**: the full model, served on LiveKit Inference in every region. Highest accuracy. Available at no cost to agents deployed to LiveKit Cloud.
- **`v1-mini`**: a lightweight version that runs locally on CPU, free to use in any context at no additional cost. Recommended for agents not deployed to LiveKit Cloud.

If the full model is unavailable, the session automatically falls back to `v1-mini` for the rest of the session. See [Fallback to the mini model](#audio-fallback).

### Installation

The audio turn detector is built into the Agents SDK: `livekit-agents` 1.6.1 or later for Python, and `@livekit/agents` 1.4.7 or later for Node.js. No separate plugin or extra is required.

### Usage

Initialize your `AgentSession` with `TurnDetector`. `AgentSession` provides the required VAD automatically, and the model is selected based on your environment (see [Default model selection](#audio-default-model)).

**Python**:

```python
from livekit.agents import AgentSession, TurnHandlingOptions, inference

session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection=inference.TurnDetector(),
    ),
    # ... stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { inference, voice } from '@livekit/agents';

const session = new voice.AgentSession({
  turnHandling: {
    turnDetection: new inference.TurnDetector(),
  },
  // ... stt, tts, llm, etc.
});

```

To pin a specific version instead of relying on auto-selection, pass `version`:

**Python**:

```python
turn_detection=inference.TurnDetector(version="v1-mini")

```

---

**Node.js**:

```typescript
turnDetection: new inference.TurnDetector({ version: 'v1-mini' }),

```

See the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md) for a complete example.

> ℹ️ **Note**
> 
> Some STT models, such as [Deepgram Flux](https://docs.livekit.io/agents/models/stt/deepgram.md), include built-in end-of-turn detection. No special configuration is needed to use them alongside the audio turn detector: the configured turn detector takes precedence, and the session uses end-of-turn signals from the STT only when you set `turn_detection="stt"`.

### Parameters

The following parameters are available on the `TurnDetector` constructor:

- **`version`** _(Literal['v1', 'v1-mini'])_ (optional): Selects the model version. `v1` is the full model served on LiveKit Inference while `v1-mini` runs locally on CPU. When omitted, the version is selected automatically based on your environment. See [Default model selection](#audio-default-model).

- **`unlikely_threshold`** _(float | dict[str, float])_ (optional): Override the model's confidence threshold for ending a turn. Accepts a scalar (applied to every language) or a dict keyed by language code. Unmapped languages keep the calibrated default for the active model. See [Custom thresholds](#audio-custom-thresholds). In Node.js, this parameter is called `unlikelyThreshold`.

### Endpointing defaults

By default, the session waits between `0.5` and `3.0` seconds after speech to confirm the end of a turn. When you use the audio turn detector, the model provides a confident end-of-turn signal, so the session commits sooner with shorter [endpointing](https://docs.livekit.io/agents/logic/turns.md#endpointing-configuration) delays:

| Option | Default | With audio turn detector |
| `min_delay` | `0.5` seconds | `0.3` seconds |
| `max_delay` | `3.0` seconds | `2.5` seconds |

Override either value through [`EndpointingOptions`](https://docs.livekit.io/reference/agents/turn-handling-options.md#endpointingoptions). If the model doesn't return a prediction within about a second, the agent commits the turn anyway, and a timeout on the full `v1` model triggers a [fallback to `v1-mini`](#audio-fallback) for the rest of the session.

The audio turn detector requires VAD, and the VAD's `min_silence_duration` must be at least `0.25` seconds (250 ms). A lower value raises a `ValueError` when the session starts. The Silero VAD default of `0.55` seconds already satisfies this.

### Supported languages

The audio turn detector supports 14 languages: English, Arabic, German, Spanish, French, Hindi, Indonesian, Italian, Japanese, Korean, Dutch, Portuguese, Turkish, and Chinese.

When STT is enabled, the detector uses the language it reports to apply the right per-language threshold. To force a specific language, configure the [STT model](https://docs.livekit.io/agents/models/stt.md) with that language. The `language` parameter accepts any format supported by [`LanguageCode`](https://docs.livekit.io/agents/models/stt.md#language-codes). For example, to set Spanish:

**Python**:

```python
session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection=inference.TurnDetector(),
    ),
    stt=inference.STT(language="es"),
    # ... tts, llm, etc.
)

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
  turnHandling: {
    turnDetection: new inference.TurnDetector(),
  },
  stt: new inference.STT({ language: 'es' }),
  // ... tts, llm, etc.
});

```

When no STT is configured (for example, with a realtime model), the detector defaults to English thresholds.

### Custom thresholds

Each language has a calibrated `unlikely_threshold` that determines how confident the model must be before considering the user's turn complete. Lower values make the detector more eager to respond while higher values make it more patient.

Override the threshold globally with a scalar:

**Python**:

```python
inference.TurnDetector(unlikely_threshold=0.5)

```

---

**Node.js**:

```typescript
new inference.TurnDetector({ unlikelyThreshold: 0.5 });

```

Or override per language (unmapped languages keep the default):

**Python**:

```python
inference.TurnDetector(
    unlikely_threshold={
        "en": 0.5,
        "ja": 0.6,
    }
)

```

---

**Node.js**:

```typescript
new inference.TurnDetector({
  unlikelyThreshold: {
    en: 0.5,
    ja: 0.6,
  },
});

```

The two models ship with different calibrated defaults. When the session falls back from `v1` to `v1-mini` mid-session, your override is rescaled to preserve its relationship to the calibrated defaults of the active model.

### Realtime model usage

Because the audio turn detector doesn't depend on a transcript, you can use it with a realtime model without adding an STT plugin. You still need to disable the realtime model's built-in turn detection so the two systems don't conflict.

**Python**:

```python
from livekit.agents import AgentSession, TurnHandlingOptions, inference
from livekit.plugins import openai

session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection=inference.TurnDetector(),
    ),
    llm=openai.realtime.RealtimeModel(
        voice="alloy",
        # Disable the model's built-in turn detection to use
        # the LiveKit audio turn detector instead
        turn_detection=None,
    ),
)

```

---

**Node.js**:

```typescript
import { inference, voice } from '@livekit/agents';
import * as openai from '@livekit/agents-plugin-openai';

const session = new voice.AgentSession({
  turnHandling: {
    turnDetection: new inference.TurnDetector(),
  },
  llm: new openai.realtime.RealtimeModel({
    voice: 'alloy',
    // Disable the model's built-in turn detection to use
    // the LiveKit audio turn detector instead
    turnDetection: null,
  }),
});

```

### Default model selection

When you don't set the `version` parameter, the detector picks a version based on your environment:

| Environment | Default version |
| Agent deployed to LiveKit Cloud | `v1` (full model) |
| Local development (`dev` mode) with LiveKit Cloud credentials | `v1` (full model) |
| Agent deployed to another environment (`start` command) | `v1-mini` (runs locally) |

Local development includes a free monthly allowance of the full model on every plan. When the allowance is exhausted, the session falls back to `v1-mini` automatically. To learn more, see [Quotas and limits](https://docs.livekit.io/deploy/admin/quotas-and-limits.md#audio-turn-detection). To pin one version in every environment, set `version` explicitly.

If you don't pass `turn_detection` to `AgentSession` at all, the session uses a `TurnDetector` by default, unless your LLM is a realtime model that provides its own server-side turn detection.

When `v1-mini` runs (in production outside LiveKit Cloud, or after a fallback), it executes in a shared CPU process. Use compute-optimized instances (such as AWS c6i or c7i) rather than burstable instances (such as AWS t3 or t4g) to avoid inference timeouts from CPU credit limits.

### Fallback to the mini model

When the full `v1` model is active, the detector monitors for connection failures and prediction timeouts. A connection failure includes the case where the agent can't reach LiveKit Inference at all (for example, the free allowance is exhausted). If either occurs, the session does the following:

1. Logs a warning (once per session).
2. Emits a default probability (`1.0`) for any in-flight prediction so the current turn isn't blocked.
3. Swaps to `v1-mini` for the rest of the session.
4. Rescales any custom `unlikely_threshold` to preserve its relationship to the mini model's calibrated defaults.

The fallback is sticky for the lifetime of the session. The next session starts fresh and attempts the full model again.

If `v1-mini` isn't available (for example, the binary failed to load), the detector emits the default probability for each turn and retries on the next turn. The full model is also retried on each new session.

### Benchmarks

LiveKit benchmarks the audio turn detector against other end-of-turn models using [eot-bench](https://github.com/livekit/eot-bench), an open source harness that simulates the live turn-taking decisions a production voice agent makes against natural, task-oriented conversations. See the repository for the current methodology and results.

For a deeper look at the model architecture and evaluation approach, see the [LiveKit blog](https://livekit.com/blog/solving-end-of-turn-detection).

## Text turn detector

> 🔥 **Deprecated**
> 
> The text turn detector is deprecated and slated for removal in version 2.0 of the LiveKit Agents SDK. Use the [audio turn detector](#audio-turn-detector) for new agents. It remains available for cases where you can't use LiveKit Inference and need a fully open-weights, self-contained option, but no longer receives feature work.

The text turn detector is an open-weights language model that adds conversational context as an additional signal to VAD using transcripts from your STT pipeline.

For more general information about the model, read about it on the [LiveKit blog](https://blog.livekit.io/improved-end-of-turn-model-cuts-voice-ai-interruptions-39/).

### Requirements

The text turn detector is designed for use inside an `AgentSession` and also requires an [STT model](https://docs.livekit.io/agents/models/stt.md). If you're using a realtime model, you must include a separate STT model to use this detector.

LiveKit recommends also using the [Silero VAD plugin](https://docs.livekit.io/agents/logic/turns/vad.md) for maximum performance, but you can rely on your STT plugin's endpointing instead if you prefer.

The model is deployed globally on LiveKit Cloud, and agents deployed there automatically use this optimized inference service.

For custom agent deployments, the model runs locally on the CPU in a shared process and requires <`500` MB of RAM. Use compute-optimized instances (such as AWS c6i or c7i) rather than burstable instances (such as AWS t3 or t4g) to avoid inference timeouts due to CPU credit limits.

### Installation

Install the plugin.

**Python**:

Install the plugin from PyPI:

```shell
uv add "livekit-agents[turn-detector]~=1.5"

```

---

**Node.js**:

Install the plugin from npm:

```shell
pnpm install @livekit/agents-plugin-livekit

```

### Usage

Initialize your `AgentSession` with the `MultilingualModel` and an STT model. These examples use LiveKit Inference for STT, but more options [are available](https://docs.livekit.io/agents/models/stt.md).

**Python**:

```python
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.agents import AgentSession, inference, TurnHandlingOptions

session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection=MultilingualModel(),
    ),
    stt=inference.STT(language="multi"),
    # ... vad, stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice, inference } from '@livekit/agents';
import * as livekit from '@livekit/agents-plugin-livekit';

const session = new voice.AgentSession({
  stt: new inference.STT({ language: 'multi' }),
  turnHandling: {
    turnDetection: new livekit.turnDetector.MultilingualModel(),
  },
  // ... vad, stt, tts, llm, etc.
});

```

### Parameters

The text turn detector itself has no configuration, but you can configure the following endpointing parameters in the turn handling options passed to the `AgentSession`. To learn more, see [EndpointingOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#endpointingoptions).

- **`mode`** _(Literal['dynamic', 'fixed'])_ (optional) - Default: `fixed`: Endpointing timing behavior. The endpointing delay is the time the agent waits before terminating the users's turn.

- `"fixed"` - Use the configured `min_delay` and `max_delay` values to determine the endpointing delay.
- `"dynamic"` - Adapt the delay within the `min_delay` and `max_delay` range based on session pause statistics (exponential moving average of between-utterance and between-turn pauses). Suits most conversations.

- **`min_delay`** _(float)_ (optional) - Default: `0.5 seconds`: Minimum time (in seconds) to wait since the last detected speech to declare the user's turn to be complete.

With [dynamic endpointing](https://docs.livekit.io/reference/agents/turn-handling-options.md#dynamic-endpointing), this is the lower bound. The agent might use a longer effective delay when session pause statistics suggest slower turn-taking.

- In VAD mode, this effectively behaves like `max(VAD silence, min_delay)`.
- In STT mode, this is applied _after_ the STT end-of-speech signal, and therefore in addition to the STT provider's endpointing delay.

- **`max_delay`** _(float)_ (optional) - Default: `3.0 seconds`: Maximum time (in seconds) the agent waits before terminating the turn. This prevents the agent from waiting indefinitely for the user to continue speaking.

With [dynamic endpointing](https://docs.livekit.io/reference/agents/turn-handling-options.md#dynamic-endpointing), this is the upper bound. The agent might use a shorter effective delay when session pause statistics suggest faster turn-taking.

- **`alpha`** _(float)_ (optional) - Default: `0.9`: Exponential moving average (EMA) coefficient for [dynamic endpointing](https://docs.livekit.io/reference/agents/turn-handling-options.md#dynamic-endpointing). Higher values give more weight to accumulated history, so the learned delay adapts more slowly. Lower values react faster to recent pauses. Only applies when `mode` is `"dynamic"`.

> ℹ️ **Note**
> 
> When you use the [audio turn detector](https://docs.livekit.io/agents/logic/turns/turn-detector.md#audio-turn-detector), any `min_delay` and `max_delay` values you don't set default to `0.3` and `2.5` seconds instead of `0.5` and `3.0`. The model provides a confident end-of-turn signal, so the agent can commit sooner. See [Endpointing defaults](https://docs.livekit.io/agents/logic/turns/turn-detector.md#audio-endpointing).

> ℹ️ **Time units**
> 
> In Node.js, `min_delay` and `max_delay` are in milliseconds (for example, `500` and `3000`). Python uses seconds (for example, `0.5` and `3.0`).

### Supported languages

The `MultilingualModel` supports English and 13 other languages. The model relies on your [STT model](https://docs.livekit.io/agents/models/stt.md) to report the language of the user's speech. To set the language to a fixed value, configure the STT model with a specific language. The `language` parameter accepts any format supported by [`LanguageCode`](https://docs.livekit.io/agents/models/stt.md#language-codes). For example, to force the model to use Spanish:

**Python**:

```python
session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection=MultilingualModel(),
    ),
    stt=inference.STT(language="es"),
    # ... vad, stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice, inference } from '@livekit/agents';
import * as livekit from '@livekit/agents-plugin-livekit';

const session = new voice.AgentSession({
  stt: new inference.STT({ language: 'es' }),
  turnHandling: {
    turnDetection: new livekit.turnDetector.MultilingualModel(),
  },
  // ... vad, stt, tts, llm, etc.
});

```

The model currently supports English, Spanish, French, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Indonesian, Turkish, Russian, and Hindi.

### Realtime model usage

Realtime models like the OpenAI Realtime API produce user transcripts after the end of the turn, rather than incrementally while the user speaks. The text turn detector requires live STT results to operate, so you must provide an STT plugin to the `AgentSession` to use it with a realtime model. This incurs extra cost for the STT model.

You must also disable the realtime model's built-in turn detection so it doesn't conflict with the LiveKit turn detector. The following example demonstrates how to do this with the OpenAI Realtime API:

**Python**:

```python
from livekit.agents import AgentSession, TurnHandlingOptions
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins import deepgram, openai, silero

session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection=MultilingualModel(),
    ),
    vad=silero.VAD.load(),
    stt=deepgram.STT(),
    # OpenAI Realtime API
    llm=openai.realtime.RealtimeModel(
        voice="alloy",
        # Disable the model's built-in turn detection to use
        # the LiveKit turn detector instead
        turn_detection=None,
        input_audio_transcription=None,  # use Deepgram STT instead
    ),
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import * as deepgram from '@livekit/agents-plugin-deepgram';
import * as livekit from '@livekit/agents-plugin-livekit';
import * as openai from '@livekit/agents-plugin-openai';
import * as silero from '@livekit/agents-plugin-silero';

const session = new voice.AgentSession({
  turnHandling: {
    turnDetection: new livekit.turnDetector.MultilingualModel(),
  },
  vad: await silero.VAD.load(),
  stt: new deepgram.STT(),
  // OpenAI Realtime API
  llm: new openai.realtime.RealtimeModel({
    voice: 'alloy',
    // Disable the model's built-in turn detection to use
    // the LiveKit turn detector instead
    turnDetection: null,
    inputAudioTranscription: null, // use Deepgram STT instead
  }),
});

```

### Benchmarks

The following data shows the expected performance of the text turn detector model.

#### Runtime performance

The size on disk and typical CPU inference time for the text turn detector model is as follows:

| Model | Base Model | Size on Disk | Per Turn Latency |
| Multilingual | [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | 396 MB | ~50-160 ms |

#### Detection accuracy

The following tables show accuracy metrics for the text turn detector model in each supported language.

- **True positive** means the model correctly identifies the user has finished speaking.
- **True negative** means the model correctly identifies the user will continue speaking.

| Language | True Positive Rate | True Negative Rate |
| Hindi | 99.4% | 96.30% |
| Korean | 99.3% | 94.50% |
| French | 99.3% | 88.90% |
| Portuguese | 99.4% | 87.40% |
| Indonesian | 99.3% | 89.40% |
| Russian | 99.3% | 88.00% |
| English | 99.3% | 87.00% |
| Chinese | 99.3% | 86.60% |
| Japanese | 99.3% | 88.80% |
| Italian | 99.3% | 85.10% |
| Spanish | 99.3% | 86.00% |
| German | 99.3% | 87.80% |
| Turkish | 99.3% | 87.30% |
| Dutch | 99.3% | 88.10% |

### Resources

The following resources cover the open-weights text turn detector:

- **[Plugin reference](https://docs.livekit.io/reference/python/livekit/plugins/turn_detector/index.html.md)**: Reference for the `livekit-plugins-turn-detector` package.

- **[GitHub repo](https://github.com/livekit/agents/tree/main/livekit-plugins/livekit-plugins-turn-detector)**: View the source or contribute to the text turn detector plugin.

- **[LiveKit Model License](https://huggingface.co/livekit/turn-detector/blob/main/LICENSE)**: LiveKit Model License used for the text turn detector and the `v1-mini` model.

## Additional resources

- **[Audio turn detector deep dive](https://livekit.com/blog/solving-end-of-turn-detection)**: Model architecture, benchmarks, and evaluation methodology on the LiveKit blog.

- **[Evaluation harness](https://github.com/livekit/eot-bench)**: Open source harness for benchmarking end-of-turn models under production endpointing policies.

- **[Evaluation datasets](https://huggingface.co/datasets/livekit/eot-evals)**: Open source English and multilingual end-of-turn test datasets on Hugging Face.

---

This document was rendered at 2026-08-28T04:22:13.063Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/turns/turn-detector.md](https://docs.livekit.io/agents/logic/turns/turn-detector.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-28"></a>
## Page 28: agents/logic/turns/adaptive-interruption-handling/
**Original URL:** https://docs.livekit.io/agents/logic/turns/adaptive-interruption-handling/  
**Source MD URL:** https://docs.livekit.io/agents/logic/turns/adaptive-interruption-handling.md

LiveKit docs › Build Agents › Logic & Structure › Turn detection & interruptions › Adaptive interruption handling

---

# Adaptive interruption handling

> Distinguish between true interruptions and conversational backchanneling.

> ℹ️ **Available for agents deployed to LiveKit Cloud**
> 
> Adaptive interruption handling is available for agents deployed to LiveKit Cloud. For details, see [quota and limits](#quota-and-limits).

## Overview

Adaptive interruption handling allows an agent to respond naturally when users speak mid-response. Instead of relying on fixed timing or volume thresholds, the model analyzes the acoustic signals to identify intentional interruptions (barge-ins) from conversational backchanneling.

Backchanneling includes short listener cues such as "uh-huh," "okay," or "right" that indicate attention but don't require a response. By filtering these out, the agent avoids unnecessary turn switches caused by brief acknowledgments, incidental sounds, or background noise. The result is smoother, more natural interactions.

> ℹ️ **Agents SDK version**
> 
> Adaptive interruption handling requires the latest Agents SDK versions:
> 
> - Python SDK v1.5.0 or greater
> - Node.js SDK v1.2.0 or greater

[Video: Adaptive interruption handling demo](https://www.youtube.com/watch?v=DSXCE7D4Kvs)

## How it works

The adaptive interruption (barge-in) model is trained on real conversational audio to distinguish true interruption attempts from non-interruptive speech. It operates after voice activity detection (VAD) identifies incoming user audio.

Instead of immediately stopping the agent whenever speech is detected, the model analyzes the audio to determine whether the agent should actually yield the turn. Because the decision is based on acoustic signals rather than waiting for a transcript, the model can respond faster and reduce unnecessary interruptions.

> ℹ️ **Language support**
> 
> The adaptive interruption model is meant to be used with any spoken language. It might perform better with English in some cases, but in most cases it works with any language.

![Diagram of adaptive interruption handling model architecture.](/images/agents/adaptive-interruption-diagram.png)

## How to use

Adaptive interruption handling is available in LiveKit Cloud and is enabled by default if the following conditions are met:

- Agent is [deployed to LiveKit Cloud](https://docs.livekit.io/agents/deploy.md) or running in dev mode.
- VAD is enabled.
- LLM is not a realtime model.
- STT model supports [aligned transcripts](#aligned-transcripts).

Otherwise, the default behavior is to rely on VAD for interruption detection.

> ℹ️ **Availability and usage limitations**
> 
> Adaptive interruption handling is available for unlimited usage to agents deployed to LiveKit Cloud. It's also available for local development with usage limitations.

You can also explicitly set the interruption `mode` to `"adaptive"` in the turn handling options:

**Python**:

```python
session = AgentSession(
    # ... stt, llm, tts, vad
    turn_handling=TurnHandlingOptions(
        turn_detection=inference.TurnDetector(),
        interruption={
            "mode": "adaptive",
        },
    ),
)

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
  // ... stt, llm, tts, vad
  turnHandling: {
    turnDetection: new inference.TurnDetector(),
    interruption: {
      mode: 'adaptive',
    },
  },
});

```

## Audio samples

Compare the following audio samples to see how the agent responds to interruptions and non-interruptions with and without adaptive interruption handling.

### Using adaptive interruption handling

The following samples have adaptive interruption handling enabled and demonstrate how the agent ignores the speaker's brief acknowledgments signaling attention, but responds to genuine interruptions (barge-ins).

**Audio comparison** (audio-only, not available in text):

- Backchannel (non-interruption)
- Genuine interruption (barge-in)

### Without adaptive interruption handling

This sample uses VAD-only detection. Without adaptive interruption handling, the agent is interrupted by the speaker's brief acknowledgment of the agent's response.

**Audio comparison** (audio-only, not available in text):

- VAD-only detection

## Performance

The adaptive interruption model analyzes streaming audio chunks during overlapping speech to determine whether a detected speech segment is a true interruption.

The model runs in every region on LiveKit Cloud's inference infrastructure and adds minimal latency to the interruption pipeline. When agents are deployed to LiveKit Cloud, they run in the same data centers as the inference service, further reducing end-to-end latency.

## Turn boundary cooldown

Available in:
- [ ] Node.js
- [x] Python

At the beginning or end of an agent's turn, the adaptive model can mistake a real interruption for a backchannel. The following are two common cases:

- Immediately after the agent starts speaking, a user correction or change of mind might be incorrectly filtered out as a backchannel.
- Just before the agent stops speaking, a short answer to its final question might be incorrectly discarded as overlap if the STT transcript arrives too late.

The `backchannel_boundary` option defines a cooldown window around each agent turn to handle both cases. The default start and end cooldown values are `(1.0, 1.0)`:

- Start cooldown of `1.0` seconds: adaptive detection is suppressed for the first second after the agent starts speaking. VAD-based interruption is used instead during this window, so true barge-ins still pass through.
- End cooldown of `1.0` seconds: late STT transcripts whose timestamps fall within the last second of agent speech are included as a real user turn instead of being discarded as overlap.

The end value accounts for imprecise STT transcript timestamps; increase it if your STT provider delivers transcripts with a longer delay. Pass a single `float` to use the same value for both sides, or `None` to disable the cooldown entirely.

The following example tunes both sides of the boundary. Pass it to the `turn_handling` parameter of `AgentSession`:

```python
turn_handling = {
    "interruption": {"backchannel_boundary": (0.5, 2.0)},
}

```

For the full parameter reference, see [`backchannel_boundary`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions-parameters).

## Quota and limits

Adaptive interruption handling is included at no extra cost for all agents deployed to LiveKit Cloud.

For local development and testing, every plan includes 40,000 free inference requests per month.

## Aligned transcripts support

An aligned transcript includes timing information that allows you to synchronize the transcript with the audio. Each word or chunk of speech is assigned a start and end timestamp. Support for aligned transcripts is required for [adaptive interruption handling](https://docs.livekit.io/agents/logic/turns/adaptive-interruption-handling.md). All STT models provided by [LiveKit Inference](https://docs.livekit.io/agents/models.md#inference) support aligned transcripts.

For plugins, you can determine if the model supports aligned transcripts by checking the `capabilities.aligned_transcript` property:

**Python**:

```python
if stt.capabilities.aligned_transcript:
    print("This STT model supports aligned transcripts.")

```

---

**Node.js**:

```typescript
if (stt.capabilities.alignedTranscript) {
    console.log("This STT model supports aligned transcripts.");
}

```

## Metrics and usage

When adaptive interruption handling is enabled, an agent session collects interruption metrics for each barge-in detection, including per-event latency, and the number of requests and interruptions. `InterruptionMetrics` events are available through per-plugin metrics listeners. See the [metrics reference](https://docs.livekit.io/deploy/observability/data.md#metrics-reference) for the full list of fields.

Interruption model usage, including total requests per provider and model, is available in `session.usage`. See [Session usage](https://docs.livekit.io/deploy/observability/data.md#session-usage) for details.

To learn more, see [Metrics and usage](https://docs.livekit.io/deploy/observability/data.md#metrics).

## Turn off adaptive interruption handling

To use VAD-only interruption detection instead of adaptive handling, set the interruption `mode` to `"vad"` in the turn handling options:

**Python**:

```python
turn_handling = {
    "interruption": {
        "mode": "vad",
    },
}

```

---

**Node.js**:

```typescript
const turnHandling = {
  interruption: {
    mode: 'vad',
  },
};

```

To disable interruption handling entirely, set `enabled` to `false` in the [interruption options](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions). This means the agent cannot be interrupted by user speech.

---

This document was rendered at 2026-08-28T04:22:13.081Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/turns/adaptive-interruption-handling.md](https://docs.livekit.io/agents/logic/turns/adaptive-interruption-handling.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-29"></a>
## Page 29: agents/logic/turns/vad/
**Original URL:** https://docs.livekit.io/agents/logic/turns/vad/  
**Source MD URL:** https://docs.livekit.io/agents/logic/turns/vad.md

LiveKit docs › Build Agents › Logic & Structure › Turn detection & interruptions › Silero VAD plugin

---

# Silero VAD plugin

> High-performance voice activity detection for LiveKit Agents.

## Overview

The Silero VAD plugin provides voice activity detection (VAD) that contributes to accurate [turn detection](https://docs.livekit.io/agents/logic/turns.md) in voice AI applications.

VAD is a crucial component for voice AI applications as it helps determine when a user is speaking versus when they are silent. This enables natural turn-taking in conversations and helps optimize resource usage by only performing speech-to-text while the user speaks.

LiveKit recommends using the Silero VAD plugin in combination with the custom [turn detector model](https://docs.livekit.io/agents/logic/turns/turn-detector.md) for the best performance.

## Quick reference

The following sections provide a quick overview of the Silero VAD plugin. For more information, see [Additional resources](#additional-resources).

### Requirements

The model runs locally on the CPU and requires minimal system resources.

### Installation

Install the Silero VAD plugin.

**Python**:

Install the plugin from PyPI:

```shell
uv add "livekit-agents[silero]~=1.5"

```

---

**Node.js**:

Install the plugin from npm:

```shell
pnpm install @livekit/agents-plugin-silero

```

### Usage

Initialize your `AgentSession` with the Silero VAD plugin:

**Python**:

```python
from livekit.plugins import silero

session = AgentSession(
    vad=silero.VAD.load(),
    # ... stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import * as silero from '@livekit/agents-plugin-silero';

const session = new voice.AgentSession({
  vad: await silero.VAD.load(),
  // ... stt, tts, llm, etc.
});

```

## Prewarm

You can [prewarm](https://docs.livekit.io/agents/server/options.md#prewarm) the plugin to improve load times for new jobs:

**Python**:

```python
from livekit.agents import AgentServer


server = AgentServer()


def prewarm(proc: agents.JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


server.setup_fnc = prewarm

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: agents.JobContext):
    session = AgentSession(
        vad=ctx.proc.userdata["vad"],
        # ... stt, tts, llm, etc.
    )

    # ... session.start etc ...


if __name__ == "__main__":
    agents.cli.run_app(server)

```

---

**Node.js**:

```typescript
import { voice, defineAgent, cli, ServerOptions, type JobContext, type JobProcess } from '@livekit/agents';
import * as silero from '@livekit/agents-plugin-silero';
import { fileURLToPath } from 'node:url';

export default defineAgent({
  prewarm: async (proc: JobProcess) => {
    proc.userData.vad = await silero.VAD.load();
  },
  entry: async (ctx: JobContext) => {
    const vad = ctx.proc.userData.vad! as silero.VAD;

    const session = new voice.AgentSession({
      vad,
      // ... stt, tts, llm, etc.
    });

    // ... session.start etc ...
  },
});

cli.runApp(new ServerOptions({ agent: fileURLToPath(import.meta.url) }));

```

## Configuration

The following parameters are available on the `load` method:

- **`min_speech_duration`** _(float)_ (optional) - Default: `0.05`: Minimum duration of speech required to start a new speech chunk.

- **`min_silence_duration`** _(float)_ (optional) - Default: `0.55`: Duration of silence to wait after speech ends to determine if the user has finished speaking.

- **`prefix_padding_duration`** _(float)_ (optional) - Default: `0.5`: Duration of padding to add to the beginning of each speech chunk.

- **`max_buffered_speech`** _(float)_ (optional) - Default: `60.0`: Maximum duration of speech to keep in the buffer (in seconds).

- **`activation_threshold`** _(float)_ (optional) - Default: `0.5`: Threshold to consider a frame as speech. A higher threshold results in more conservative detection but might miss soft speech. A lower threshold results in more sensitive detection, but might identify noise as speech.

- **`sample_rate`** _(Literal[8000, 16000])_ (optional) - Default: `16000`: Sample rate for the inference (only 8KHz and 16KHz are supported).

- **`force_cpu`** _(bool)_ (optional) - Default: `True`: Force the use of CPU for inference.

## Additional resources

The following resources provide more information about using the LiveKit Silero VAD plugin.

- **[Python package](https://pypi.org/project/livekit-plugins-silero/)**: The `livekit-plugins-silero` package on PyPI.

- **[Plugin reference](https://docs.livekit.io/reference/python/livekit/plugins/silero/index.html.md#livekit.plugins.silero.VAD)**: Reference for the LiveKit Silero VAD plugin.

- **[GitHub repo](https://github.com/livekit/agents/tree/main/livekit-plugins/livekit-plugins-silero)**: View the source or contribute to the LiveKit Silero VAD plugin.

- **[Silero VAD project](https://github.com/snakers4/silero-vad)**: The open source VAD model that powers the LiveKit Silero VAD plugin.

- **[Transcriber](https://docs.livekit.io/reference/recipes/transcriber.md)**: An example using standalone VAD and STT outside of an `AgentSession`.

---

This document was rendered at 2026-08-28T04:22:13.093Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/turns/vad.md](https://docs.livekit.io/agents/logic/turns/vad.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-30"></a>
## Page 30: agents/logic/turns/tuning/
**Original URL:** https://docs.livekit.io/agents/logic/turns/tuning/  
**Source MD URL:** https://docs.livekit.io/agents/logic/turns/tuning.md

LiveKit docs › Build Agents › Logic & Structure › Turn detection & interruptions › Turn-taking tuning

---

# Turn-taking tuning

> Tune turn detection, endpointing, interruption, and preemptive generation for natural, low-latency conversations.

## Overview

Turn-taking in voice AI involves several stages of the agent pipeline:

- **User activity detection** decides when the user has finished a turn so the agent can reply. Options include turn detection mode, endpointing delays, and endpointing mode.
- **Interruption handling** decides when the user can cut the agent off mid-response. Options include enable/disable, detection mode, interruption thresholds, and false-interruption recovery.
- **Preemptive generation** lets the LLM (and optionally TTS) start work before the user's turn is fully confirmed. Options include enable/disable, preemptive TTS, max speech duration, and max retries.
- **Audio pre-processing** (noise cancellation, automatic gain control) cleans the input before any of these stages run. Options include voice isolation and background noise suppression.
- **Agent speech scheduling** controls the cadence of the agent's own utterances. Options include the minimum gap between agent utterances (Python only).

The defaults are reasonable for most apps, but tuning matters when you're chasing low latency, working in noisy environments, or seeing specific symptoms like the agent cutting users off. This page gives a recommended starting config, a full reference of the options that affect each stage, and a troubleshooting table mapping common symptoms to the options that fix them.

For a deeper reference on each parameter, see [TurnHandlingOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md).

## Configuration

The next two sections cover a recommended starting config and a full options reference.

### Recommended starting config

A starting point for a voice agent that needs to respond quickly in environments with background noise or other speakers. See [All options](#all-options) for what each parameter does.

**Python**:

```python
from livekit.agents import AgentSession, TurnHandlingOptions, inference, room_io
from livekit.plugins import ai_coustics

session = AgentSession(
    turn_handling=TurnHandlingOptions(
        turn_detection=inference.TurnDetector(),
        endpointing={
            "mode": "fixed",
            "min_delay": 0.5,
            "max_delay": 3.0,
        },
        interruption={
            "mode": "adaptive",
            "min_duration": 0.5,
            "min_words": 0,
        },
        # preemptive_generation is enabled by default. Opt into preemptive TTS
        # for lower latency at the cost of wasted compute on cancellations.
        preemptive_generation={
            "preemptive_tts": False,
        },
    ),
    # ... stt, tts, llm, etc.
)

await session.start(
    # ...,
    room_options=room_io.RoomOptions(
        audio_input=room_io.AudioInputOptions(
            noise_cancellation=ai_coustics.audio_enhancement(
                model=ai_coustics.EnhancerModel.QUAIL_VF_L,
            ),
        ),
    ),
)

```

---

**Node.js**:

```typescript
import { inference, voice } from '@livekit/agents';
import * as aiCoustics from '@livekit/plugins-ai-coustics';

const session = new voice.AgentSession({
  turnHandling: {
    turnDetection: new inference.TurnDetector(),
    endpointing: {
      minDelay: 500,
      maxDelay: 3000,
    },
    interruption: {
      mode: 'adaptive',
      minDuration: 500,
      minWords: 0,
    },
    // preemptiveGeneration is enabled by default. Opt into preemptive TTS
    // for lower latency at the cost of wasted compute on cancellations.
    preemptiveGeneration: {
      preemptiveTts: false,
    },
  },
  // ... stt, tts, llm, etc.
});

await session.start({
  // ...,
  inputOptions: {
    noiseCancellation: aiCoustics.audioEnhancement({ model: 'quailVfL' }),
  },
});

```

For quieter environments, drop the noise cancellation argument from `session.start()`. The rest of the config still applies.

For SIP participants, swap voice isolation for the telephony-tuned Krisp model: `noise_cancellation.BVCTelephony()` (Python) or `TelephonyBackgroundVoiceCancellation()` (Node.js). For multi-speaker rooms, use [background noise suppression](https://docs.livekit.io/transport/media/noise-cancellation.md#agents-background-noise-suppression) instead of voice isolation.

### All options

The following table lists the options that affect turn-taking, grouped by pipeline stage.

**Python**:

| Option | Stage | What it controls | Default |
| [`turn_detection`](https://docs.livekit.io/reference/agents/turn-handling-options.md#turnhandlingoptions) mode | User activity detection | How the session decides the user is done speaking. Options: turn detector model, VAD, STT endpointing, realtime LLM, manual. | Auto-selected |
| [`endpointing.min_delay`](https://docs.livekit.io/reference/agents/turn-handling-options.md#endpointingoptions-parameters) | User activity detection | Minimum time after detected silence before the turn closes. In VAD mode this is `max(VAD silence, min_delay)`. In STT mode it adds to the provider's endpoint signal. | `0.5 seconds` |
| [`endpointing.max_delay`](https://docs.livekit.io/reference/agents/turn-handling-options.md#endpointingoptions-parameters) | User activity detection | Maximum time the agent waits before forcing the turn closed. | `3.0 seconds` |
| [`endpointing.mode`](https://docs.livekit.io/reference/agents/turn-handling-options.md#endpointingoptions-parameters) | User activity detection | `"fixed"` always uses the configured delays. `"dynamic"` adapts within the range based on session pause statistics. | `"fixed"` |
| [`interruption.enabled`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Master on/off toggle for interruptions. Set to `False` to make the agent uninterruptible. | `True` |
| [`interruption.mode`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | `"adaptive"` (recommended) uses an audio model to distinguish real interruptions from backchannel acknowledgments. `"vad"` triggers on any detected speech. | `"adaptive"` if available, otherwise `"vad"` |
| [`interruption.min_duration`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Minimum speech duration to register as an interruption. | `0.5 seconds` |
| [`interruption.min_words`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Minimum word count to register as an interruption. Requires STT. | `0` |
| [`interruption.false_interruption_timeout`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Silence window after a detected interruption before it's classified as false. After this elapses with no transcript, the agent can resume (see `resume_false_interruption`). | `2.0 seconds` |
| [`interruption.resume_false_interruption`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Whether to resume the interrupted speech after the false-interruption timeout passes. | `True` |
| [`preemptive_generation.enabled`](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) | Preemptive generation | Whether to start LLM generation as soon as a final transcript arrives, before the turn is confirmed. | `True` |
| [`preemptive_generation.preemptive_tts`](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) | Preemptive generation | Also start TTS preemptively. Cuts more latency at the cost of wasted compute on cancellations. | `False` |
| [`preemptive_generation.max_speech_duration`](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) | Preemptive generation | Skip preemptive generation for utterances longer than this. Long turns are more likely to mutate. | `10.0 seconds` |
| [`preemptive_generation.max_retries`](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) | Preemptive generation | Cap on preemptive attempts per turn. Resets when the turn completes. | `3` |
| [Voice isolation](https://docs.livekit.io/transport/media/noise-cancellation.md#agents-voice-isolation) | Audio pre-processing | Suppresses competing voices in the input so STT, VAD, and the turn detector see clean audio. Models include ai-coustics QUAIL_VF_L, Krisp BVC, and Krisp BVCTelephony. | Off |
| [Background noise suppression](https://docs.livekit.io/transport/media/noise-cancellation.md#agents-background-noise-suppression) | Audio pre-processing | Suppresses non-speech noise. Use when the main challenge is environmental noise rather than competing speakers. | Off |
| [`min_consecutive_speech_delay`](https://docs.livekit.io/agents/logic/sessions.md#user-interaction) | Agent speech scheduling | Minimum gap between consecutive agent utterances. Does not affect user-side turn detection. | `0.0 seconds` |

---

**Node.js**:

| Option | Stage | What it controls | Default |
| [`turnDetection`](https://docs.livekit.io/reference/agents/turn-handling-options.md#turnhandlingoptions) mode | User activity detection | How the session decides the user is done speaking. Options: turn detector model, VAD, STT endpointing, realtime LLM, manual. | Auto-selected |
| [`endpointing.minDelay`](https://docs.livekit.io/reference/agents/turn-handling-options.md#endpointingoptions-parameters) | User activity detection | Minimum time after detected silence before the turn closes. In VAD mode this is `max(VAD silence, minDelay)`. In STT mode it adds to the provider's endpoint signal. | `500 ms` |
| [`endpointing.maxDelay`](https://docs.livekit.io/reference/agents/turn-handling-options.md#endpointingoptions-parameters) | User activity detection | Maximum time the agent waits before forcing the turn closed. | `3000 ms` |
| [`interruption.enabled`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Master on/off toggle for interruptions. Set to `false` to make the agent uninterruptible. | `true` |
| [`interruption.mode`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | `"adaptive"` (recommended) uses an audio model to distinguish real interruptions from backchannel acknowledgments. `"vad"` triggers on any detected speech. | `"adaptive"` if available, otherwise `"vad"` |
| [`interruption.minDuration`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Minimum speech duration to register as an interruption. | `500 ms` |
| [`interruption.minWords`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Minimum word count to register as an interruption. Requires STT. | `0` |
| [`interruption.falseInterruptionTimeout`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Silence window after a detected interruption before it's classified as false. After this elapses with no transcript, the agent can resume (see `resumeFalseInterruption`). | `2000 ms` |
| [`interruption.resumeFalseInterruption`](https://docs.livekit.io/reference/agents/turn-handling-options.md#interruptionoptions) | Interruption handling | Whether to resume the interrupted speech after the false-interruption timeout passes. | `true` |
| [`preemptiveGeneration.enabled`](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) | Preemptive generation | Whether to start LLM generation as soon as a final transcript arrives, before the turn is confirmed. | `true` |
| [`preemptiveGeneration.preemptiveTts`](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) | Preemptive generation | Also start TTS preemptively. Cuts more latency at the cost of wasted compute on cancellations. | `false` |
| [`preemptiveGeneration.maxSpeechDuration`](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) | Preemptive generation | Skip preemptive generation for utterances longer than this. Long turns are more likely to mutate. | `10000 ms` |
| [`preemptiveGeneration.maxRetries`](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) | Preemptive generation | Cap on preemptive attempts per turn. Resets when the turn completes. | `3` |
| [Voice isolation](https://docs.livekit.io/transport/media/noise-cancellation.md#agents-voice-isolation) | Audio pre-processing | Suppresses competing voices in the input so STT, VAD, and the turn detector see clean audio. Models include ai-coustics QUAIL_VF_L, Krisp BVC, and Krisp BVCTelephony. | Off |
| [Background noise suppression](https://docs.livekit.io/transport/media/noise-cancellation.md#agents-background-noise-suppression) | Audio pre-processing | Suppresses non-speech noise. Use when the main challenge is environmental noise rather than competing speakers. | Off |

## Troubleshooting

The following table maps common turn-taking complaints to the options that affect them.

| Symptom | Likely options |
| Agent cuts users off mid-thought. | Switch `turn_detection` to the [turn detector model](https://docs.livekit.io/agents/logic/turns/turn-detector.md). Raise `endpointing.min_delay`. Switch `interruption.mode` to `"adaptive"` if it isn't already. Add [voice isolation](https://docs.livekit.io/transport/media/noise-cancellation.md#agents-voice-isolation) if cross-talk or noise is causing false speech detection. |
| Agent is interrupted by short acknowledgments ("uh-huh," "okay"). | Switch `interruption.mode` to `"adaptive"`. Raise `interruption.min_words` (requires STT) or `interruption.min_duration`. Confirm `false_interruption_timeout` and `resume_false_interruption` are at their defaults so the agent resumes after silent false positives. |
| Agent feels too slow to respond. | Confirm `preemptive_generation` is enabled (it is by default). Consider `preemptive_tts: true` to start TTS early. Lower `endpointing.min_delay`. In Python, switch `endpointing.mode` to `"dynamic"` to adapt to actual pause patterns. |
| Agent reads a partial transcript and replies based on incomplete input. | The preemptive response should be canceled when the final transcript changes. Confirm by checking that you aren't returning early from `on_user_turn_completed`. Lower `preemptive_generation.max_speech_duration` so long utterances skip preemptive responses entirely. Lower `max_retries` to avoid repeated retries on jittery transcripts. |
| Audio quality is fine but turn detection still misfires in noisy rooms. | Add [voice isolation](https://docs.livekit.io/transport/media/noise-cancellation.md#agents-voice-isolation) for single-speaker scenarios or [background noise suppression](https://docs.livekit.io/transport/media/noise-cancellation.md#agents-background-noise-suppression) for multi-speaker. Both run before VAD and STT, so they improve every downstream turn-taking signal. |
| Agent runs back-to-back utterances together with no breath (for example, a `say()` followed by a tool-driven `generate_reply()`). | Set `min_consecutive_speech_delay` to a small value like `0.2`–`0.4` seconds (Python only). |

If you're tuning by feel, use [agent observability](https://docs.livekit.io/deploy/observability/insights.md) to confirm changes actually move the metrics you care about. Preemptive generation in particular doesn't always reduce latency, and the metrics tell you whether your changes are pulling their weight.

## Additional resources

- **[Preemptive generation](https://docs.livekit.io/agents/multimodality/audio.md#preemptive-generation)**: Start LLM generation before the user's end of turn is confirmed.

- **[Noise & echo cancellation](https://docs.livekit.io/transport/media/noise-cancellation.md)**: Background voice cancellation and noise suppression for cleaner input audio.

- **[Turn handling options](https://docs.livekit.io/reference/agents/turn-handling-options.md)**: Full reference for every turn-handling parameter.

---

This document was rendered at 2026-08-28T04:22:13.113Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/turns/tuning.md](https://docs.livekit.io/agents/logic/turns/tuning.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-31"></a>
## Page 31: agents/prebuilt/tasks/get-name/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-name/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-name.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › GetNameTask

---

# GetNameTask

> Collect and validate a user's name from noisy voice transcription or text input.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

Use `GetNameTask` to collect a user's name with configurable parts. The task handles first, middle, and last names independently, with built-in support for noisy voice transcription.

`GetNameTask` handles the following:

- Configurable collection of first, middle, and last name parts.
- Normalization of spoken name patterns, including letter-by-letter spelling and phonetic alphabet input.
- Conversion of words like "dash" and "apostrophe" into symbols (`-`, `'`).
- Optional spelling verification where the agent spells back each name part letter by letter.
- Culturally diverse name patterns and special characters.

The task returns a `GetNameResult` data class with three optional fields: `first_name`, `middle_name`, and `last_name`. Only the fields you configure for collection are populated.

### Basic usage

For a basic example, see the following code snippet:

```python
from livekit.agents.beta.workflows import GetNameTask

# ... within your agent ...
name_result = await GetNameTask(
    first_name=True,
    last_name=True,
    chat_ctx=self.chat_ctx,
)
print(f"Collected name: {name_result.first_name} {name_result.last_name}")

```

### Usage with spelling verification

Enable spelling verification to have the agent spell back the name letter by letter before confirming:

```python
from livekit.agents.beta.workflows import GetNameTask
from livekit.agents import function_tool, RunContext

@function_tool()
async def collect_patient_name(context: RunContext) -> str:
    """Collect the patient's full name with spelling verification"""
    name_result = await GetNameTask(
        first_name=True,
        last_name=True,
        verify_spelling=True,
        chat_ctx=context.session.chat_ctx,
        extra_instructions="This is for a medical record, so accuracy is critical.",
    )
    return f"Patient name recorded: {name_result.first_name} {name_result.last_name}"

```

### Parameters

For a full list of parameters, see the [GetNameTask reference](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/index.html.md#livekit.agents.beta.workflows.GetNameTask).

- **`first_name`** _(bool)_ (optional) - Default: `True`: Whether to collect the user's first name.

- **`last_name`** _(bool)_ (optional) - Default: `False`: Whether to collect the user's last name.

- **`middle_name`** _(bool)_ (optional) - Default: `False`: Whether to collect the user's middle name.

- **`name_format`** _(string)_ (optional): Custom format string for the name parts. Uses `{first_name}`, `{middle_name}`, and `{last_name}` placeholders. Defaults to the enabled parts joined by spaces.

- **`verify_spelling`** _(bool)_ (optional) - Default: `False`: Whether to verify the spelling of the name by reading it back letter by letter.

- **`extra_instructions`** _(string)_ (optional) - Default: `""`: Additional instructions to append to the task's default instructions.

- **`chat_ctx`** _(ChatContext)_ (optional): The conversation history the task-specific LLM sees. If you omit it, the task runs with an empty context, with no memory of what was said earlier in the session. Pass the primary agent's chat context so the task can refer to prior turns and, when used inside a task group, so exchanges are summarized back into the main context.

- **`require_confirmation`** _(bool)_ (optional): Whether to read the name back to the user to confirm it before finalizing the task. For audio sessions this defaults to `True`, for text it defaults to `False`.

- **`tools`** _(list)_ (optional): Additional tools available to the task. Use this to add or substitute function tools.

---

This document was rendered at 2026-08-28T04:22:13.118Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks/get-name.md](https://docs.livekit.io/agents/prebuilt/tasks/get-name.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-32"></a>
## Page 32: agents/prebuilt/tasks/get-email/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-email/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-email.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › GetEmailTask

---

# GetEmailTask

> Collect and validate an email address from the user with noisy voice transcription handling.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

Use `GetEmailTask` to reliably collect and validate an email address from the user.

`GetEmailTask` handles the following:

- Normalization of noisy voice transcription and spoken email patterns.
- Conversion of words like "dot," "underscore," "dash," "plus" into symbols (`.`, `_`, `-`, `+`).
- Recognition of patterns where users spell out words (for example, "john j o h n").

The task returns a `GetEmailResult` data class with one field: `email_address`.

### Basic usage

For a basic example, see the following code snippet:

```python
from livekit.agents.beta.workflows import GetEmailTask

# ... within your agent ...
email_result = await GetEmailTask(chat_ctx=self.chat_ctx)
print(f"Collected email: {email_result.email_address}")

```

### Custom implementation

By default `GetEmailTask` calls its `decline_email_capture()` tool when the user doesn't provide an email address. The following example customizes the task to instead collect alternative contact information:

```python
from livekit.agents.beta.workflows import GetEmailTask
from livekit.agents import function_tool, RunContext
    
@function_tool()
async def get_alternate_contact_info(context: RunContext, contact_method: str, contact_value: str) -> None:
    """Collect alternative contact information when email isn't available"""
    # Store the alternative contact info
    context.session.userdata.alternate_contact_method = contact_method
    context.session.userdata.alternate_contact_value = contact_value
    
    await context.session.generate_reply(
        instructions=f"Acknowledge that you've recorded their {contact_method}: {contact_value}. Let them know this will be used for communication instead of email."
    )

# Customize GetEmailTask with extra instructions and tools
# ... within your agent ...
@function_tool()
async def collect_contact_info(context: RunContext) -> str:

    """Collect email or alternative contact information"""
    email_result = await GetEmailTask(
        chat_ctx=context.session.chat_ctx,
        extra_instructions="If the user cannot provide an email, call get_alternate_contact_info() instead of decline_email_capture().",
        tools=[get_alternate_contact_info]
    )

    return f"Collected email: {email_result.email_address}"

```

### Parameters

For a full list of parameters, see the [GetEmailTask reference](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/index.html.md#livekit.agents.beta.workflows.GetEmailTask).

- **`instructions`** _(string)_ (optional): Instructions for the task, replacing the default instructions. Use this to customize behavior for specific use cases.

- **`extra_instructions`** _(string)_ (optional): Deprecated. Use `instructions` instead. Additional instructions to append to the task's default instructions. Ignored if `instructions` is also provided.

- **`chat_ctx`** _(ChatContext)_ (optional): The conversation history the task-specific LLM sees. If you omit it, the task runs with an empty context, with no memory of what was said earlier in the session. Pass the primary agent's chat context so the task can refer to prior turns and, when used inside a task group, so exchanges are summarized back into the main context.

- **`require_confirmation`** _(bool)_ (optional): Whether to read the email address back to the user to confirm it before finalizing the task. For audio sessions this defaults to `True`, for text it defaults to `False`.

- **`tools`** _(list)_ (optional): Additional tools available to the task. Use this to add or substitute function tools.

---

This document was rendered at 2026-08-28T04:22:13.118Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks/get-email.md](https://docs.livekit.io/agents/prebuilt/tasks/get-email.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-33"></a>
## Page 33: agents/prebuilt/tasks/get-address/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-address/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-address.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › GetAddressTask

---

# GetAddressTask

> Collect and validate a complete mailing address from the user with international format support.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

Use `GetAddressTask` to collect and validate a complete mailing address from the user. The task supports international addresses and automatically normalizes spoken address formats.

`GetAddressTask` handles the following:

- Accepts addresses from any country and normalizes different address formats.
- Converts words like "dash" and "apostrophe" into symbols (`-`, `'`), and spelled-out numbers into numerals.
- Processes postal codes digit-by-digit.
- Prompts for address components in order: street address, unit number (if applicable), locality, and country.

The task returns a `GetAddressResult` data class with one field: `address`.

### Usage

The following example uses `GetAddressTask` to collect a user's mailing address:

```python
from livekit.agents.beta.workflows import GetAddressTask
from livekit.agents import Agent, function_tool, RunContext
    
@function_tool()
async def collect_shipping_address(context: RunContext) -> str:
    """Collect the user's shipping address"""
    address_result = await GetAddressTask(
        chat_ctx=context.session.chat_ctx,
        extra_instructions="Emphasize that this is for shipping purposes and accuracy is important."
    )
    
    return f"Shipping address recorded: {address_result.address}"

```

### Parameters

For a full list of parameters, see the [GetAddressTask reference](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/index.html.md#livekit.agents.beta.workflows.GetAddressTask).

- **`extra_instructions`** _(string)_ (optional): Additional instructions to append to the task's default instructions.

- **`chat_ctx`** _(ChatContext)_ (optional): The conversation history the task-specific LLM sees. If you omit it, the task runs with an empty context, with no memory of what was said earlier in the session. Pass the primary agent's chat context so the task can refer to prior turns and, when used inside a task group, so exchanges are summarized back into the main context.

- **`require_confirmation`** _(bool)_ (optional): Whether to read the address back to the user to confirm it before finalizing the task. For audio sessions this defaults to `True`, for text it defaults to `False`.

- **`tools`** _(list)_ (optional): Additional tools available to the task. Use this to add or substitute function tools.

---

This document was rendered at 2026-08-28T04:22:13.141Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks/get-address.md](https://docs.livekit.io/agents/prebuilt/tasks/get-address.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-34"></a>
## Page 34: agents/prebuilt/tasks/get-dob/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-dob/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-dob.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › GetDOBTask

---

# GetDOBTask

> Collect and validate a date of birth from the user with spoken date handling.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

Use `GetDOBTask` to collect a user's date of birth with support for various spoken and written date formats. The task validates the date and optionally collects a time of birth.

`GetDOBTask` handles the following:

- Normalization of spoken dates in formats like "January fifteenth, nineteen ninety" or "01 15 1990."
- Conversion of spoken ordinals and numbers to their numeric form.
- Handling of two-digit years (for example, "90" becomes 1990).
- Validation that the date is not in the future.
- Optional collection of time of birth.

The task returns a `GetDOBResult` data class with two fields: `date_of_birth` (`datetime.date`) and `time_of_birth` (`datetime.time | None`).

### Basic usage

For a basic example, see the following code snippet:

```python
from livekit.agents.beta.workflows import GetDOBTask

# ... within your agent ...
dob_result = await GetDOBTask(chat_ctx=self.chat_ctx)
print(f"Date of birth: {dob_result.date_of_birth}")

```

### Usage with time of birth

Enable time collection for use cases like birth records or astrology applications:

```python
from livekit.agents.beta.workflows import GetDOBTask
from livekit.agents import function_tool, RunContext

@function_tool()
async def collect_birth_info(context: RunContext) -> str:
    """Collect the user's date and time of birth"""
    dob_result = await GetDOBTask(
        include_time=True,
        chat_ctx=context.session.chat_ctx,
    )
    result = f"Date of birth: {dob_result.date_of_birth}"
    if dob_result.time_of_birth:
        result += f", Time: {dob_result.time_of_birth}"
    return result

```

### Parameters

For a full list of parameters, see the [GetDOBTask reference](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/index.html.md#livekit.agents.beta.workflows.GetDOBTask).

- **`include_time`** _(bool)_ (optional) - Default: `False`: Whether to also ask for and collect the user's time of birth. The time is optional for the user even when enabled.

- **`extra_instructions`** _(string)_ (optional) - Default: `""`: Additional instructions to append to the task's default instructions.

- **`chat_ctx`** _(ChatContext)_ (optional): The conversation history the task-specific LLM sees. If you omit it, the task runs with an empty context, with no memory of what was said earlier in the session. Pass the primary agent's chat context so the task can refer to prior turns and, when used inside a task group, so exchanges are summarized back into the main context.

- **`require_confirmation`** _(bool)_ (optional): Whether to read the date back to the user to confirm it before finalizing the task. For audio sessions this defaults to `True`, for text it defaults to `False`.

- **`tools`** _(list)_ (optional): Additional tools available to the task. Use this to add or substitute function tools.

---

This document was rendered at 2026-08-28T04:22:13.153Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks/get-dob.md](https://docs.livekit.io/agents/prebuilt/tasks/get-dob.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-35"></a>
## Page 35: agents/prebuilt/tasks/get-phone-number/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-phone-number/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-phone-number.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › GetPhoneNumberTask

---

# GetPhoneNumberTask

> Collect and validate a phone number from the user with spoken digit handling.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

Use `GetPhoneNumberTask` to collect a phone number from the user. The task normalizes spoken digit patterns and validates the result against international phone number formats.

`GetPhoneNumberTask` handles the following:

- Conversion of spoken digits to their numeric form (for example, "five five five" becomes "555").
- Recognition of "plus" as the international prefix `+` and "area code" as a verbal cue.
- Stripping of dashes, spaces, parentheses, and dots.
- Validation against international phone number formats (7 to 15 digits, with optional leading `+`).
- Reading the number back in groups rather than as a single block.

The task returns a `GetPhoneNumberResult` data class with one field: `phone_number`.

### Usage

The following example uses `GetPhoneNumberTask` to collect a callback number:

```python
from livekit.agents.beta.workflows import GetPhoneNumberTask
from livekit.agents import function_tool, RunContext

@function_tool()
async def collect_callback_number(context: RunContext) -> str:
    """Collect a callback phone number from the user"""
    phone_result = await GetPhoneNumberTask(
        chat_ctx=context.session.chat_ctx,
        extra_instructions="Ask for a number where we can reach them during business hours.",
    )
    return f"Callback number recorded: {phone_result.phone_number}"

```

### Parameters

For a full list of parameters, see the [GetPhoneNumberTask reference](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/index.html.md#livekit.agents.beta.workflows.GetPhoneNumberTask).

- **`extra_instructions`** _(string)_ (optional) - Default: `""`: Additional instructions to append to the task's default instructions.

- **`chat_ctx`** _(ChatContext)_ (optional): The conversation history the task-specific LLM sees. If you omit it, the task runs with an empty context, with no memory of what was said earlier in the session. Pass the primary agent's chat context so the task can refer to prior turns and, when used inside a task group, so exchanges are summarized back into the main context.

- **`require_confirmation`** _(bool)_ (optional): Whether to read the phone number back to the user to confirm it before finalizing the task. For audio sessions this defaults to `True`, for text it defaults to `False`.

- **`tools`** _(list)_ (optional): Additional tools available to the task. Use this to add or substitute function tools.

---

This document was rendered at 2026-08-28T04:22:13.148Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks/get-phone-number.md](https://docs.livekit.io/agents/prebuilt/tasks/get-phone-number.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-36"></a>
## Page 36: agents/prebuilt/tasks/get-credit-card/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-credit-card/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-credit-card.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › GetCreditCardTask

---

# GetCreditCardTask

> Collect and validate complete credit card information including card number, security code, and expiration date.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

Use `GetCreditCardTask` to collect complete credit card information from the user. This is a composite task that runs a `TaskGroup` internally to collect the cardholder name, card number, security code, and expiration date in sequence.

`GetCreditCardTask` handles the following:

- Sequential collection of cardholder name, card number, security code, and expiration date using a task group.
- Card number format validation.
- Card issuer detection (Visa, Mastercard, American Express, Discover).
- Expiration date validation to reject expired cards.
- Built-in restart flow if the user wants to provide a different card.
- Sensitive information is never repeated back to the user during audio sessions.

The task returns a `GetCreditCardResult` data class with five fields: `cardholder_name`, `issuer`, `card_number`, `security_code`, and `expiration_date`.

### Usage

The following example uses `GetCreditCardTask` to collect payment information:

```python
from livekit.agents.beta.workflows import GetCreditCardTask
from livekit.agents import function_tool, RunContext

@function_tool()
async def collect_payment(context: RunContext) -> str:
    """Collect payment card information from the user"""
    card_result = await GetCreditCardTask(
        chat_ctx=context.session.chat_ctx,
    )
    last_four = card_result.card_number[-4:]
    return f"Payment recorded: {card_result.issuer} ending in {last_four}"

```

### Sub-tasks

`GetCreditCardTask` internally runs a `TaskGroup` with the following sub-tasks in order:

1. **`GetNameTask`**: Collects the cardholder's full name (first and last).
2. **`GetCardNumberTask`**: Collects and validates the card number format.
3. **`GetSecurityCodeTask`**: Collects the 3 or 4 digit security code (CVV/CVC).
4. **`GetExpirationDateTask`**: Collects and validates the expiration date.

Each sub-task includes a `restart_card_collection` tool that allows the user to start over from the beginning if needed.

### Parameters

For a full list of parameters, see the [GetCreditCardTask reference](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/index.html.md#livekit.agents.beta.workflows.GetCreditCardTask).

- **`chat_ctx`** _(ChatContext)_ (optional): The conversation history the task-specific LLM sees. If you omit it, the task runs with an empty context, with no memory of what was said earlier in the session. Pass the primary agent's chat context so the task can refer to prior turns and, when used inside a task group, so exchanges are summarized back into the main context.

- **`require_confirmation`** _(bool)_ (optional): Whether to confirm each piece of card information with the user before finalizing. For audio sessions this defaults to `True`, for text it defaults to `False`. This setting propagates to all sub-tasks.

- **`tools`** _(list)_ (optional): Additional tools available to the task. Use this to add or substitute function tools.

---

This document was rendered at 2026-08-28T04:22:13.163Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks/get-credit-card.md](https://docs.livekit.io/agents/prebuilt/tasks/get-credit-card.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-37"></a>
## Page 37: agents/prebuilt/tasks/get-dtmf/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-dtmf/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks/get-dtmf.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › GetDtmfTask

---

# GetDtmfTask

> Collect keypad (DTMF) or spoken digits from callers for IVR and telephony flows.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

`GetDtmfTask` collects a series of keypad (DTMF) or spoken digits from callers in telephony flows. For example, use this to implement IVR systems that can be navigated by either pressing or speaking numbers.

`GetDtmfTask` handles the following:

- Listening for DTMF tones from the phone keypad.
- Accepting spoken digits as an alternative to DTMF input.
- Waiting for the specified number of digits with a configurable timeout.
- Interrupting the agent when DTMF input is received.

The task returns a `GetDtmfResult` data class with one field: `user_input` (a string of the collected digits).

- **[DTMF example](https://github.com/livekit/agents/blob/main/examples/telephony/basic_dtmf_agent.py)**: A menu-based example that demonstrates using DTMF to collect user input.

- **[Handling DTMF](https://docs.livekit.io/telephony/features/dtmf.md)**: Sending and receiving DTMF in LiveKit telephony apps.

- **[Send DTMF events](https://docs.livekit.io/agents/prebuilt/tools/send-dtmf-events.md)**: Prebuilt tool for sending DTMF tones from your agent to telephony providers.

### Usage

The following example asks the caller to provide a 10-digit phone number and confirms the number with the caller:

```python
from livekit.agents.beta.workflows.dtmf_inputs import GetDtmfTask
from livekit.agents import Agent, function_tool, RunContext

class PhoneAgent(Agent):
    @function_tool()
    async def ask_for_phone_number(self, context: RunContext) -> str:
        """Ask user to provide a phone number."""
        result = await GetDtmfTask(
            num_digits=10,
            chat_ctx=context.session.chat_ctx.copy(
                exclude_instructions=True, 
                exclude_function_call=True
            ),
            ask_for_confirmation=True,
            extra_instructions=(
                "Let the caller know you'll record their 10-digit phone number "
                "and that they can speak or dial it, then capture the digits."
            ),
        )
        
        return f"User's phone number is {result.user_input}"

```

### Parameters

For a full list of parameters, see the [GetDtmfTask reference](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/dtmf_inputs.html.md#livekit.agents.beta.workflows.dtmf_inputs.GetDtmfTask).

- **`extra_instructions`** _(string)_ (optional): Extra instructions to add to the task.

- **`chat_ctx`** _(ChatContext)_: The chat context to use for the task.

- **`num_digits`** _(int)_: Number of digits to collect. Must be greater than 0.

- **`ask_for_confirmation`** _(bool)_ (optional) - Default: `False`: Whether to ask the user to confirm the collected digits before finalizing (for example, by reading them back). When `True`, the task uses a confirmation flow.

- **`dtmf_input_timeout`** _(float)_ (optional) - Default: `4.0`: Per-digit timeout in seconds while waiting for DTMF or spoken input.

- **`dtmf_stop_event`** _(DtmfEvent)_ (optional) - Default: `DtmfEvent.POUND`: The DTMF event to stop collecting inputs (default `#`).

---

This document was rendered at 2026-08-28T04:22:13.177Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks/get-dtmf.md](https://docs.livekit.io/agents/prebuilt/tasks/get-dtmf.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-38"></a>
## Page 38: agents/prebuilt/tasks/warm-transfer/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tasks/warm-transfer/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tasks/warm-transfer.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tasks › WarmTransferTask

---

# WarmTransferTask

> Execute an agent-assisted warm transfer with SIP dialing, hold music, and context handoff.

Available in:
- [x] Node.js
- [x] Python

## Overview

Use `WarmTransferTask` to execute an agent-assisted warm transfer. The task automatically manages the complexities of the transfer workflow, including dialing the human agent, providing context, and merging the calls.

`WarmTransferTask` handles the following:

- Creating a separate room for the human agent.
- Dialing the human agent using SIP.
- Playing hold music to the caller while connecting.
- Providing the human agent with conversation history and context.
- Disabling I/O for the caller during the transfer process.
- Providing tools for the human agent to:- `connect_to_caller`: Connect the human agent to the original caller.
- `decline_transfer`: Decline the transfer with a reason.
- `voicemail_detected`: Handle voicemail detection.

The task returns a `WarmTransferResult` data class with one field: `human_agent_identity` (`humanAgentIdentity` in Node.js).

- **[Agent-assisted warm transfer](https://docs.livekit.io/telephony/features/transfers/warm.md)**: A comprehensive guide to transferring calls using an AI agent to provide context.

### Usage

For a basic example, see the following code snippet:

**Python**:

```python
import os

from livekit.agents.beta.workflows import WarmTransferTask
from livekit.protocol.sip import SIPOutboundConfig

result = await WarmTransferTask(
    sip_call_to=<human-agent-phone-number>,         # Human agent's phone number
    sip_connection=SIPOutboundConfig(               # Inline trunk configuration
        hostname=os.getenv("SIP_TRUNK_HOSTNAME"),
        auth_username=os.getenv("SIP_AUTH_USERNAME"),
        auth_password=os.getenv("SIP_AUTH_PASSWORD"),
    ),
    chat_ctx=self.chat_ctx,                         # Conversation history
)

```

---

**Node.js**:

```typescript
import { workflows } from '@livekit/agents';

const result = await new workflows.WarmTransferTask({
  sipCallTo: '<human-agent-phone-number>', // Human agent's phone number
  sipTrunkId: process.env.LIVEKIT_SIP_OUTBOUND_TRUNK, // Stored outbound trunk ID
  chatCtx: this.chatCtx, // Conversation history
  instructions: { extra: '<summary-instructions>' },
}).run();

```

> ℹ️ **Stored outbound trunk**
> 
> You can also use a stored outbound trunk by passing `sip_trunk_id` instead of `sip_connection`. For details, see [Outbound trunk](https://docs.livekit.io/telephony/making-calls/outbound-trunk.md). You can set the trunk ID with the `LIVEKIT_SIP_OUTBOUND_TRUNK` environment variable.

> ℹ️ **Node.js namespace**
> 
> In Node.js (v1.5+), `WarmTransferTask` is part of the stable `workflows` namespace — import it as `workflows.WarmTransferTask` and use camelCase options. In Python, it remains under `beta.workflows`.

### Parameters

For a full list of parameters, see the [WarmTransferTask reference](https://docs.livekit.io/reference/python/livekit/agents/beta/workflows/warm_transfer.html.md#livekit.agents.beta.workflows.warm_transfer.WarmTransferTask).

You can customize the behavior of `WarmTransferTask` by passing additional parameters:

- **`sip_call_to`** _(string)_: The phone number or SIP URI to dial for the warm transfer.

- **`sip_trunk_id`** _(string)_ (optional) - Environment: `LIVEKIT_SIP_OUTBOUND_TRUNK`: The outbound SIP trunk ID to use for dialing. Either `sip_trunk_id` or `sip_connection` is required. You can also set this with the `LIVEKIT_SIP_OUTBOUND_TRUNK` environment variable.

- **`sip_connection`** _(api.SIPOutboundConfig)_ (optional): [Inline trunk configuration](https://docs.livekit.io/telephony/making-calls/outbound-calls.md#inline-trunk). Pass trunk settings directly instead of using a stored trunk. You can specify a custom hostname, transport protocol, or authentication credentials.

Either `sip_connection` or `sip_trunk_id` is required.

- **`sip_number`** _(string)_ (optional) - Environment: `LIVEKIT_SIP_NUMBER`: The SIP "From" number to use as the caller ID. If empty, the trunk number is used. You can also set this with the `LIVEKIT_SIP_NUMBER` environment variable.

- **`sip_headers`** _(dict[str, str])_ (optional): Custom SIP headers included as-is in the outbound INVITE request. Use this to pass metadata that identifies the call to the remote SIP endpoint.

- **`dtmf`** _(str | None)_ (optional): DTMF tones to send after the human agent answers the call. Use this to dial an extension or navigate an interactive voice response (IVR) menu. Insert `w` characters to pause ~0.5 seconds each before or between digits. For example, `"wwww1234#"` waits ~2 seconds then dials extension 1234.

- **`ringing_timeout`** _(float | None)_ (optional): Seconds to wait for the human agent to answer before giving up. When the timeout elapses, the task completes with a `ToolError` and the caller conversation resumes.

- **`hold_audio`** _(AudioSource | AudioConfig | list | None)_ (optional) - Default: `BuiltinAudioClip.HOLD_MUSIC`: Audio to play while the caller is on hold. By default, plays `BuiltinAudioClip.HOLD_MUSIC`.

**Audio comparison** (audio-only, not available in text):

- [Default hold music](https://github.com/livekit/agents/blob/main/livekit-agents/livekit/agents/resources/hold_music.ogg)

- **`extra_instructions`** _(string)_ (optional): Additional instructions for the transfer agent. These instructions are passed to the transfer agent along with the conversation history and the default instructions.

- **`callerHangupInstruction`** _(string)_ (optional): Available in:
- [x] Node.js
- [ ] Python

Instructions used to generate the message the human agent hears if the caller hangs up mid-transfer. Their call ends after the message plays. By default, the message conveys that the caller has left and the call is ending.

- **`tools`** _(list)_ (optional): Additional tools that can be used in the execution of the transfer task. These tools can be used in place of, or in addition to, the default tools.

---

This document was rendered at 2026-08-28T04:22:13.174Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tasks/warm-transfer.md](https://docs.livekit.io/agents/prebuilt/tasks/warm-transfer.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-39"></a>
## Page 39: agents/prebuilt/tools/end-call-tool/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tools/end-call-tool/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tools/end-call-tool.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tools › EndCallTool

---

# EndCallTool

> Provide your agent with a tool that gracefully ends the call and disconnects from the room.

Available in (BETA):
- [x] Node.js
- [x] Python

## Overview

Use `EndCallTool` to provide your agent with a tool that gracefully ends the call and disconnects from the room. The tool automatically handles cleanup, including optionally deleting the room and shutting down the session.

When the `end_call` tool is called:

1. The agent generates a final response (based on `end_instructions`).
2. The session shuts down after the response is complete.
3. If `delete_room` is `True`, the room is deleted, disconnecting all participants.
4. The job process shuts down.

### Basic usage

Add `EndCallTool` (Python) or `beta.createEndCallTool()` (Node.js) to your agent's tools:

**Python**:

```python
from livekit.agents.beta.tools import EndCallTool
from livekit.agents import Agent

class CustomerServiceAgent(Agent):
    def __init__(self):
        end_call_tool = EndCallTool()
        super().__init__(
            instructions="You are a helpful customer service agent.",
            tools=end_call_tool.tools,
        )

```

---

**Node.js**:

```typescript
import { beta, voice } from '@livekit/agents';

const customerServiceAgent = voice.Agent.create({
  instructions: 'You are a helpful customer service agent.',
  tools: [beta.createEndCallTool()],
});

```

The LLM automatically has access to the `end_call` tool and can use it when the conversation is complete.

### Custom implementation

By default, `EndCallTool` uses generic instructions for when and how to end the call. The following example customizes the tool with `extra_description` and `end_instructions` so the agent only ends the call after confirming the customer's issue is resolved and says a custom goodbye message.

**Python**:

```python
from livekit.agents.beta.tools import EndCallTool
from livekit.agents import Agent

class SupportAgent(Agent):
    def __init__(self):
        end_call_tool = EndCallTool(
            extra_description="Only end the call after confirming the customer's issue is resolved.",
            delete_room=True,
            end_instructions="Thank the customer for their time and wish them a good day.",
        )
        super().__init__(
            instructions="You are a technical support agent. Help resolve customer issues.",
            tools=end_call_tool.tools,
        )

```

---

**Node.js**:

```typescript
import { beta, voice } from '@livekit/agents';

const supportAgent = voice.Agent.create({
  instructions: 'You are a technical support agent. Help resolve customer issues.',
  tools: [
    beta.createEndCallTool({
      extraDescription: "Only end the call after confirming the customer's issue is resolved.",
      deleteRoom: true,
      endInstructions: 'Thank the customer for their time and wish them a good day.',
    }),
  ],
});

```

### Parameters

For a full list of Python parameters, see the [EndCallTool reference](https://docs.livekit.io/reference/python/livekit/agents/beta/tools/index.html.md#livekit.agents.beta.tools.EndCallTool). In Node.js, pass camelCase options to `beta.createEndCallTool(...)`.

- **`extra_description`** _(string)_ (optional): Additional description to add to the end call tool description. Useful for providing context-specific instructions.

- **`delete_room`** _(bool)_ (optional) - Default: `True`: Whether to delete the room when the call ends. Deleting the room disconnects all remote users, including SIP callers.

- **`end_instructions`** _(string)_ (optional) - Default: `say goodbye to the user`: Tool output to the LLM for generating the tool response. This is the message the LLM receives after the tool is called.

- **`on_tool_called / onToolCalled`** _(Callable)_ (optional): Callback invoked when the end-call tool is called.

- **`on_tool_completed / onToolCompleted`** _(Callable)_ (optional): Callback invoked after the end-call tool completes.

---

This document was rendered at 2026-08-28T04:22:13.164Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tools/end-call-tool.md](https://docs.livekit.io/agents/prebuilt/tools/end-call-tool.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-40"></a>
## Page 40: agents/prebuilt/tools/send-dtmf-events/
**Original URL:** https://docs.livekit.io/agents/prebuilt/tools/send-dtmf-events/  
**Source MD URL:** https://docs.livekit.io/agents/prebuilt/tools/send-dtmf-events.md

LiveKit docs › Build Agents › Prebuilt components › Prebuilt tools › send_dtmf_events

---

# send_dtmf_events

> Send DTMF tones to telephony providers for IVR navigation and phone systems.

Available in (BETA):
- [ ] Node.js
- [x] Python

## Overview

Use `send_dtmf_events` to send DTMF (dual-tone multi-frequency) tones to telephony providers. This is essential for navigating phone systems, IVR menus, and automated phone services.

The `send_dtmf_events` tool:

- Sends DTMF events sequentially with a 0.3-second delay between each event (defined by `DEFAULT_DTMF_PUBLISH_DELAY`).
- Returns a success message listing all sent events if all events are sent successfully.
- Returns an error message if any event fails to send (stops sending remaining events on first failure).

- **[Handling DTMF](https://docs.livekit.io/telephony/features/dtmf.md)**: Sending and receiving DTMF in LiveKit telephony apps.

- **[GetDtmfTask](https://docs.livekit.io/agents/prebuilt/tasks/get-dtmf.md)**: Prebuilt task for collecting DTMF input from users.

- **[Bank IVR example](https://github.com/livekit/agents/tree/main/examples/telephony/bank-ivr)**: Full agent that navigates a bank IVR using `send_dtmf_events` (via `ivr_detection=True`).

### Usage

Add `send_dtmf_events` as a tool to your agent:

```python
from livekit.agents.beta.tools import send_dtmf_events
from livekit.agents import Agent, function_tool

class IVRAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are an IVR navigation assistant. Help users navigate phone systems.",
            tools=[send_dtmf_events],
        )

```

### Parameters

For a full list of parameters, see the [send_dtmf_events reference](https://docs.livekit.io/reference/python/livekit/agents/beta/tools/send_dtmf.html.md).

- **`events`** _(list[DtmfEvent])_: List of DTMF events to send to the telephony provider. Available events include digits, special characters, and letters.

---

This document was rendered at 2026-08-28T04:22:13.174Z.
For the latest version of this document, see [https://docs.livekit.io/agents/prebuilt/tools/send-dtmf-events.md](https://docs.livekit.io/agents/prebuilt/tools/send-dtmf-events.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

