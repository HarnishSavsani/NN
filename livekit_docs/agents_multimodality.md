# Agents: Speech, Audio & Vision

Speech synthesis/recognition, background audio, wake word detection, live video sampling, and virtual avatars.

- **Total pages in this section**: 10
- **Successful retrieves**: 10
- **API References / Placeholders**: 0

## Table of Contents

1. [agents/multimodality/](#page-1) (✓)
2. [agents/multimodality/audio/](#page-2) (✓)
3. [agents/multimodality/text/](#page-3) (✓)
4. [agents/multimodality/instructions/](#page-4) (✓)
5. [agents/multimodality/vision/](#page-5) (✓)
6. [agents/multimodality/audio/customization/](#page-6) (✓)
7. [agents/multimodality/audio/background-audio/](#page-7) (✓)
8. [agents/multimodality/audio/wakeword/](#page-8) (✓)
9. [agents/multimodality/vision/images/](#page-9) (✓)
10. [agents/multimodality/vision/video/](#page-10) (✓)

---

<a name="page-1"></a>
## Page 1: agents/multimodality/
**Original URL:** https://docs.livekit.io/agents/multimodality/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality.md

LiveKit docs › Build Agents › Multimodality › Overview

---

# Multimodality overview

> Build agents that communicate through multiple channels for richer, more natural interactions.

## Overview

LiveKit Agents supports multimodality, enabling your agents to communicate through multiple channels simultaneously. Agents can process and generate speech, text, images, and live video, allowing them to understand context from different sources and respond in the most appropriate format. This flexibility enables richer, more natural interactions where agents can see what users show them, read transcriptions of conversations, send text messages, and speak — all within a single session.

## Modality options

Just as humans can see, hear, speak, and read, LiveKit agents can process and produce audio, text, images, and video. You can build agents that use a single modality or combine multiple modalities for richer, more flexible interactions.

| Modality | Description | Use cases |
| **Speech and audio** | Process realtime audio input from users' microphones, with support for speech-to-text, turn detection, and interruptions. Generate speech output with TTS. | Voice assistants, call center automation, and voice-controlled applications. |
| **Text and transcriptions** | Handle text messages and transcriptions, enabling text-only sessions or hybrid voice and text interactions. Send text responses and transcriptions. | Chatbots, text-based customer support, and accessibility features for users who prefer typing. |
| **Images and video** | Process images and live video feeds for visual understanding. Send images to the frontend with byte streams, or add a virtual avatar for lifelike video output. | Visual assistants, avatar-based agents, screen sharing analysis, and image-based question answering. |

## In this section

Read more about each modality.

- **[Speech and audio](https://docs.livekit.io/agents/multimodality/audio.md)**: Control agent speech, handle interruptions, and customize audio output.

- **[Text and transcriptions](https://docs.livekit.io/agents/multimodality/text.md)**: Handle text messages, transcriptions, and text-only sessions.

- **[Images and video](https://docs.livekit.io/agents/multimodality/vision.md)**: Process image and video input, send images, and add virtual avatars for video output.

---

This document was rendered at 2026-08-28T04:22:10.485Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality.md](https://docs.livekit.io/agents/multimodality.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-2"></a>
## Page 2: agents/multimodality/audio/
**Original URL:** https://docs.livekit.io/agents/multimodality/audio/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/audio.md

LiveKit docs › Build Agents › Multimodality › Speech & audio › Overview

---

# Agent speech and audio

> Speech and audio capabilities for LiveKit agents.

## Overview

Speech capabilities are a core feature of LiveKit agents, enabling them to interact with users through voice. This guide covers the various speech features and functionalities available for agents.

LiveKit Agents provide a unified interface for controlling agents using both the STT-LLM-TTS pipeline and realtime models.

## In this section

This page covers core speech control features like initiating speech, managing speech handles, and handling interruptions. The following  pages in this section cover additional topics:

| Topic | Description |
| [Audio customization](https://docs.livekit.io/agents/multimodality/audio/customization.md) | Cache TTS responses, customize pronunciation, and adjust speech volume. |
| [Background audio](https://docs.livekit.io/agents/multimodality/audio/background-audio.md) | Add ambient sounds, thinking sounds, and on-demand audio playback. |
| [Custom voices](https://docs.livekit.io/agents/models/tts/custom-voices.md) | Create voice clones from short audio samples for use with supported TTS providers. |
| [Wakeword detection](https://docs.livekit.io/agents/multimodality/audio/wakeword.md) | Detect a spoken trigger phrase on the client to activate the agent hands-free. |

To learn more and see usage examples, see the following topics:

- **[Text-to-speech (TTS)](https://docs.livekit.io/agents/models/tts.md)**: TTS is a synthesis process that converts text into audio, giving AI agents a "voice."

- **[Speech-to-speech](https://docs.livekit.io/agents/models/realtime.md)**: Multimodal, realtime APIs can understand speech input and generate speech output directly.

## Instant connect

The instant connect feature reduces perceived connection time by capturing microphone input before the agent connection is established. This pre-connect audio buffer sends speech as context to the agent, avoiding awkward gaps between a user's connection and their ability to interact with an agent.

Microphone capture begins locally while the agent is connecting. Once the connection is established, the speech and metadata is sent over a byte stream with the topic `lk.agent.pre-connect-audio-buffer`. If no agent connects before timeout, the buffer is discarded.

You can enable this feature using `withPreconnectAudio`:

**JavaScript**:

In the Javascript SDK, this functionality is exposed via `TrackPublishOptions`.

```typescript
await room.localParticipant.setMicrophoneEnabled(!enabled, undefined, {
  preConnectBuffer: true,
});

```

---

**Swift**:

```swift
try await room.withPreConnectAudio(timeout: 10) {
  try await room.connect(url: serverURL, token: token)
} onError: { err in
  print("Pre-connect audio send failed:", err)
}

```

---

**Android**:

```kotlin
try {
  room.withPreconnectAudio {
      // Audio is being captured automatically
      // Perform other async setup
      val (url, token) = tokenService.fetchConnectionDetails()
      room.connect(
          url = url,
          token = token,
      )
      room.localParticipant.setMicrophoneEnabled(true)
  }
} catch (e: Throwable) {
  Log.e(TAG, "Error!")
}

```

---

**Flutter**:

```dart
try {
  await room.withPreConnectAudio(() async {
    // Audio is being captured automatically, perform other async setup
    // Get connection details from token service etc.
    final connectionDetails = await tokenService.fetchConnectionDetails();
    await room.connect(
      connectionDetails.serverUrl,
      connectionDetails.participantToken,
    );
    // Mic already enabled
  });
} catch (error) {
  print("Error: $error");
}

```

## Automatic gain control

Available in:
- [ ] Node.js
- [x] Python

The Agents framework normalizes incoming audio levels using a built-in audio processing module. This is helpful when participants are at different distances from their microphones or have different gain settings. This feature is enabled by default.

To turn off, set `auto_gain_control=False` on `AudioInputOptions`:

```python
from livekit.agents import room_io

room_options = room_io.RoomOptions(
    audio_input=room_io.AudioInputOptions(
        auto_gain_control=False,
    ),
)

```

## Preemptive speech generation

**Preemptive generation** speculatively starts an LLM response before the user's end of turn is confirmed, reducing perceived latency in back-and-forth conversation. It's enabled by default. Only the LLM runs preemptively — TTS waits until the turn is confirmed. For the lowest possible latency, enable `preemptive_tts` to also run TTS speculatively, at the cost of higher wasted compute when the response is discarded.

If the chat context or tools change in the `on_user_turn_completed` [node](https://docs.livekit.io/agents/build/nodes.md#on_user_turn_completed), the speculative response is discarded and regenerated. This means preemptive generation increases LLM token usage, and the tradeoff is less favorable when users speak for extended periods (dictation, storytelling) since the speculative response is more likely to be discarded. Consider disabling it in those scenarios.

### Configuration

Configure preemptive generation using the `preemptive_generation` key in `turn_handling`. For a full list of options, see the [PreemptiveGenerationOptions](https://docs.livekit.io/reference/agents/turn-handling-options.md#preemptivegenerationoptions) reference.

**Python**:

```python
session = AgentSession(
    turn_handling={
        "preemptive_generation": {
            "preemptive_tts": True,       # also run TTS before turn confirmation
            "max_speech_duration": 10.0,  # skip if user speaks longer than 10s
            "max_retries": 3,             # max preemptive attempts per turn
        },
    },
    # ... STT, LLM, TTS, etc.
)

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
    // ... llm, stt, etc.
    turnHandling: {
      preemptiveGeneration: {
        preemptiveTts: true,       // also run TTS before turn confirmation
        maxSpeechDuration: 10_000, // skip if user speaks longer than 10s (ms)
        maxRetries: 3,             // max preemptive attempts per turn
      },
    },
});

```

To disable preemptive generation entirely:

**Python**:

```python
session = AgentSession(
    turn_handling={
        "preemptive_generation": {"enabled": False},
    },
    # ... STT, LLM, TTS, etc.
)

```

---

**Node.js**:

```typescript
const session = new voice.AgentSession({
    // ... llm, stt, etc.
    turnHandling: {
      preemptiveGeneration: { enabled: false },
    },
});

```

## Initiating speech

By default, the agent waits for user input before responding — the Agents framework automatically handles response generation.

In some cases, though, the agent might need to initiate the conversation. For example, it might greet the user at the start of a session or check in after a period of silence. For fixed phrases like these, you can [cache TTS and use pre-synthesized audio](https://docs.livekit.io/agents/multimodality/audio/customization.md#caching-tts) to avoid redundant TTS calls and reduce latency.

### session.say

To have the agent speak a predefined message, use `session.say()`. This triggers the configured TTS to synthesize speech and play it back to the user.

You can also optionally provide pre-synthesized audio for playback. This skips the TTS step and reduces response time.

> 💡 **Realtime models and TTS**
> 
> The `say` method requires a TTS plugin. If you're using a realtime model, you need to add a TTS plugin to your session or use the [`generate_reply()`](#manually-interrupt-and-generate-responses) method instead.

**Python**:

```python
await session.say(
   "Hello. How can I help you today?",
   allow_interruptions=False,
)

```

---

**Node.js**:

```typescript
await session.say(
  'Hello. How can I help you today?',
  {
    allowInterruptions: false,
  }
);

```

#### Parameters

You can call `session.say()` with the following options:

- `text` only: Synthesizes speech using TTS, which is added to the transcript and chat context (unless `add_to_chat_ctx=False`).
- `audio` only: Plays audio, which is not added to the transcript or chat context.
- `text` + `audio`: Plays the provided audio and the `text` is used for the transcript and chat context.

- **`text`** _(str | AsyncIterable[str])_ (optional): Text for TTS playback, added to the transcript and by default to the chat context.

- **`audio`** _(AsyncIterable[rtc.AudioFrame])_ (optional): Pre-synthesized audio to play. If used without `text`, nothing is added to the transcript or chat context.

- **`allow_interruptions`** _(boolean)_ (optional) - Default: `True`: If `True`, allow the user to interrupt the agent while speaking.

- **`add_to_chat_ctx`** _(boolean)_ (optional) - Default: `True`: If `True`, add the text to the agent's chat context after playback. Has no effect if `text` is not provided.

#### Returns

Returns a [`SpeechHandle`](#speechhandle) object.

#### Events

This method triggers a [`speech_created`](https://docs.livekit.io/reference/agents/events.md#speech_created) event.

### generate_reply

To make conversations more dynamic, use `session.generate_reply()` to prompt the LLM to generate a response.

There are two ways to use `generate_reply`:

1. give the agent instructions to generate a response

**Python**:

```python
session.generate_reply(
   instructions="greet the user and ask where they are from",
)

```

---

**Node.js**:

```typescript
 session.generateReply({
 instructions: 'greet the user and ask where they are from',
 });

```
2. provide the user's input via text

**Python**:

```python
session.generate_reply(
   user_input="how is the weather today?",
)

```

---

**Node.js**:

```typescript
 session.generateReply({
 userInput: 'how is the weather today?',
 });

```

#### How instructions interact with session-level instructions

The `instructions` parameter acts as extra instructions for that reply. The agent's session-level instructions (`Agent(instructions=...)`) remain active — `generate_reply` instructions don't replace them.

How the extra instructions are delivered to the model depends on the model type:

- **STT-LLM-TTS pipeline**: `instructions` are added as a separate system message at the end of the chat context, after the conversation history. For providers that don't natively support mid-conversation system messages (Anthropic, Google, AWS Bedrock), the framework automatically converts them to user messages wrapped in `<instructions>` tags.

For full control over the instructions used for a reply, [use a custom chat context](#custom-chat-context) (available in Python).
- **Realtime models**: the delivery method is provider-specific.

- OpenAI receives them as per-response instructions, scoped to that reply only. The framework prepends session-level instructions to preserve them.
- Gemini and Phonic receive them as a model message.
- Ultravox receives them as a user message wrapped in `<instructions>` tags.
For Gemini, Phonic, and Ultravox, `instructions` are added to the chat context and may influence future turns.

#### Using a custom chat context

For pipeline agents, you can use the `chat_ctx` parameter to `generate_reply` to fully control the context used for that reply, including replacing the agent's session-level instructions entirely rather than appending to them.

This is useful when the `instructions` parameter isn't enough. For example, if you need to switch contexts for a specific reply, exclude certain messages from the conversation history, or inject additional context before the LLM call. Pass a custom chat context and omit the `instructions` parameter.

The following example uses a modified copy of the agent's chat context:

**Python**:

```python
# Copy the current chat context to modify for this reply
ctx = session.current_agent.chat_ctx.copy()
# Modify context as needed: replace instructions, trim history, inject context, etc.
# Then pass the modified context to generate_reply without instructions
await session.generate_reply(chat_ctx=ctx)

```

---

**Node.js**:

```ts
// Copy the current chat context to modify for this reply
const ctx = session.currentAgent.chatCtx.copy();
// Modify context as needed: replace instructions, trim history, inject context, etc.
// Then pass the modified context to generateReply without instructions
await session.generateReply({ chatCtx: ctx });

```

For more details on working with `ChatContext`, see [Chat context](https://docs.livekit.io/agents/logic/chat-context.md).

#### Per-response tools and tool choice

Use `tools` and `tool_choice` to control which tools the agent can call for a single reply, without permanently changing what's registered on the agent. This is useful for staged workflows like surfacing a payment tool only during checkout or restricting destructive actions until identity is verified.

The `tools` parameter (Python only) takes a list of tool IDs that map to the agent's registered function tools and toolsets. For a function tool, the ID is the function name. For a toolset, it's the ID set at construction.

Both parameters apply only to the current reply, but the underlying behavior depends on the model:

- **OpenAI Realtime** and **STT-LLM-TTS pipelines**: `tools` and `tool_choice` are passed directly to the single LLM call for this reply.
- **Other realtime models** (Google, AWS Nova Sonic, Phonic, Ultravox, SpaceXAI): the framework swaps the realtime session's tools and tool choice for this reply, then restores the originals when it completes.

#### Parameters

The `generate_reply()` method accepts the following parameters. For a full list of parameters, see the [Python reference](https://docs.livekit.io/reference/python/livekit/agents.md#livekit.agents.AgentSession.generate_reply) and [Node.js reference](https://docs.livekit.io/reference/agents-js/classes/agents.voice.AgentSession.html.md#generateReply).

- **`user_input`** _(string)_ (optional): The user input to respond to.

- **`instructions`** _(string)_ (optional): Instructions for the agent to use for the reply.

- **`tool_choice`** _(ToolChoice)_ (optional): Controls how the LLM selects a tool for this reply: `"auto"`, `"required"`, `"none"`, or a named function `{ type: "function", function: { name: "..." } }`. If `generate_reply` is invoked from inside a function tool, defaults to `"none"`. To learn more, see [Per-response tools and tool choice](#per-response-tools).

- **`tools`** _(list[str])_ (optional): Available in:
- [ ] Node.js
- [x] Python

List of tool IDs to make available for this reply. When set, only the listed tools can be used. IDs must match registered tools on the agent. To learn more, see [Per-response tools and tool choice](#per-response-tools).

- **`allow_interruptions`** _(boolean)_ (optional): If `True`, allow the user to interrupt the agent while speaking. (default `True`)

- **`chat_ctx`** _(ChatContext)_ (optional): The chat context to use for generating the reply. Defaults to the agent's current chat context. Pass a modified copy to fully control the context for this reply. To learn more, see [Using a custom chat context](#custom-chat-context).

#### Returns

Returns a [`SpeechHandle`](#speechhandle) object.

#### Events

This method triggers a [`speech_created`](https://docs.livekit.io/reference/agents/events.md#speech_created) event.

## Controlling agent speech

You can control agent speech using the `SpeechHandle` object returned by the `say()` and `generate_reply()` methods, and allowing user interruptions.

### SpeechHandle

The `say()` and `generate_reply()` methods return a `SpeechHandle` object, which lets you track the state of the agent's speech. This can be useful for coordinating follow-up actions, for example, notifying the user before ending the call.

**Python**:

```python
# The following is a shortcut for:
# handle = session.say("Goodbye for now.", allow_interruptions=False)
# await handle.wait_for_playout()
await session.say("Goodbye for now.", allow_interruptions=False)

```

---

**Node.js**:

```typescript
// The following is a shortcut for:
// const handle = session.say('Goodbye for now.', { allowInterruptions: false });
// await handle;
await session.say('Goodbye for now.', { allowInterruptions: false });

```

You can wait for the agent to finish speaking before continuing:

**Python**:

```python
handle = session.generate_reply(instructions="Tell the user we're about to run some slow operations.")

# perform an operation that takes time
...

await handle # finally wait for the speech

```

---

**Node.js**:

```typescript
const handle = session.generateReply({
  instructions: "Tell the user we're about to run some slow operations."
});

// perform an operation that takes time
...

await handle; // finally wait for the speech

```

The following example makes a web request for the user, and cancels the request when the user interrupts:

**Python**:

```python
async with aiohttp.ClientSession() as client_session:
    web_request = client_session.get('https://api.example.com/data')
    handle = await session.generate_reply(instructions="Tell the user we're processing their request.")
    if handle.interrupted:
        # if the user interrupts, cancel the web_request too
        web_request.cancel()

```

---

**Node.js**:

```typescript
import { Task } from '@livekit/agents';

const webRequestTask = Task.from(async (controller) => {
  const response = await fetch('https://api.example.com/data', {
    signal: controller.signal
  });
  return response.json();
});

const handle = await session.generateReply({
  instructions: "Tell the user we're processing their request.",
});

if (handle.interrupted) {
  // if the user interrupts, cancel the web_request too
  webRequestTask.cancel();
}

```

`SpeechHandle` has an API similar to `asyncio.Future`, allowing you to add a callback:

**Python**:

```python
handle = session.say("Hello world")
handle.add_done_callback(lambda _: print("speech done"))

```

---

**Node.js**:

```typescript
const handle = session.say('Hello world');
handle.then(() => console.log('speech done'));

```

### Getting the current speech handle

The agent session's active speech handle, if any, is available with the `current_speech` property. If no speech is active, this property returns `None`. Otherwise, it returns the active `SpeechHandle`.

Use the active speech handle to coordinate with the speaking state. For instance, you can ensure that a hang up occurs only after the current speech has finished, rather than mid-speech:

**Python**:

```python
# to hang up the call as part of a function call
@function_tool
async def end_call(self, ctx: RunContext):
   """Use this tool when the user has signaled they wish to end the current call. The session ends automatically after invoking this tool."""
   await ctx.wait_for_playout() # let the agent finish speaking


   # call API to delete_room
   ...

```

---

**Node.js**:

```typescript
const endCall = llm.tool({
  name: 'endCall',
  description: 'End the call.',
  parameters: z.object({
    reason: z
      .enum([
        'assistant-ended-call',
        'sip-call-transferred',
        'user-ended-call',
        'unknown-error',
      ])
      .describe('The reason to end the call'),
  }),
  execute: async ({ reason }, { ctx }) => {
    await ctx.session.generateReply({
      userInput: `You are about to end the call due to ${reason}, notify the user with one last message`,
    });

    ctx.session.shutdown({ reason });
  },
});

```

### Interruptions

By default, the agent stops speaking when it detects that the user has started speaking. You can customize this behavior. To learn more, see [Interruptions](https://docs.livekit.io/agents/logic/turns.md#interruptions) in the Turn detection topic.

## Additional resources

To learn more, see the following resources.

- **[Audio customization](https://docs.livekit.io/agents/multimodality/audio/customization.md)**: Customize pronunciation, adjust speech volume, and cache TTS responses.

- **[Background audio](https://docs.livekit.io/agents/multimodality/audio/background-audio.md)**: Add ambient sounds, thinking sounds, and on-demand audio playback.

- **[Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md)**: Use the quickstart as a starting base for adding audio code.

- **[Speech related event](https://docs.livekit.io/agents/build/events.md#speech_created)**: Learn more about the `speech_created` event, triggered when new agent speech is created.

- **[Text-to-speech (TTS)](https://docs.livekit.io/agents/models/tts.md)**: TTS models for pipeline agents.

- **[Speech-to-speech](https://docs.livekit.io/agents/models/realtime.md)**: Realtime models that understand speech input and generate speech output directly.

- **[Custom voices](https://docs.livekit.io/agents/models/tts/custom-voices.md)**: Create voice clones from short audio samples.

---

This document was rendered at 2026-08-28T04:22:11.853Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/audio.md](https://docs.livekit.io/agents/multimodality/audio.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-3"></a>
## Page 3: agents/multimodality/text/
**Original URL:** https://docs.livekit.io/agents/multimodality/text/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/text.md

LiveKit docs › Build Agents › Multimodality › Text & transcriptions

---

# Text and transcriptions

> Integrate realtime text features into your agent.

## Overview

LiveKit Agents supports text inputs and outputs in addition to audio, based on the [text streams](https://docs.livekit.io/transport/data/text-streams.md) feature of the LiveKit SDKs. This guide explains what's possible and how to use it in your app.

> 💡 **Modality-aware prompts**
> 
> To give an agent different system prompts for voice and text input, see [modality-aware instructions](https://docs.livekit.io/agents/multimodality/instructions.md).

## Transcriptions

When an agent performs STT as part of its processing pipeline, the transcriptions are also published to the frontend in realtime. A text representation of the agent speech is also published in sync with audio playback when the agent speaks. These features are both enabled by default when using `AgentSession`.

Transcriptions use the `lk.transcription` text stream topic. They include a `lk.transcribed_track_id` attribute and the sender identity is the transcribed participant.

> ℹ️ **Migrating from TranscriptionReceived**
> 
> The `TranscriptionReceived` client event and the `publish_transcription()` method are deprecated. They use a separate delivery mechanism from text streams, so writing to the `lk.transcription` text stream doesn't trigger `TranscriptionReceived`. See the [migration guide](https://docs.livekit.io/reference/migration-guides/v0-migration/python.md#transcriptions) for details.

To disable transcription output, set `text_output=False` in `RoomOptions` (Python) or `transcriptionEnabled: false` in `outputOptions` (Node.js).

### Synchronized transcription forwarding

When both voice and transcription are enabled, the agent's speech is synchronized with its transcriptions, displaying text word by word as it speaks. If the agent is interrupted, the transcription stops and is truncated to match the spoken output.

#### Disabling synchronization

To send transcriptions to the client as soon as they become available, without synchronizing to the original speech, set `sync_transcription` to False in text output options.

**Python**:

```python
from livekit.agents import room_io

await session.start(
    agent=MyAgent(),
    room=ctx.room,
    room_options=room_io.RoomOptions(
        text_output=room_io.TextOutputOptions(
            sync_transcription=False
        ),
    ),
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

await session.start({
  agent: voice.Agent.create({
    instructions: 'You are a helpful assistant.',
  }),
  room: ctx.room,
  outputOptions: {
    syncTranscription: false,
  },
});

```

### Accessing from AgentSession

You can be notified within your agent whenever text input or output is committed to the chat history by listening to the [conversation_item_added](https://docs.livekit.io/reference/agents/events.md#conversation_item_added) event.

### TTS-aligned transcriptions

If your TTS provider supports it, you can enable TTS-aligned transcription forwarding to improve transcription synchronization to your frontend. This feature synchronizes the transcription output with the actual speech timing, enabling word-level synchronization. When using this feature, certain formatting may be lost from the original text (dependent on the TTS provider).

Currently, only the [Cartesia](https://docs.livekit.io/agents/models/tts/cartesia.md), [ElevenLabs](https://docs.livekit.io/agents/models/tts/elevenlabs.md), and [Rime](https://docs.livekit.io/agents/models/tts/rime.md) plugins support word-level transcription timing. For other providers, including LiveKit Inference, the alignment is applied at the sentence level and still improves synchronization reliability for multi-sentence turns.

To enable this feature, set `use_tts_aligned_transcript=True` in your `AgentSession` configuration:

**Python**:

```python
session = AgentSession(
    # ... stt, llm, tts, vad, etc...
    use_tts_aligned_transcript=True,
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const session = new voice.AgentSession({
  // ... vad, stt, tts, llm, etc.
  voiceOptions: {
    useTtsAlignedTranscript: true,
  },
});

```

To access timing information in your code, implement a [transcription_node](https://docs.livekit.io/agents/build/nodes.md#transcription-node) method in your agent. The iterator yields a `TimedString` which includes `start_time` and `end_time` for each word, in seconds relative to the start of the agent's current [turn](https://docs.livekit.io/agents/logic/turns.md).

> 🔥 **Experimental feature**
> 
> The `transcription_node` and `TimedString` implementations are experimental and may change in a future version of the SDK.

**Python**:

```python
async def transcription_node(
    self, text: AsyncIterable[str | TimedString], model_settings: ModelSettings
) -> AsyncGenerator[str | TimedString, None]:
    async for chunk in text:
        if isinstance(chunk, TimedString):
            logger.info(f"TimedString: '{chunk}' ({chunk.start_time} - {chunk.end_time})")
        yield chunk

```

---

**Node.js**:

```typescript
async transcriptionNode(
  text: ReadableStream<string | TimedString>,
  modelSettings: ModelSettings,
): Promise<ReadableStream<string | TimedString> | null> {
  return new ReadableStream({
    async start(controller) {
      const reader = text.getReader();
      try {
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          if (typeof value === 'object' && 'startTime' in value) {
            console.log(`TimedString: '${value.text}' (${value.startTime} - ${value.endTime})`);
          }
          controller.enqueue(value);
        }
        controller.close();
      } finally {
        reader.releaseLock();
      }
    },
  });
}

```

#### Timed transcripts

Timestamps on each transcript chunk let frontend clients sync the display to audio playback. Common use cases include captioning, clickable transcripts where selecting a word jumps to that moment in a recording, and time-aligned post-call analysis.

By default, the agent publishes plain text to `lk.transcription`. To publish each chunk as a JSON object containing the text plus its timing data, set `json_format=True` in `TextOutputOptions` (Python) or `jsonFormat: true` in `outputOptions` (Node.js).

**Python**:

```python
from livekit.agents import room_io

await session.start(
    agent=MyAgent(),
    room=ctx.room,
    room_options=room_io.RoomOptions(
        text_output=room_io.TextOutputOptions(
            json_format=True,
            sync_transcription=True,
        ),
    ),
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

await session.start({
  agent: new MyAgent(),
  room: ctx.room,
  outputOptions: {
    jsonFormat: true,
    syncTranscription: true,
  },
});

```

This example assumes TTS-aligned transcripts are enabled (see [TTS-aligned transcriptions](#tts-aligned-transcriptions)) and a TTS that emits word-level timestamps.

Each chunk has the following format:

```json
{"text": "hello", "start_time": 0.42, "end_time": 0.67}

```

The `text` field is always present. The `start_time` and `end_time` fields appear when the underlying chunk is a `TimedString`.

Word-level timing depends on the TTS provider:

- [Cartesia](https://docs.livekit.io/agents/models/tts/cartesia.md) and [ElevenLabs](https://docs.livekit.io/agents/models/tts/elevenlabs.md) emit word-level timestamps directly.
- Non-streaming TTS providers wrapped with `StreamAdapter` emit sentence-level timestamps.
- Other providers emit JSON objects without timing fields, but the `text` field is still present.

## Text transforms

The `tts_text_transforms` option on `AgentSession` lets you modify text before it reaches the TTS. Transforms are applied in order, and each one receives the streaming text output of the previous transform.

Two built-in string transforms are available: `"filter_markdown"` strips Markdown formatting and `"filter_emoji"` removes emoji characters. When `tts_text_transforms` is not set, both are applied by default. Set `tts_text_transforms` to `None` (Python) or `null` (Node.js) to turn off all transforms.

> 🔀 **Behavior change in Node.js v1.4.2**
> 
> As of `@livekit/agents@1.4.2`, `filter_markdown` and `filter_emoji` are applied by default in Node.js. In prior versions, TTS input was unfiltered. If you need raw text to reach the TTS, set `ttsTextTransforms: null`.

### Built-in replace transform

Use `text_transforms.replace()` to substitute words or phrases before they reach the TTS. This is useful for fixing pronunciation of acronyms, proper nouns, and any other terms that need phonetic overrides. The transform buffers across token boundaries so replacements work even when a term is split across streaming chunks.

**Python**:

```python
from livekit.agents import AgentSession, text_transforms

session = AgentSession(
    stt="deepgram/nova-3:en",
    llm="google/gemma-4-31b-it",
    tts="cartesia/sonic-3",
    tts_text_transforms=[
        "filter_emoji",
        "filter_markdown",
        text_transforms.replace({
            "LiveKit": "<<ˈ|l|aɪ|v>> <<ˈ|k|ɪ|t>>",
            "API": "A P I",
            "RTMP": "R T M P",
        }),
    ],
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const session = new voice.AgentSession({
  stt: 'deepgram/nova-3:en',
  llm: 'google/gemma-4-31b-it',
  tts: 'cartesia/sonic-3',
  ttsTextTransforms: [
    'filter_emoji',
    'filter_markdown',
    voice.textTransforms.replace({
      'LiveKit': 'Lyve Kit',
      'API': 'A P I',
      'RTMP': 'R T M P',
    }),
  ],
});

```

The `replace()` function accepts a dictionary (Python) or object (Node.js) mapping source terms to their replacements, and an optional `case_sensitive` (Python) or `caseSensitive` (Node.js) flag (default: case-insensitive).

The `<<ˈ|l|aɪ|v>>` markers in the Python example are Cartesia's inline phoneme syntax: each `<<...>>` block is a pronunciation override expressed as `|`-separated IPA symbols, with `ˈ` marking primary stress. This syntax is specific to Cartesia models (such as `cartesia/sonic-3`). Other TTS providers might support phonemes or other methods of customizing pronunciation. Check provider docs before copying these replacements to a different TTS. For Cartesia specifically, see [Customizing pronunciation](https://docs.livekit.io/agents/models/tts/cartesia.md#customizing-pronunciation) on the Cartesia TTS page.

### Custom callable transforms

You can pass any callable as a transform. In Python, use the signature `Callable[[AsyncIterable[str]], AsyncIterable[str]]`. In Node.js, use `(text: ReadableStream<string>) => ReadableStream<string>`. This lets you implement custom text processing logic that operates on the streaming text.

**Python**:

```python
from collections.abc import AsyncIterable
from livekit.agents import AgentSession, text_transforms


async def redact_emails(text: AsyncIterable[str]) -> AsyncIterable[str]:
    """Replace email addresses with 'email redacted'."""
    import re
    buffer = ""
    async for chunk in text:
        buffer += chunk
        # flush everything before the last potential partial email
        safe, _, tail = buffer.rpartition(" ")
        if safe:
            safe = re.sub(r"\S+@\S+\.\S+", "email redacted", safe)
            yield safe + " "
            buffer = tail
    if buffer:
        buffer = re.sub(r"\S+@\S+\.\S+", "email redacted", buffer)
        yield buffer


session = AgentSession(
    stt="deepgram/nova-3:en",
    llm="google/gemma-4-31b-it",
    tts="inworld/inworld-tts-2",
    tts_text_transforms=[
        "filter_markdown",
        redact_emails,
        text_transforms.replace({"ACME": "Acme Corp"}),
    ],
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const redactEmails = (text: ReadableStream<string>): ReadableStream<string> => {
  return new ReadableStream({
    async start(controller) {
      const reader = text.getReader();
      let buffer = '';
      try {
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          buffer += value;
          // flush everything before the last potential partial email
          const lastSpace = buffer.lastIndexOf(' ');
          if (lastSpace !== -1) {
            const safe = buffer.slice(0, lastSpace + 1);
            controller.enqueue(safe.replace(/\S+@\S+\.\S+/g, 'email redacted'));
            buffer = buffer.slice(lastSpace + 1);
          }
        }
        if (buffer) {
          controller.enqueue(buffer.replace(/\S+@\S+\.\S+/g, 'email redacted'));
        }
        controller.close();
      } finally {
        reader.releaseLock();
      }
    },
  });
};

const session = new voice.AgentSession({
  stt: 'deepgram/nova-3:en',
  llm: 'google/gemma-4-31b-it',
  tts: 'inworld/inworld-tts-2',
  ttsTextTransforms: [
    'filter_markdown',
    redactEmails,
    voice.textTransforms.replace({ 'ACME': 'Acme Corp' }),
  ],
});

```

Transforms are applied in order. In the examples above, Markdown is stripped first, then emails are redacted, then text replacements are applied.

## Text input

Your agent monitors the `lk.chat` text stream topic for incoming text messages from its linked participant. The agent interrupts its current speech, if any, to process the message and generate a new response.

To disable text input, set `text_input=False` in `RoomOptions` (Python) or `textEnabled: false` in `RoomInputOptions` (Node.js).

### Sending from frontend

Use the `sendText` method to send text messages:

**JavaScript**:

```typescript
const text = 'Hello how are you today?';
const info = await room.localParticipant.sendText(text, {
  topic: 'lk.chat',
});

```

---

**Swift**:

```swift
let text = "Hello how are you today?"
let info = try await room.localParticipant.sendText(text, for: "lk.chat")

```

### Manual input

To insert text input and generate a response, use the `generate_reply` method of AgentSession: `session.generate_reply(user_input="...")`.

### Custom handling

You can customize how agents handle incoming text input, replacing the default behavior with custom logic, such as command processing, message filtering, or custom response generation.

To implement custom text input handling, provide a text input callback function in room options:

**Python**:

In Python, use the `TextInputOptions` parameter for `text_input` in `RoomOptions` to provide a text input callback function:

```python
from livekit.agents import AgentServer, AgentSession
from livekit.agents import room_io


def custom_text_input_handler(session: AgentSession, event: room_io.TextInputEvent) -> None:
    # Access the incoming text message
    message = event.text

    # Handle commands
    if message.startswith("/"):
        if message == "/help":
            session.say("Available commands: /help, /status")
            return
        elif message == "/status":
            session.say("Agent is running normally")
            return

    # Apply custom filtering
    if any(word in message.lower() for word in ["spam", "inappropriate"]):
        session.say("I can't respond to that type of message.")
        return

    # Default behavior: interrupt and generate reply
    session.interrupt()
    session.generate_reply(user_input=message)


server = AgentServer()

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: JobContext):
    # Create the session
    session = AgentSession(
        # ... stt, llm, tts, etc.
    )

    # Start session with custom text input handler
    session.start(
        # other options...
        room_options=room_io.RoomOptions(
            text_input=room_io.TextInputOptions(
                text_input_cb=custom_text_input_handler
            )
        )
    )

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const customTextInputHandler = (session: voice.AgentSession, event: voice.TextInputEvent): void => {
  const message = event.text;

  if (message.startsWith('/')) {
    if (message === '/help') {
      session.say('Available commands: /help, /status');
      return;
    }
    if (message === '/status') {
      session.say('Agent is running normally');
      return;
    }
  }

  if (['spam', 'inappropriate'].some((word) => message.toLowerCase().includes(word))) {
    session.say("I can't respond to that type of message.");
    return;
  }

  session.interrupt();
  session.generateReply({ userInput: message });
};

await session.start({
  agent,
  room: ctx.room,
  inputOptions: {
    textInputCallback: customTextInputHandler,
  },
});

```

## Text-only sessions

You have two options for disabling audio input and output for text-only sessions:

- Permanently: Disable audio for the entire session to prevent any audio tracks from being published to the room.
- Temporarily: Toggle audio input and output dynamically for hybrid sessions.

Turn off audio input and output for a text-only session, or dynamically, using the `session.input.set_audio_enabled()` and `session.output.set_audio_enabled()` methods.

### Disable audio for the entire session

You can turn off audio input or output for the entire session when you start a session. When audio output is disabled, the agent does not publish audio tracks to the room. Text responses are sent without the `lk.transcribed_track_id` attribute and without speech synchronization.

**Python**:

In Python, you can turn off audio input and output in `RoomOptions` when you start a session:

```python
session.start(
    # ... agent, room
    room_options=RoomOptions(
      audio_input=False,
      audio_output=False,
    ),
)

```

---

**Node.js**:

In Node.js, you can turn off audio input and output in `inputOptions` and `outputOptions` when you start a session:

```typescript
await session.start({
  // ... agent, room
  inputOptions: {
    audioEnabled: false,
  },
  outputOptions: {
    audioEnabled: false,
  },
});

```

### Toggle audio input and output

For hybrid sessions where audio input and output might be used, such as when a user toggles an audio switch, you can allow the agent to toggle audio input and output dynamically using `session.input.set_audio_enabled()` and `session.output.set_audio_enabled()`. This still publishes the audio track to the room.

**Python**:

```python
session = AgentSession(...)

# start with audio disabled
session.input.set_audio_enabled(False)
session.output.set_audio_enabled(False)
await session.start(...)

# user toggles audio switch
@room.local_participant.register_rpc_method("toggle_audio")
async def on_toggle_audio(data: rtc.RpcInvocationData) -> None:
    session.input.set_audio_enabled(not session.input.audio_enabled)
    session.output.set_audio_enabled(not session.output.audio_enabled)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const session = new voice.AgentSession({
  // ... configuration
});

// start with audio disabled
session.input.setAudioEnabled(false);
session.output.setAudioEnabled(false);
await session.start({
  agent,
  room: ctx.room,
});

// user toggles audio switch
ctx.room.localParticipant.registerRpcMethod('toggle_audio', async (data) => {
  session.input.setAudioEnabled(!session.input.audioEnabled);
  session.output.setAudioEnabled(!session.output.audioEnabled);
});

```

You can also temporarily pause audio input to prevent speech from being queued for response. This is useful when an agent needs to run non-verbal jobs and you want to stop the agent from listening to any input. This prevents the audio track from being published to the room.

> 💡 **Tip**
> 
> This is different from [manual turn control](https://docs.livekit.io/agents/logic/turns.md#manual) which is used for interfaces such as push-to-talk.

**Python**:

```python
# if currently speaking, stop first so states don't overlap
session.interrupt()

session.input.set_audio_enabled(False) # stop listening
try:
    await do_job()  # your non-verbal job
finally:
    session.input.set_audio_enabled(True) # start listening again

```

---

**Node.js**:

```typescript
try {
  // if currently speaking, stop first so states don't overlap
  session.interrupt();

  session.input.setAudioEnabled(false); // stop listening
  await doJob(); // your non-verbal job
} finally {
  session.input.setAudioEnabled(true); // start listening again
}

async function doJob() {
  // placeholder for actual work
  return new Promise((resolve) => setTimeout(resolve, 7000));
}

```

## Frontend rendering

LiveKit client SDKs have native support for text streams. For more information, see the [text streams](https://docs.livekit.io/transport/data/text-streams.md) documentation.

### Receiving text streams

> ℹ️ **Replaces TranscriptionReceived**
> 
> `registerTextStreamHandler` replaces the deprecated `TranscriptionReceived` event. In React, use [`useTranscriptions`](https://docs.livekit.io/reference/components/react/hook/usetranscriptions.md) instead of the deprecated `useTrackTranscriptions` hook.

Use the `registerTextStreamHandler` method to receive incoming transcriptions or text.

When an audio track is transcribed, the speech is split into segments. For each segment, two streams are produced:

- `interim_stream`: while the segment is being processed
- `final_stream`: when the segment is complete

> 💡 **Tip**
> 
> Use the `lk.transcription_final` value to determine if the stream is interim (`false`) or final (`true`).

These streams share the same `segment_id` and `transcribed_track_id`, so logging every message can produce duplicates. Tracking `interim_stream` is only recommended for use cases that require live typing updates. Replace interim messages with the final message when `lk.transcription_final` is `true`.

For React development, use the [`useTranscriptions`](https://docs.livekit.io/reference/components/react/hook/usetranscriptions.md) hook.

**Android**:

```kotlin
// Register a text stream handler for transcription
room.registerTextStreamHandler("lk.transcription") { reader, participantIdentity ->
    // Launch a coroutine to handle the async reading
    scope.launch {
        try {
            // Read all the text data from the stream
            val messages = reader.readAll()
            val fullMessage = messages.joinToString("")

            val isFinal = reader.info.attributes["lk.transcription_final"] == "true"            
            // Check if this is a transcription by looking at the stream attributes
            val isTranscription = reader.info.attributes["lk.transcribed_track_id"] != null
            val segmentId = reader.info.attributes["lk.segment_id"]
            
            if (isTranscription) {
                Log.d("TextStream", "New transcription from $participantIdentity [final=$isFinal, segment=$segmentId]: $fullMessage")
            } else {
                Log.d("TextStream", "New message from $participantIdentity: $fullMessage")
            }
        } catch (e: Exception) {
            Log.e("TextStream", "Error reading text stream", e)
        }
    }
}

```

---

**Flutter**:

```dart
room.registerTextStreamHandler('lk.transcription', (TextStreamReader reader, String participantIdentity) async {
  final message = await reader.readAll();

  final isTranscription = reader.info?.attributes['lk.transcribed_track_id'] != null;
  final isFinal = reader.info?.attributes['lk.transcription_final'] == 'true';
  final segmentId = reader.info?.attributes['lk.segment_id']
  
  if (isTranscription) {
    print('New transcription from $participantIdentity [final=$isFinal, segment=$segmentId]: $message');
  } else {
    print('New message from $participantIdentity: $message');
  }
});

```

---

**JavaScript**:

```typescript
room.registerTextStreamHandler('lk.transcription', async (reader, participantInfo) => {
  const message = await reader.readAll();
  if (reader.info.attributes['lk.transcribed_track_id']) {
    console.log(`New transcription from ${participantInfo.identity}: ${message}`);
  } else {
    console.log(`New message from ${participantInfo.identity}: ${message}`);
  }
});

```

---

**Swift**:

```swift
try await room.registerTextStreamHandler(for: "lk.transcription") { reader, participantIdentity in
    let message = try await reader.readAll()
    if let transcribedTrackId = reader.info.attributes["lk.transcribed_track_id"] {
        print("New transcription from \(participantIdentity): \(message)")
    } else {
        print("New message from \(participantIdentity): \(message)")
    }
}

```

---

This document was rendered at 2026-08-28T04:22:11.879Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/text.md](https://docs.livekit.io/agents/multimodality/text.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-4"></a>
## Page 4: agents/multimodality/instructions/
**Original URL:** https://docs.livekit.io/agents/multimodality/instructions/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/instructions.md

LiveKit docs › Build Agents › Multimodality › Modality-aware instructions

---

# Modality-aware instructions

> Give your agent different system prompts for voice and text input.

## Overview

A single agent can serve both voice and text users in the same session, but the two input types can benefit from different instructions. Spoken input arrives as imperfect transcription and can contain relative expressions (for example, "next Tuesday"), self-corrections, and filler words, so the LLM might need additional guidance to interpret it correctly. Typed input, on the other hand, is usually more precise and literal, so these same instructions can degrade text responses by adding spoken-style confirmations or stripping useful formatting.

The `Instructions` class holds two variants of your system prompt, one for `audio` and one for `text`. The framework applies the variant that matches each turn's input modality before calling the LLM, so voice turns get the audio prompt and text turns get the text prompt automatically.

> ℹ️ **Beta in Python**
> 
> In Python, `Instructions` is exported from `livekit.agents.beta` and is subject to change. In Node.js, it's a stable export of the main `llm` namespace (and also re-exported from `beta`).

## Define instructions per modality

Create an `Instructions` object with `audio` and `text` variants and pass it wherever you would pass an instructions string, such as the `Agent` constructor. The `text` variant is optional and falls back to the `audio` variant when omitted.

**Python**:

```python
from livekit.agents import Agent
from livekit.agents.beta import Instructions

instructions = Instructions(
    audio=(
        "You are a scheduling assistant. The user is speaking, so their input may be "
        "imperfect. Resolve spoken expressions like 'next Tuesday' to concrete dates, "
        "honor verbal self-corrections, and confirm the date and time out loud before booking."
    ),
    text=(
        "You are a scheduling assistant. The user is typing, so take their input literally. "
        "Accept exact dates and times in any common format and skip verbal confirmations."
    ),
)


class SchedulingAgent(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=instructions)

```

---

**Node.js**:

```typescript
import { llm, voice } from '@livekit/agents';

const instructions = new llm.Instructions({
  audio:
    'You are a scheduling assistant. The user is speaking, so their input may be ' +
    "imperfect. Resolve spoken expressions like 'next Tuesday' to concrete dates, " +
    'honor verbal self-corrections, and confirm the date and time out loud before booking.',
  text:
    'You are a scheduling assistant. The user is typing, so take their input literally. ' +
    'Accept exact dates and times in any common format and skip verbal confirmations.',
});

const schedulingAgent = voice.Agent.create({ instructions });

```

## How variants are applied

During a session, the framework selects the variant that matches the input modality of each turn: the `audio` variant for spoken turns and the `text` variant for typed turns. Both variants are preserved across turns, so an agent that handles a voice turn followed by a text turn uses the correct prompt for each.

## Select the active variant

When you [generate a reply manually](https://docs.livekit.io/agents/multimodality/audio.md#generate_reply), specify the variant with the `input_modality` (Python) or `inputModality` (Node.js) parameter:

**Python**:

```python
# Use the audio variant for this reply
session.generate_reply(input_modality="audio")

```

---

**Node.js**:

```typescript
// Use the audio variant for this reply
session.generateReply({ inputModality: 'audio' });

```

To explicitly set the active variant, use `as_modality` (Python) or `asModality` (Node.js). This returns a copy of the instructions with the selected variant active. Both variants are preserved, so you can switch between them as needed.

**Python**:

```python
# Return a copy whose active value is the text variant
text_first = instructions.as_modality("text")

```

---

**Node.js**:

```typescript
// Return a copy whose active value is the text variant
const textFirst = instructions.asModality('text');

```

## Compose instructions

You can build instructions from reusable pieces while keeping both variants intact. A shared base prompt can be combined with modality-specific guidance using concatenation and templating.

**Python**:

In Python, `Instructions` subclasses `str`. Use `+` to concatenate and `format` to substitute values. Both handle each variant separately:

```python
base = Instructions(
    audio="You are Alex, a scheduling assistant.\n{modality_specific}",
    text="You are Alex, a scheduling assistant.\n{modality_specific}",
)

modality_specific = Instructions(
    audio="Resolve spoken dates and confirm out loud.",
    text="Accept literal dates and skip confirmations.",
)

# `format` applies to both variants at once
instructions = base.format(modality_specific=modality_specific)

# `+` also works and preserves both variants
instructions = instructions + "\nThe current date is 2026-05-29."

```

---

**Node.js**:

In Node.js, use the `Instructions.tpl` tagged template to compose with template literals, or `concatInstructions` to join a mix of strings and `Instructions`. Both handle each variant separately:

```typescript
import { llm } from '@livekit/agents';

const modalitySpecific = new llm.Instructions({
  audio: 'Resolve spoken dates and confirm out loud.',
  text: 'Accept literal dates and skip confirmations.',
});

// `tpl` interpolates each variant from any embedded Instructions
const instructions = llm.Instructions.tpl`You are Alex, a scheduling assistant.
${modalitySpecific}
The current date is 2026-05-29.`;

// `concatInstructions` joins strings and Instructions, preserving both variants
const combined = llm.concatInstructions('Base prompt. ', modalitySpecific);

```

## Customize built-in tasks

Available in (BETA):
- [ ] Node.js
- [x] Python

[Prebuilt tasks](https://docs.livekit.io/agents/prebuilt/tasks.md) ship with their own default prompts. The beta `InstructionParts` type lets you customize those prompts without rewriting them. Set `persona` to change the agent's identity and `extra` to append domain-specific context. Leave a field unset to keep the task's built-in default, or set it to an empty string to remove that section entirely. Each field accepts a plain string or an `Instructions` object, so customizations can themselves be modality-aware.

To apply a customization, pass an `InstructionParts` object as a task's `instructions` argument:

```python
from livekit.agents.beta import Instructions
from livekit.agents.beta.workflows import GetEmailTask, InstructionParts

task = GetEmailTask(
    instructions=InstructionParts(
        persona="You are Riley, a friendly intake assistant collecting a contact email.",
        # `extra` is itself modality-aware: confirm out loud for voice, stay quiet for text
        extra=Instructions(
            audio="Confirm the spelling out loud, letter by letter, for unusual domains.",
            text="Accept the email exactly as typed; only re-prompt if it's clearly malformed.",
        ),
    )
)

```

## Additional resources

A complete, runnable example agent that sets different instructions for voice and text users:

- **[Per-modality instructions (Node.js)](https://github.com/livekit/agents-js/blob/main/examples/src/instructions_per_modality.ts)**: A scheduling assistant with separate audio and text prompts, built with the Node.js SDK.

---

This document was rendered at 2026-08-28T04:22:11.862Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/instructions.md](https://docs.livekit.io/agents/multimodality/instructions.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-5"></a>
## Page 5: agents/multimodality/vision/
**Original URL:** https://docs.livekit.io/agents/multimodality/vision/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/vision.md

LiveKit docs › Build Agents › Multimodality › Images & video › Overview

---

# Images and video

> Process images and video input, and send visual output with avatars and byte streams.

## Overview

LiveKit Agents supports images and video as both input and output modalities. On the input side, you can add images to your agent's chat context, receive images from the frontend, sample video frames, or enable live video input with a supported realtime model. On the output side, you can send images to the frontend using [byte streams](https://docs.livekit.io/transport/data/byte-streams.md) or add a virtual avatar for lifelike video output.

## In this section

This page provides an overview of image and video capabilities. The following pages in this section cover each topic in detail:

| Topic | Description |
| [Images](https://docs.livekit.io/agents/multimodality/vision/images.md) | Add images to your agent's context, receive images from the frontend, and send images back to users. |
| [Video](https://docs.livekit.io/agents/multimodality/vision/video.md) | Sample video frames, enable live video input, and add virtual avatars for video output. |

## Additional resources

- **[Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md)**: Use the quickstart as a starting base for adding vision code.

- **[Byte streams](https://docs.livekit.io/transport/data/byte-streams.md)**: Send and receive images and files with byte streams.

- **[Virtual avatar models](https://docs.livekit.io/agents/models/avatar.md)**: Detailed setup guides for each avatar provider.

- **[Frontend avatars](https://docs.livekit.io/frontends/build/virtual-avatars.md)**: Build frontends that render avatar video.

- **[Gemini Vision Assistant](https://docs.livekit.io/reference/recipes/gemini_live_vision.md)**: A voice AI agent with video input powered by Gemini Live.

- **[Camera and microphone](https://docs.livekit.io/transport/media/publish.md)**: Publish camera and microphone tracks from your frontend.

---

This document was rendered at 2026-08-28T04:22:11.862Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/vision.md](https://docs.livekit.io/agents/multimodality/vision.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-6"></a>
## Page 6: agents/multimodality/audio/customization/
**Original URL:** https://docs.livekit.io/agents/multimodality/audio/customization/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/audio/customization.md

LiveKit docs › Build Agents › Multimodality › Speech & audio › Audio customization

---

# Audio customization

> Cache TTS responses, customize pronunciation, and adjust speech volume.

## Overview

LiveKit Agents provides several ways to customize how your agent sounds. You can adjust pronunciation of specific words, control speech volume, and cache TTS responses for fixed phrases to avoid redundant TTS calls and reduce latency.

## Caching TTS responses

For fixed phrases like greetings, hold messages, and error prompts, you can avoid TTS calls and save tokens by providing pre-synthesized audio to `session.say(text, audio=...)`. Playback uses your audio, and the text is still used for the transcript and chat context.

There are three approaches:

- [Pre-synthesized or prerecorded](#caching-tts-prerecorded) — Use audio you already have (files or one-time synthesis at startup). Best when the set of phrases is known and stable.
- [Automatic caching (reuse by key)](#caching-tts-automatic) — Synthesize on first use and cache frames by text. Reuse the same audio whenever that text is spoken again. Best when the agent might repeat the same phrases during a session or across sessions.
- [Using cached TTS in a tool call](#cached-tts-in-tools) — Play a pre-synthesized hold message while a tool executes, and cancel it early if the API returns quickly.

### Using pre-synthesized or prerecorded audio

Prerecord phrases as audio files or synthesize once at startup, load the audio into frames, and pass the frames to `say()` as the `audio` argument.

**Python**:

```python
from livekit.agents.utils.audio import audio_frames_from_file

await session.say(
    "Your phrase",
    audio=audio_frames_from_file(path, sample_rate=24000, num_channels=1),
)

```

---

**Node.js**:

```typescript
import { audioFramesFromFile } from '@livekit/agents';

await session.say('Your phrase', {
  audio: audioFramesFromFile(path, { sampleRate: 24000, numChannels: 1 }),
});

```

- **[Playing Audio](https://docs.livekit.io/reference/recipes/playing_audio.md)**: Full example of loading a WAV and streaming it via `say()` with the `audio` parameter, the same pattern used above for cached TTS.

### Automatic caching (reuse by key)

To reuse TTS output whenever the same text is spoken, synthesize on first use and cache the frames keyed by text. Use the same TTS instance you pass to `AgentSession`. On a cache hit, pass the cached frames to `say(text, audio=...)`, and on a cache miss, call `tts.synthesize(text)`, collect the frames, store them, then pass to `say()`.

To cache TTS for pipeline output (LLM-generated speech) as well, you can implement the same cache-and-reuse logic inside a [custom TTS node](https://docs.livekit.io/agents/build/nodes.md#tts_node). Be aware that cache lookup might require the full text segment, which can increase time-to-first-byte.

**Python**:

```python
from livekit import rtc
from livekit.agents import AgentSession

# Hold a reference to the TTS instance you pass to AgentSession.
tts_cache: dict[str, list[rtc.AudioFrame]] = {}

async def say_cached(session: AgentSession, tts, text: str) -> None:
    if text not in tts_cache:
        stream = tts.synthesize(text)
        frames: list[rtc.AudioFrame] = []
        async for event in stream:
            frames.append(event.frame)
        tts_cache[text] = frames

    async def audio_gen():
        for frame in tts_cache[text]:
            yield frame

    await session.say(text, audio=audio_gen())

```

---

**Node.js**:

```typescript
import { toStream, voice } from '@livekit/agents';
import type { AudioFrame } from '@livekit/rtc-node';

// Hold a reference to the TTS instance you pass to AgentSession.
const ttsCache = new Map<string, AudioFrame[]>();

async function sayCached(
  session: voice.AgentSession,
  tts: { synthesize(text: string): AsyncIterableIterator<{ frame: AudioFrame }> },
  text: string,
): Promise<void> {
  let frames = ttsCache.get(text);
  if (!frames) {
    frames = [];
    for await (const event of tts.synthesize(text)) {
      frames.push(event.frame);
    }
    ttsCache.set(text, frames);
  }

  async function* cachedAudio() {
    for (const frame of frames) {
      yield frame;
    }
  }

  // say() takes a ReadableStream, so wrap the async generator with toStream()
  await session.say(text, { audio: toStream(cachedAudio()) });
}

```

### Using cached TTS in a tool call

A common use case for cached TTS is playing a hold message like "let me check that for you" at the start of a [function tool](https://docs.livekit.io/agents/logic/tools.md) while waiting for an external API. Pre-synthesize the audio once at startup, then play it with `say()` inside the tool. If the API returns before the message finishes, interrupt the speech handle so the agent can immediately speak the result.

> ℹ️ **Note**
> 
> Don't `await` the `say()` call inside the tool. Awaiting waits for the speech to finish playing before continuing, which blocks the API call. Instead, capture the returned `SpeechHandle` and let the hold message play concurrently with your API request.

**Python**:

```python
from livekit import rtc
from livekit.agents import Agent, RunContext, function_tool

# Pre-synthesize a hold message once at startup
HOLD_FRAMES: list[rtc.AudioFrame] = []

async def preload_hold_message(tts) -> None:
    global HOLD_FRAMES
    async for event in tts.synthesize("Let me check that for you."):
        HOLD_FRAMES.append(event.frame)

class MyAgent(Agent):
    @function_tool()
    async def check_order_status(
        self,
        context: RunContext,
        order_id: str,
    ) -> str:
        """Check the status of an order.

        Args:
            order_id: The order ID to look up.
        """
        async def cached_audio():
            for frame in HOLD_FRAMES:
                yield frame

        # Play the hold message concurrently — don't await
        hold_handle = context.session.say(
            "Let me check that for you.",
            audio=cached_audio(),
            add_to_chat_ctx=False,
        )

        # Call the external API (runs while the hold message plays)
        result = await fetch_order_status(order_id)

        # If the API returned before the hold message finished, cancel it
        if not hold_handle.interrupted and not hold_handle.done():
            hold_handle.interrupt()

        return result

```

---

**Node.js**:

```typescript
import { llm, toStream, voice } from '@livekit/agents';
import type { AudioFrame } from '@livekit/rtc-node';
import { z } from 'zod';

// Pre-synthesize a hold message once at startup
let holdFrames: AudioFrame[] = [];

async function preloadHoldMessage(
  tts: { synthesize(text: string): AsyncIterableIterator<{ frame: AudioFrame }> },
) {
  holdFrames = [];
  for await (const event of tts.synthesize('Let me check that for you.')) {
    holdFrames.push(event.frame);
  }
}

const agent = voice.Agent.create({
  instructions: 'You are a helpful assistant.',
  tools: [
    llm.tool({
      name: 'checkOrderStatus',
      description: 'Check the status of an order.',
      parameters: z.object({
        orderId: z.string().describe('The order ID to look up.'),
      }),
      execute: async ({ orderId }, { ctx }) => {
        // Play the hold message concurrently — don't await
        const holdHandle = ctx.session.say('Let me check that for you.', {
          // say() takes a ReadableStream, so wrap the async generator with toStream()
          audio: toStream(
            (async function* () {
              for (const frame of holdFrames) {
                yield frame;
              }
            })(),
          ),
          addToChatCtx: false,
        });

        // Call the external API (runs while the hold message plays)
        const result = await fetchOrderStatus(orderId);

        // If the API returned before the hold message finished, cancel it
        if (!holdHandle.interrupted && !holdHandle.done()) {
          holdHandle.interrupt();
        }

        return result;
      },
    }),
  ],
});

```

> 💡 **Interruptions during the hold message**
> 
> If the user speaks during the hold message, the agent is interrupted by default and the hold message stops. The tool keeps running, and its result is recorded in the chat history so the model doesn't call the tool again, but the agent doesn't speak the result. To keep the agent engaged so it delivers the result (for example, when the tool performs a write operation), call `context.disallow_interruptions()` in Python or `ctx.disallowInterruptions()` in Node.js at the start of the tool.

## Customizing pronunciation

You can customize how your agent pronounces specific words using a built-in pronunciation map or a custom [tts_node](https://docs.livekit.io/agents/build/nodes.md#tts_node) override. Many TTS providers also support SSML tags for finer control — see the [SSML reference](#ssml-tags) below. Some providers offer their own pronunciation options — see [Google Gemini TTS](https://docs.livekit.io/agents/models/tts/gemini.md) and [Sarvam TTS](https://docs.livekit.io/agents/models/tts/sarvam.md) for examples.

### Using a pronunciation map

The simplest way to customize pronunciation is with a built-in map of terms to their replacement text. The agent applies the substitutions as a streaming text transform before TTS synthesis, handling terms that span across token boundaries without requiring a custom node override.

Use the [`text_transforms.replace()`](https://docs.livekit.io/agents/multimodality/text.md#built-in-replace-transform) function on `AgentSession` to define pronunciation replacements:

**Python**:

```python
from livekit.agents import AgentSession, text_transforms

session = AgentSession(
    # ... stt, llm, tts, etc.
    tts_text_transforms=[
        "filter_emoji",
        "filter_markdown",
        text_transforms.replace({
            "LiveKit": "Live Kit",
            "API": "A P I",
            "SQL": "sequel",
            "kubectl": "kube control",
            "nginx": "engine x",
        }),
    ],
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const session = new voice.AgentSession({
  // ... stt, llm, tts, etc.
  ttsTextTransforms: [
    'filter_emoji',
    'filter_markdown',
    voice.textTransforms.replace({
      'LiveKit': 'Live Kit',
      'API': 'A P I',
      'SQL': 'sequel',
      'kubectl': 'kube control',
      'nginx': 'engine x',
    }),
  ],
});

```

### Using a custom TTS node

For pronunciation logic beyond simple text replacement — such as regex-based matching, conditional rules, or context-dependent substitutions — use a custom [tts_node](https://docs.livekit.io/agents/build/nodes.md#tts_node) override:

** Filename: `agent.py`**

```python
async def tts_node(
    self,
    text: AsyncIterable[str],
    model_settings: ModelSettings
) -> AsyncIterable[rtc.AudioFrame]:
    # Pronunciation replacements for common technical terms and abbreviations.
    # Support for custom pronunciations depends on the TTS provider.
    pronunciations = {
        "API": "A P I",
        "REST": "rest",
        "SQL": "sequel",
        "kubectl": "kube control",
        "AWS": "A W S",
        "UI": "U I",
        "URL": "U R L",
        "npm": "N P M",
        "LiveKit": "Live Kit",
        "async": "a sink",
        "nginx": "engine x",
    }

    async def adjust_pronunciation(input_text: AsyncIterable[str]) -> AsyncIterable[str]:
        async for chunk in input_text:
            modified_chunk = chunk

            # Apply pronunciation rules
            for term, pronunciation in pronunciations.items():
                # Use word boundaries to avoid partial replacements
                modified_chunk = re.sub(
                    rf'\b{term}\b',
                    pronunciation,
                    modified_chunk,
                    flags=re.IGNORECASE
                )

            yield modified_chunk

    # Process with modified text through base TTS implementation
    async for frame in Agent.default.tts_node(
        self,
        adjust_pronunciation(text),
        model_settings
    ):
        yield frame

```

** Filename: `Required imports`**

```python
import re
from livekit import rtc
from livekit.agents.voice import ModelSettings
from livekit.agents import tts
from typing import AsyncIterable

```

** Filename: `agent.ts`**

```typescript
// Pronunciation replacements for common technical terms and abbreviations.
// Support for custom pronunciations depends on the TTS provider.
const pronunciations = {
  API: 'A P I',
  REST: 'rest',
  SQL: 'sequel',
  kubectl: 'kube control',
  AWS: 'A W S',
  UI: 'U I',
  URL: 'U R L',
  npm: 'N P M',
  LiveKit: 'Live Kit',
  async: 'a sink',
  nginx: 'engine x',
};

const agent = voice.Agent.create({
  instructions: 'You are a helpful voice AI assistant.',
  async ttsNode(ctx, text, modelSettings) {
    async function* adjustPronunciation(inputText: AsyncIterable<string>) {
      for await (const chunk of inputText) {
        let modifiedChunk = chunk;

        // Apply pronunciation rules
        for (const [term, pronunciation] of Object.entries(pronunciations)) {
          // Use word boundaries to avoid partial replacements
          const regex = new RegExp(`\\b${term}\\b`, 'gi');
          modifiedChunk = modifiedChunk.replace(regex, pronunciation);
        }

        yield modifiedChunk;
      }
    }

    // Process with modified text through base TTS implementation
    return voice.Agent.default.ttsNode(ctx.agent, adjustPronunciation(text), modelSettings);
  },
});

```

** Filename: `Required imports`**

```typescript
import { voice } from '@livekit/agents';

```

### SSML tags

Many TTS providers support Speech Synthesis Markup Language (SSML) tags for finer control over pronunciation. SSML support varies by provider — see your provider's page (for example, [ElevenLabs](https://docs.livekit.io/agents/models/tts/elevenlabs.md), [Cartesia](https://docs.livekit.io/agents/models/tts/cartesia.md), [Google](https://docs.livekit.io/agents/models/tts/google.md)) for details. The following table lists commonly supported SSML tags:

| SSML Tag | Description |
| `phoneme` | Specify phonetic pronunciation using IPA or X-SAMPA notation. |
| `say-as` | Specifies how to interpret the enclosed text. For example, use `character` to speak each character individually, or `date` to specify a calendar date. |
| `lexicon` | A custom dictionary that defines the pronunciation of certain words using phonetic notation or text-to-pronunciation mappings. |
| `emphasis` | Speak text with an emphasis. |
| `break` | Add a manual pause. |
| `prosody` | Controls pitch, speaking rate, and volume of speech output. |

## Adjusting speech volume

To adjust the volume of the agent's speech, add a processor to the `tts_node` or the `realtime_audio_output_node`.  Alternatively, you can also [adjust the volume of playback](https://docs.livekit.io/transport/media/subscribe.md#volume) in the frontend SDK.

The following example agent has an adjustable volume between 0 and 100, and offers a [tool call](https://docs.livekit.io/agents/build/tools.md) to change it.

** Filename: `agent.py`**

```python
class Assistant(Agent):
    def __init__(self) -> None:
        self.volume: int = 50
        super().__init__(
            instructions=f"You are a helpful voice AI assistant. Your starting volume level is {self.volume}."
        )

    @function_tool()
    async def set_volume(self, volume: int):
        """Set the volume of the audio output.

        Args:
            volume (int): The volume level to set. Must be between 0 and 100.
        """
        self.volume = volume

    # Audio node used by STT-LLM-TTS pipeline models
    async def tts_node(self, text: AsyncIterable[str], model_settings: ModelSettings):
        return self._adjust_volume_in_stream(
            Agent.default.tts_node(self, text, model_settings)
        )

    # Audio node used by realtime models
    async def realtime_audio_output_node(
        self, audio: AsyncIterable[rtc.AudioFrame], model_settings: ModelSettings
    ) -> AsyncIterable[rtc.AudioFrame]:
        return self._adjust_volume_in_stream(
            Agent.default.realtime_audio_output_node(self, audio, model_settings)
        )

    async def _adjust_volume_in_stream(
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
                yield self._adjust_volume_in_frame(f)

        if stream is not None:
            for f in stream.flush():
                yield self._adjust_volume_in_frame(f)

    def _adjust_volume_in_frame(self, frame: rtc.AudioFrame) -> rtc.AudioFrame:
        audio_data = np.frombuffer(frame.data, dtype=np.int16)
        audio_float = audio_data.astype(np.float32) / np.iinfo(np.int16).max
        audio_float = audio_float * max(0, min(self.volume, 100)) / 100.0
        processed = (audio_float * np.iinfo(np.int16).max).astype(np.int16)

        return rtc.AudioFrame(
            data=processed.tobytes(),
            sample_rate=frame.sample_rate,
            num_channels=frame.num_channels,
            samples_per_channel=len(processed) // frame.num_channels,
        )

```

** Filename: `Required imports`**

```python
import numpy as np
from typing import AsyncIterable
from livekit.agents import Agent, function_tool, utils
from livekit import rtc

```

** Filename: `agent.ts`**

```typescript
function createAssistant(initialVolume: number) {
  let volume = initialVolume;

  function adjustVolumeInFrame(frame: AudioFrame): AudioFrame {
    const audioData = new Int16Array(frame.data);
    const volumeMultiplier = Math.max(0, Math.min(volume, 100)) / 100.0;

    const processedData = new Int16Array(audioData.length);
    for (let i = 0; i < audioData.length; i++) {
      const floatSample = audioData[i]! / 32767.0;
      const adjustedSample = floatSample * volumeMultiplier;
      processedData[i] = Math.round(adjustedSample * 32767.0);
    }

    return new AudioFrame(processedData, frame.sampleRate, frame.channels, frame.samplesPerChannel);
  }

  async function* adjustVolumeInStream(
    audioStream: AsyncIterable<AudioFrame>,
  ): AsyncIterable<AudioFrame> {
    for await (const frame of audioStream) {
      yield adjustVolumeInFrame(frame);
    }
  }

  return voice.Agent.create({
    instructions: `You are a helpful voice AI assistant. Your starting volume level is ${initialVolume}.`,
    tools: [
      llm.tool({
        name: 'setVolume',
        description: 'Set the volume of the audio output.',
        parameters: z.object({
          volume: z
            .number()
            .min(0)
            .max(100)
            .describe('The volume level to set. Must be between 0 and 100.'),
        }),
        execute: async ({ volume: nextVolume }) => {
          volume = nextVolume;
          return `Volume set to ${nextVolume}`;
        },
      }),
    ],
    // Audio node used by STT-LLM-TTS pipeline models
    async ttsNode(ctx, text, modelSettings) {
      const baseStream = await voice.Agent.default.ttsNode(
        ctx.agent,
        text,
        modelSettings,
      );
      return baseStream ? adjustVolumeInStream(baseStream) : null;
    },
    // Audio node used by realtime models
    async realtimeAudioOutputNode(ctx, audio, modelSettings) {
      const baseStream = await voice.Agent.default.realtimeAudioOutputNode(
        ctx.agent,
        audio,
        modelSettings,
      );
      return baseStream ? adjustVolumeInStream(baseStream) : null;
    },
  });
}

```

** Filename: `Required imports`**

```typescript
import { llm, voice } from '@livekit/agents';
import { AudioFrame } from '@livekit/rtc-node';
import { z } from 'zod';

```

## Additional resources

- **[Speech & audio overview](https://docs.livekit.io/agents/multimodality/audio.md)**: Control agent speech, handle interruptions, and initiate speech.

- **[Text-to-speech (TTS)](https://docs.livekit.io/agents/models/tts.md)**: TTS models for pipeline agents.

- **[Pipeline nodes & hooks](https://docs.livekit.io/agents/logic/nodes.md)**: Customize agent behavior with pipeline nodes.

---

This document was rendered at 2026-08-28T04:22:12.954Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/audio/customization.md](https://docs.livekit.io/agents/multimodality/audio/customization.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-7"></a>
## Page 7: agents/multimodality/audio/background-audio/
**Original URL:** https://docs.livekit.io/agents/multimodality/audio/background-audio/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/audio/background-audio.md

LiveKit docs › Build Agents › Multimodality › Speech & audio › Background audio

---

# Background audio

> Add ambient sounds, thinking sounds, and on-demand audio playback to your agent.

## Overview

To add more realism to your agent, or add additional sound effects, publish background audio. This audio is played on a separate audio track. The `BackgroundAudioPlayer` class supports on-demand playback of custom audio as well as automatic ambient and thinking sounds synchronized to the agent lifecycle.

For a complete example, see the following recipe:

- **[Background audio example in Node.js](https://github.com/livekit/agents-js/blob/main/examples/src/background_audio.ts)**: A voice AI agent with background audio for ambiance.

## Create the player

The `BackgroundAudioPlayer` class manages audio playback to a room. It can also play ambient and thinking sounds automatically during the lifecycle of the agent session, if desired.

- **`ambient_sound`** _(AudioSource | AudioConfig | list[AudioConfig])_ (optional): Ambient sound plays on a loop in the background during the agent session. See [Supported audio sources](#audio-sources) and [Multiple audio clips](#multiple-audio-clips) for more details.

- **`thinking_sound`** _(AudioSource | AudioConfig | list[AudioConfig])_ (optional): Thinking sound plays while the agent is in the "thinking" state. See [Supported audio sources](#audio-sources) and [Multiple audio clips](#multiple-audio-clips) for more details.

Create the player within your entrypoint function:

**Python**:

```python
from livekit.agents import BackgroundAudioPlayer, AudioConfig, BuiltinAudioClip

# An audio player with automated ambient and thinking sounds
background_audio = BackgroundAudioPlayer(
    ambient_sound=AudioConfig(BuiltinAudioClip.OFFICE_AMBIENCE, volume=0.8),
    thinking_sound=[
        AudioConfig(BuiltinAudioClip.KEYBOARD_TYPING, volume=0.8),
        AudioConfig(BuiltinAudioClip.KEYBOARD_TYPING2, volume=0.7),
    ],
)

# An audio player with a custom ambient sound played on a loop
background_audio = BackgroundAudioPlayer(
    ambient_sound="/path/to/my-custom-sound.mp3",
)

# An audio player for on-demand playback only
background_audio = BackgroundAudioPlayer()

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const backgroundAudio = new voice.BackgroundAudioPlayer({
    ambientSound: {
            source: voice.BuiltinAudioClip.OFFICE_AMBIENCE,
            volume: 0.8,
    },
    thinkingSound: [
        { source: voice.BuiltinAudioClip.KEYBOARD_TYPING, volume: 0.8 },
        { source: voice.BuiltinAudioClip.KEYBOARD_TYPING2, volume: 0.7 },
    ],
});

// An audio player with a custom ambient sound played on a loop
const backgroundAudio2 = new voice.BackgroundAudioPlayer({
    ambientSound: "/path/to/my-custom-sound.mp3",
});

// An audio player for on-demand playback only
const backgroundAudio3 = new voice.BackgroundAudioPlayer();

```

## Start and stop the player

Call the `start` method after room connection and after starting the agent session. Pass the `room` and `agent_session` to `start()`. Ambient sounds, if any, begin playback immediately.

**Python**:

```python
await background_audio.start(room=ctx.room, agent_session=session)

```

---

**Node.js**:

```typescript
await backgroundAudio.start({ room: ctx.room, agentSession: session });

```

To stop and clean up the player, call the `aclose` (or `close` in Node.js) method. You must create a new player instance if you want to start again.

**Python**:

```python
await background_audio.aclose()

```

---

**Node.js**:

```typescript
await backgroundAudio.close();

```

## Play audio on-demand

You can play audio at any time, after starting the player, with the `play` method.

- **`audio`** _(AudioSource | AudioConfig | list[AudioConfig])_: The audio source or a probabilistic list of sources to play. To learn more, see [Supported audio sources](#audio-sources) and [Multiple audio clips](#multiple-audio-clips).

- **`loop`** _(boolean)_ (optional) - Default: `False`: Set to `True` to continuously loop playback.

For example, if you created `background_audio` in the [previous example](#create-the-player), you can play an audio file like this:

**Python**:

```python
background_audio.play("/path/to/my-custom-sound.mp3")

```

---

**Node.js**:

```typescript
backgroundAudio.play("/path/to/my-custom-sound.mp3");

```

The `play` method returns a `PlayHandle` which you can use to await or cancel the playback.

The following example uses the handle to await playback completion:

**Python**:

```python
# Wait for playback to complete
await background_audio.play("/path/to/my-custom-sound.mp3")

```

---

**Node.js**:

```typescript
const handle = await backgroundAudio.play("/path/to/my-custom-sound.mp3");

```

The next example shows the handle's `stop` method, which stops playback early:

**Python**:

```python
handle = background_audio.play("/path/to/my-custom-sound.mp3")
await(asyncio.sleep(1))
handle.stop() # Stop playback early

```

---

**Node.js**:

```typescript
const handle = backgroundAudio.play("/path/to/my-custom-sound.mp3");
await new Promise(resolve => setTimeout(resolve, 1000));
handle.stop(); // Stop playback early

```

### Fade audio in and out

Available in:
- [ ] Node.js
- [x] Python

To smooth the start and end of playback, set the `fade_in` and `fade_out` parameters on [`AudioConfig`](#multiple-audio-clips). Both fades use an equal-power curve, which applies a sinusoidal volume ramp that maintains more consistent perceived loudness than a linear fade. This produces smoother-sounding transitions at the beginning and end of playback.

With a nonzero `fade_out`, calling `stop()` starts the fade instead of cutting playback immediately. The handle isn't done until the fade completes, so `wait_for_playout()` returns after the fade-out finishes.

```python
handle = background_audio.play(
    AudioConfig(BuiltinAudioClip.OFFICE_AMBIENCE, volume=0.8, fade_in=1.0, fade_out=2.0)
)
await asyncio.sleep(5)

handle.stop()  # Starts a 2-second fade-out instead of stopping immediately
await handle.wait_for_playout()  # Returns after the fade-out completes

```

## Multiple audio clips

You can pass a list of audio sources to any of `play`, `ambient_sound`, or `thinking_sound`. The player selects a single entry in the list based on the `probability` parameter. This is useful to avoid repetitive sound effects. To allow for the possibility of no audio at all, ensure the sum of the probabilities is less than 1.

`AudioConfig` has the following properties:

- **`source`** _(AudioSource)_: The audio source to play. See [Supported audio sources](#audio-sources) for more details.

- **`volume`** _(float)_ (optional) - Default: `1`: The volume at which to play the given audio.

- **`probability`** _(float)_ (optional) - Default: `1`: The relative probability of selecting this audio source from the list.

- **`fade_in`** _(float)_ (optional) - Default: `0`: Available in:
- [ ] Node.js
- [x] Python

Duration in seconds to ramp the volume from 0 up to `volume` when playback starts. A value of `0` starts playback at full volume. See [Fade audio in and out](#fade-in-out) for more details.

- **`fade_out`** _(float)_ (optional) - Default: `0`: Available in:
- [ ] Node.js
- [x] Python

Duration in seconds to ramp the volume down to 0 when you call `stop()` on the play handle. A value of `0` stops playback immediately. See [Fade audio in and out](#fade-in-out) for more details.

**Python**:

```python
# Play the KEYBOARD_TYPING sound with an 80% probability and the KEYBOARD_TYPING2 sound with a 20% probability
background_audio.play([
    AudioConfig(BuiltinAudioClip.KEYBOARD_TYPING, volume=0.8, probability=0.8),
    AudioConfig(BuiltinAudioClip.KEYBOARD_TYPING2, volume=0.7, probability=0.2),
])

```

---

**Node.js**:

```typescript
// Play the KEYBOARD_TYPING sound with an 80% probability and the KEYBOARD_TYPING2 sound with a 20% probability
backgroundAudio.play([
    { source: voice.BuiltinAudioClip.KEYBOARD_TYPING, volume: 0.8, probability: 0.8 },
    { source: voice.BuiltinAudioClip.KEYBOARD_TYPING2, volume: 0.7, probability: 0.2 },
])

```

## Supported audio sources

The following audio sources are supported:

### Local audio file

Pass a string path to any local audio file. The player decodes files with FFmpeg via [PyAV](https://github.com/PyAV-Org/PyAV) and supports all common audio formats including MP3, WAV, AAC, FLAC, OGG, Opus, WebM, and MP4.

> 💡 **WAV files**
> 
> The player uses an optimized custom decoder to load WAV data directly to audio frames, without the overhead of FFmpeg. For small files, WAV is the highest-efficiency option.

### Built-in audio clips

The following built-in audio clips are available by default for common sound effects:

- `BuiltinAudioClip.OFFICE_AMBIENCE`: Chatter and general background noise of a busy office.
- `BuiltinAudioClip.KEYBOARD_TYPING`: The sound of an operator typing on a keyboard, close to their microphone.
- `BuiltinAudioClip.KEYBOARD_TYPING2`: A shorter version of `KEYBOARD_TYPING`.

### Raw audio frames

Pass an `AsyncIterator[rtc.AudioFrame]` to play raw audio frames from any source.

## Additional resources

- **[Background audio example in Node.js](https://github.com/livekit/agents-js/blob/main/examples/src/background_audio.ts)**: A voice AI agent with background audio for ambiance.

- **[Speech & audio overview](https://docs.livekit.io/agents/multimodality/audio.md)**: Control agent speech, handle interruptions, and initiate speech.

---

This document was rendered at 2026-08-28T04:22:12.965Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/audio/background-audio.md](https://docs.livekit.io/agents/multimodality/audio/background-audio.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-8"></a>
## Page 8: agents/multimodality/audio/wakeword/
**Original URL:** https://docs.livekit.io/agents/multimodality/audio/wakeword/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/audio/wakeword.md

LiveKit docs › Build Agents › Multimodality › Speech & audio › Wakeword detection

---

# Wakeword detection

> Detect a spoken trigger phrase on the client to activate a voice AI agent hands-free.

## Overview

A wakeword is a short spoken phrase, like "Hey Siri," that activates a voice-enabled device or agent. Running detection on the client lets your agent stay idle until the user speaks the trigger phrase. This is a common pattern for hands-free interfaces, edge devices like the Raspberry Pi, and branded activation phrases.

The [livekit-wakeword](https://github.com/livekit/livekit-wakeword) library is an open-source toolkit that includes:

- A pre-trained `hey livekit` classifier you can use out of the box.
- A training pipeline for creating custom wakeword classifiers.
- Three client SDKs (Python, Rust, Swift) for running detection on a device.

Models export as standard ONNX files and are compatible with [openWakeWord](https://github.com/dscripka/openWakeWord). For benchmarks and architecture details, see the [LiveKit blog post](https://livekit.com/blog/livekit-wakeword).

### How it works

Detection runs on the client device, not on the agent server. A typical setup pairs an on-device client with a standard LiveKit Agents server. At runtime:

1. The client listens to the microphone locally and scores each audio frame against the trained classifier.
2. When a score crosses the threshold, the client connects to a LiveKit room.
3. The agent joins the room.
4. When the user finishes, the agent leaves the room.
5. The client disconnects and resumes listening for the wakeword.

The SDK you select on the client is independent of the agent server. Any client SDK can connect to a Python or Node.js LiveKit Agents server.

### Try the example

The [hello-wakeword](https://github.com/livekit-examples/hello-wakeword) example pairs a Python client (using the pre-trained `hey livekit` model) with a LiveKit Agents server. It's the fastest way to see end-to-end detection.

The agent uses [LiveKit Inference](https://docs.livekit.io/agents/models/inference.md) for STT, LLM, and TTS, so no separate provider keys are required.

This example assumes you have:

- A [LiveKit Cloud](https://cloud.livekit.io/) account
- [uv](https://docs.astral.sh/uv/) installed

1. Clone the repo and install both packages:

```shell
git clone https://github.com/livekit-examples/hello-wakeword
cd hello-wakeword
uv sync --all-packages

```
2. Authenticate with LiveKit Cloud and generate a `.env.local` file:

```shell
lk cloud auth
lk app env -w

```
3. Start the agent server in one terminal:

```shell
lk agent dev wakeword-agent

```
4. Start the client in another terminal:

```shell
uv run wakeword-client

```
5. Say `hey livekit` to trigger the agent. Stop speaking to end the session, and the client resumes listening automatically.

## Set up wakeword detection

To run wakeword detection on a device, you need an ONNX classifier file and a client SDK to score audio against it. Either classifier (pre-trained or custom-trained) works with any of the three SDKs.

### Use the pre-trained model

Download the pre-trained `hey livekit` classifier:

```shell
curl -LO https://raw.githubusercontent.com/livekit-examples/hello-wakeword/main/client/models/hey_livekit.onnx

```

To detect a different phrase or language, [train a custom wakeword](#train-a-custom-wakeword) instead.

### Train a custom wakeword

To detect a different trigger phrase or a non-English language, train a custom classifier. The training pipeline is automated and uses TTS to generate synthetic training samples, so no audio recording or labeled data is required. The result is a single ONNX file that loads in any client SDK.

Train locally, in the cloud, or on GPU instances via [SkyPilot](https://github.com/skypilot-org/skypilot).

#### Pipeline stages

The training pipeline has six stages. The `run` command chains four of them. You can run any stage on its own with `livekit-wakeword <stage> <config>`.

| Stage | What it does |
| `setup` | Download base data (Piper or VoxCPM weights, ACAV features, room impulse responses, MUSAN background noise). |
| `generate` | Synthesize positive samples and adversarial negatives via TTS. |
| `augment` | Add noise, reverb, and pitch shifts. Extract features through the frozen mel and embedding models. |
| `train` | Train the classifier head on the extracted features. |
| `export` | Export the trained classifier to ONNX. |
| `eval` | Score the exported model against the validation set. Produces a DET curve plot and a metrics JSON file. |

#### Train via the CLI

1. Install the system dependencies: `espeak-ng`, `ffmpeg`, `sox`, `libsndfile`, and `portaudio`.

**macOS**:

```shell
brew install espeak-ng ffmpeg sox portaudio

```

---

**Ubuntu/Debian**:

```shell
sudo apt install espeak-ng ffmpeg sox libsndfile1 portaudio19-dev

```

---

**Windows**:

```powershell
winget install eSpeak-NG.eSpeak-NG
winget install Gyan.FFmpeg
winget install ChrisBagwell.SoX

```

`libsndfile` and `portaudio` are bundled with the `soundfile` and `pyaudio` Python wheels on Windows, so you don't need to install them separately.
2. Install the CLI:

```shell
pip install "livekit-wakeword[train,eval,export]"

```
3. Write a config file. A minimum config looks like this:

```yaml
# hey_robot.yaml
model_name: hey_robot
target_phrases:
  - "hey robot"

n_samples: 10000
model:
  model_type: conv_attention  # conv_attention (default), dnn, or rnn
  model_size: small           # tiny, small, medium, large
steps: 50000
target_fp_per_hour: 0.2

```
4. Download the base data:

```shell
livekit-wakeword setup --config hey_robot.yaml

```
5. Run the training pipeline:

```shell
livekit-wakeword run hey_robot.yaml

```
6. (Optional) Evaluate the model against the validation set:

```shell
livekit-wakeword eval hey_robot.yaml

```

You can evaluate any compatible ONNX model using `livekit-wakeword eval` by passing `-m /path/to/other_model.onnx`.

#### Train via the Python API

Drive the same pipeline from code when you need to integrate training into a larger system or automate model iteration:

```python
from livekit.wakeword import (
    WakeWordConfig,
    load_config,
    run_generate,
    run_augment,
    run_extraction,
    run_train,
    run_export,
    run_eval,
)

# Load from YAML
config = load_config("hey_robot.yaml")

# Or build a config programmatically
config = WakeWordConfig(
    model_name="hey_robot",
    target_phrases=["hey robot"],
    n_samples=5000,
    steps=30000,
)

run_generate(config)
run_augment(config)
run_extraction(config)
run_train(config)
onnx_path = run_export(config)

results = run_eval(config, onnx_path)
print(results)

```

#### Multilingual support

By default, training generates English samples with [Piper TTS](https://github.com/rhasspy/piper). To train in a different language, switch the TTS backend to [VoxCPM](https://github.com/OpenBMB/VoxCPM), which supports 30 languages.

1. Install the `voxcpm` extra alongside the training extras:

```shell
pip install "livekit-wakeword[train,eval,export,voxcpm]"

```
2. Set the backend in your config:

```yaml
# ni_hao_livekit.yaml
model_name: ni_hao_livekit
target_phrases:
  - "你好 livekit"
tts_backend: voxcpm

```

> 🔥 **Caution**
> 
> Multilingual accuracy is currently lower than English. To improve results, increase `voice_design_prompts` (50 to 100) and `n_samples` in your config.

### Select a client SDK

The library provides three client SDKs. Select the one that fits the platform you're targeting:

- **Python**: for Linux, macOS, or Windows clients. Includes a built-in microphone listener.
- **Rust**: for native or embedded clients. Inference only.
- **Swift**: for iOS 16+ and macOS 14+ apps. Includes a built-in microphone listener with CoreML acceleration.

Each tab below shows install + load + use steps for that SDK. Any SDK works with either classifier.

**Python**:

1. Install the library from PyPI. Add the `listener` extra to use the built-in microphone listener, which depends on PortAudio:

```shell
# macOS
brew install portaudio

# Ubuntu/Debian
sudo apt install portaudio19-dev

```

```shell
pip install "livekit-wakeword[listener]"

```

Python 3.11 or later is required. Runtime dependencies are `numpy` and `onnxruntime`.
2. Load a model and score audio frames:

```python
from livekit.wakeword import WakeWordModel

model = WakeWordModel(models=["hey_livekit.onnx"])

# Feed audio frames (16 kHz, int16 or float32)
scores = model.predict(audio_frame)
if scores["hey_livekit"] > 0.5:
    print("Wakeword detected!")

```
3. (Alternative) For hands-free use, wrap the model with `WakeWordListener`. `wait_for_detection` blocks until a score crosses the threshold:

```python
import asyncio
from livekit.wakeword import WakeWordModel, WakeWordListener

model = WakeWordModel(models=["hey_livekit.onnx"])

async def main():
    async with WakeWordListener(model, threshold=0.5, debounce=2.0) as listener:
        while True:
            detection = await listener.wait_for_detection()
            print(f"Detected {detection.name} ({detection.confidence:.2f})")

asyncio.run(main())

```

`threshold` is the minimum score (0 to 1) to count as a detection. Lower values are more sensitive but produce more false positives. `debounce` is the minimum interval, in seconds, between consecutive detections.

For a complete Python example wired up to a LiveKit Agents server, see [hello-wakeword](https://github.com/livekit-examples/hello-wakeword).

---

**Rust**:

The Rust crate is inference only, meaning it only handles wakeword detection. You need to manage audio capture yourself. Use your preferred audio library (such as [`cpal`](https://github.com/RustAudio/cpal)) to capture microphone audio and pass `i16` PCM frames to `predict()`.

1. Add the [livekit-wakeword](https://crates.io/crates/livekit-wakeword) crate to your project:

```shell
cargo add livekit-wakeword

```
2. Load a model and score `i16` PCM audio chunks at the configured sample rate:

```rust
use livekit_wakeword::WakeWordModel;

let mut model = WakeWordModel::new(&["hey_livekit.onnx"], 16000)?;

let scores = model.predict(&audio_chunk)?;
if scores["hey_livekit"] > 0.5 {
    println!("Wakeword detected!");
}

```

Input audio at sample rates between 16 kHz and 384 kHz is automatically resampled to 16 kHz. The mel spectrogram and embedding models are compiled into the binary, so only the classifier ONNX file is loaded at runtime. The crate uses a pure-Rust ONNX backend by default and falls back to the native ONNX Runtime on aarch64 Windows.

---

**Swift**:

1. Add the [`LiveKitWakeWord`](https://github.com/livekit/livekit-wakeword/tree/main/swift) package to your `Package.swift`:

```swift
.package(url: "https://github.com/livekit/livekit-wakeword", branch: "main"),

```
2. Load a model and score `Int16` PCM chunks at the configured sample rate:

```swift
import LiveKitWakeWord

let classifier = Bundle.main.url(forResource: "hey_livekit", withExtension: "onnx")!
let model = try WakeWordModel(models: [classifier], sampleRate: 16_000)

let scores = try model.predict(audioChunk)
if (scores["hey_livekit"] ?? 0) > 0.5 {
    print("Wakeword detected!")
}

```
3. (Alternative) For hands-free use, wrap the model with `WakeWordListener` and consume detections as an async sequence:

```swift
import LiveKitWakeWord

let classifier = Bundle.main.url(forResource: "hey_livekit", withExtension: "onnx")!
let model = try WakeWordModel(models: [classifier], sampleRate: 16_000)
let listener = WakeWordListener(model: model, threshold: 0.5, debounce: 2.0)

try listener.start()
for await detection in listener.detections() {
    print("Detected \(detection.name) (\(String(format: "%.2f", detection.confidence)))")
}

```

`threshold` is the minimum score (0 to 1) to count as a detection. `debounce` is the minimum interval, in seconds, between consecutive detections. Add `NSMicrophoneUsageDescription` to your `Info.plist` (and `com.apple.security.device.audio-input` on sandboxed macOS apps) before using the listener.

Audio at any sample rate is resampled to 16 kHz internally via `AVAudioConverter`. ONNX Runtime with the CoreML Execution Provider dispatches to ANE, GPU, or CPU by default.

A SwiftUI demo lives in [`examples/ios_wakeword/`](https://github.com/livekit/livekit-wakeword/tree/main/examples/ios_wakeword).

## Additional resources

The following resources provide more information about LiveKit wakeword detection.

- **[livekit-wakeword](https://github.com/livekit/livekit-wakeword)**: Source for the training toolkit, SDKs, and example apps.

- **[hello-wakeword](https://github.com/livekit-examples/hello-wakeword)**: End-to-end example of a wakeword-triggered voice agent.

- **[Python package](https://pypi.org/project/livekit-wakeword/)**: The `livekit-wakeword` package on PyPI.

- **[Rust crate](https://crates.io/crates/livekit-wakeword)**: The `livekit-wakeword` crate for native clients.

- **[Introducing livekit-wakeword](https://livekit.com/blog/livekit-wakeword)**: Blog post covering model architecture, training pipeline, and benchmarks.

---

This document was rendered at 2026-08-28T04:22:12.965Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/audio/wakeword.md](https://docs.livekit.io/agents/multimodality/audio/wakeword.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-9"></a>
## Page 9: agents/multimodality/vision/images/
**Original URL:** https://docs.livekit.io/agents/multimodality/vision/images/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/vision/images.md

LiveKit docs › Build Agents › Multimodality › Images & video › Images

---

# Images

> Add images to your agent's context, receive images from the frontend, and send images back to users.

## Overview

LiveKit Agents supports images as both input and output. On the input side, you can add images to your agent's chat context, receive images from the frontend, or sample video frames. On the output side, you can send images to the frontend using [byte streams](https://docs.livekit.io/transport/data/byte-streams.md).

## Image input

The agent's [chat context](https://docs.livekit.io/agents/logic/chat-context.md) supports images as well as text. You can add as many images as you want to the chat context, but keep in mind that larger context windows contribute to slow response times.

To add an image to the chat context, create an `ImageContent` object and include it in a chat message. The image content can be a base64 data URL, an external URL, or a frame from a [video track](https://docs.livekit.io/transport/media.md).

### Load into initial context

The following example shows an agent initialized with an image at startup. This example uses an external URL, but you can modify it to load a local file using a base64 data URL instead:

** Filename: `agent.py`**

```python
def entrypoint(ctx: JobContext):
    # ctx.connect, etc.

    session = AgentSession(
        # ... stt, tts, llm, etc.
    )

    initial_ctx = ChatContext()
    initial_ctx.add_message(
        role="user",
        content=[
            "Here is a picture of me",
            ImageContent(image="https://example.com/image.jpg")
        ],
    )

    await session.start(
        room=ctx.room,
        agent=Agent(chat_ctx=initial_ctx,),
        # ... room_options, etc.
    )

```

** Filename: `Required imports`**

```python
from livekit.agents.llm import ImageContent
from livekit.agents import Agent, AgentSession, ChatContext, JobContext

```

** Filename: `agent.ts`**

```typescript
export default defineAgent({
  entry: async (ctx: JobContext) => {
    // await ctx.connect(), etc

    const initialCtx = llm.ChatContext.empty();

    initialCtx.addMessage({
      role: 'user',
      content: [
        'Here is a picture of me',
        llm.createImageContent({
          image: 'https://example.com/image.jpg',
        }),
      ],
    });

    const agent = voice.Agent.create({
      instructions: 'You are a helpful voice AI assistant.',
      chatCtx: initialCtx,
    });

    const session = new voice.AgentSession({
      // ... stt, tts, llm, etc.
    });

    await session.start({
      room: ctx.room,
      agent,
      // ... inputOptions, etc.
    });
  },
});

```

** Filename: `Required imports`**

```typescript
import { type JobContext, defineAgent, llm, voice } from '@livekit/agents';

```

> 🔥 **LLM provider support for external URLs**
> 
> Not every provider supports external image URLs. Consult their documentation for details.

### Upload from frontend

To upload an image from your frontend app, use the [sendFile method](https://docs.livekit.io/transport/data/byte-streams.md#sending-files) of the LiveKit SDK. Add a byte stream handler to your agent to receive the image data and add it to the chat context. Here is a simple agent capable of receiving images from the user on the byte stream topic `"images"`:

** Filename: `agent.py`**

```python
class Assistant(Agent):
    def __init__(self) -> None:
        self._tasks = [] # Prevent garbage collection of running tasks
        super().__init__(instructions="You are a helpful voice AI assistant.")

    async def on_enter(self):
        def _image_received_handler(reader, participant_identity):
            task = asyncio.create_task(
                self._image_received(reader, participant_identity)
            )
            self._tasks.append(task)
            task.add_done_callback(lambda t: self._tasks.remove(t))

        # Add the handler when the agent joins
        get_job_context().room.register_byte_stream_handler("images", _image_received_handler)

    async def _image_received(self, reader, participant_identity):
        image_bytes = bytes()
        async for chunk in reader:
            image_bytes += chunk

        chat_ctx = self.chat_ctx.copy()

        # Encode the image to base64 and add it to the chat context
        chat_ctx.add_message(
            role="user",
            content=[
                ImageContent(
                    image=f"data:image/png;base64,{base64.b64encode(image_bytes).decode('utf-8')}"
                )
            ],
        )
        await self.update_chat_ctx(chat_ctx)

```

** Filename: `Required imports`**

```python
import asyncio
import base64
from livekit.agents import Agent, get_job_context
from livekit.agents.llm import ImageContent

```

** Filename: `agent.ts`**

```typescript
function createAssistant() {
  const tasks: Set<Task<void>> = new Set(); // Prevent garbage collection of running tasks
  const agent = voice.Agent.create({
    instructions: 'You are a helpful voice AI assistant.',
    onEnter() {
      // Register byte stream handler for receiving images
      getJobContext().room.registerByteStreamHandler('images', async (stream: ByteStreamReader) => {
        const task = Task.from((controller) => imageReceived(stream, controller));
        tasks.add(task);

        task.result.finally(() => {
          tasks.delete(task);
        });
      });
    },
  });

  async function imageReceived(
    stream: ByteStreamReader,
    controller: AbortController,
  ): Promise<void> {
    const chunks: Uint8Array[] = [];

    // Read all chunks from the stream
    for await (const chunk of stream) {
      if (controller.signal.aborted) return;
      chunks.push(chunk);
    }

    // Combine all chunks into a single buffer
    const totalLength = chunks.reduce((sum, chunk) => sum + chunk.length, 0);
    const imageBytes = new Uint8Array(totalLength);
    let offset = 0;

    for (const chunk of chunks) {
      imageBytes.set(chunk, offset);
      offset += chunk.length;
    }

    const chatCtx = agent.chatCtx.copy();

    // Encode the image to base64 and add it to the chat context
    const imageContent = llm.createImageContent({
      image: `data:image/png;base64,${Buffer.from(imageBytes).toString('base64')}`,
      inferenceDetail: 'auto',
    });

    chatCtx.addMessage({
      role: 'user',
      content: [imageContent],
    });

    if (controller.signal.aborted) return;
    await agent.updateChatCtx(chatCtx);
  }

  return agent;
}

```

** Filename: `Required imports`**

```typescript
import { Task, getJobContext, llm, voice } from '@livekit/agents';
import type { ByteStreamReader } from '@livekit/rtc-node';

```

### Inference detail

If your LLM provider supports it, you can set the `inference_detail` parameter to `"high"` or `"low"` to control the token usage and inference quality applied. The default is `"auto"`, which uses the provider's default.

## Image output

Your agent can send images to the frontend using [byte streams](https://docs.livekit.io/transport/data/byte-streams.md). Use this to share generated images, diagrams, screenshots, or any other visual content from your agent to the user.

To send an image, use the `send_file` method on the room's local participant. The frontend receives the image by registering a byte stream handler for the same topic.

### Send an image from your agent

** Filename: `agent.py`**

```python
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant.")

    async def on_enter(self):
        room = get_job_context().room

        # Send an image file to the frontend
        await room.local_participant.send_file(
            file_path="path/to/image.png",
            topic="agent-images",
        )

```

** Filename: `Required imports`**

```python
from livekit.agents import Agent, get_job_context

```

** Filename: `agent.ts`**

```typescript
const assistant = voice.Agent.create({
  instructions: 'You are a helpful voice AI assistant.',
  async onEnter() {
    const room = getJobContext().room;

    // Send an image file to the frontend
    await room.localParticipant!.sendFile('path/to/image.png', {
      topic: 'agent-images',
    });
  },
});

```

** Filename: `Required imports`**

```typescript
import { getJobContext, voice } from '@livekit/agents';

```

### Receive images in your frontend

Register a byte stream handler in your frontend to receive images from the agent:

**JavaScript**:

```typescript
room.registerByteStreamHandler('agent-images', async (reader, participantInfo) => {
  const data = await reader.readAll();
  const blob = new Blob(data, { type: reader.info.mimeType });
  const url = URL.createObjectURL(blob);

  // Display the image in your UI
  const img = document.createElement('img');
  img.src = url;
  document.body.appendChild(img);
});

```

---

**Swift**:

```swift
try await room.registerByteStreamHandler(for: "agent-images") { reader, participantIdentity in
    let data = try await reader.readAll()

    // Display the image in your UI
    DispatchQueue.main.async {
        let image = UIImage(data: data)
        let imageView = UIImageView(image: image)
        self.view.addSubview(imageView)
    }
}

```

---

**Android**:

```kotlin
room.registerByteStreamHandler("agent-images") { reader, participantIdentity ->
    myCoroutineScope.launch {
        val chunks = reader.readAll()
        val bytes = chunks.fold(ByteArray(0)) { acc, chunk -> acc + chunk }

        // Display the image in your UI
        withContext(Dispatchers.Main) {
            val bitmap = BitmapFactory.decodeByteArray(bytes, 0, bytes.size)
            imageView.setImageBitmap(bitmap)
        }
    }
}

```

---

**Flutter**:

```dart
room.registerByteStreamHandler('agent-images',
    (ByteStreamReader reader, String participantIdentity) async {
  final chunks = await reader.readAll();
  final bytes = chunks.expand((chunk) => chunk).toList();

  // Display the image in your UI
  setState(() {
    imageBytes = Uint8List.fromList(bytes);
  });
});

```

For full details on byte streams, see [Sending files & bytes](https://docs.livekit.io/transport/data/byte-streams.md).

---

This document was rendered at 2026-08-28T04:22:12.965Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/vision/images.md](https://docs.livekit.io/agents/multimodality/vision/images.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-10"></a>
## Page 10: agents/multimodality/vision/video/
**Original URL:** https://docs.livekit.io/agents/multimodality/vision/video/  
**Source MD URL:** https://docs.livekit.io/agents/multimodality/vision/video.md

LiveKit docs › Build Agents › Multimodality › Images & video › Video

---

# Video

> Sample video frames, enable live video input, and add virtual avatars for video output.

## Overview

LiveKit Agents supports video as both input and output. On the input side, you can sample video frames from an STT-LLM-TTS pipeline or enable live video input with a supported realtime model. On the output side, you can add a virtual avatar for lifelike video output.

## Sample video frames

LLMs can process video in the form of still images, but many LLMs are not trained for this use case and can produce suboptimal results in understanding motion and other changes through a video feed. Realtime models, like [Gemini Live](https://docs.livekit.io/agents/models/realtime/plugins/gemini.md), are trained on video and you can enable [live video input](#live-video-input) for automatic support.

If you're using an STT-LLM-TTS pipeline, you can still work with video by sampling frames at suitable times. In the following example, the agent includes the latest video frame for each user turn by injecting it into the [chat context](https://docs.livekit.io/agents/logic/chat-context.md), providing additional context without overwhelming the model or requiring it to process multiple sequential frames.

** Filename: `agent.py`**

```python
class Assistant(Agent):
    def __init__(self) -> None:
        self._latest_frame = None
        self._video_stream = None
        self._tasks = []
        super().__init__(instructions="You are a helpful voice AI assistant.")

    async def on_enter(self):
        room = get_job_context().room

        # Find the first video track (if any) from the remote participant
        if room.remote_participants:
            remote_participant = list(room.remote_participants.values())[0]
            video_tracks = [publication.track for publication in list(remote_participant.track_publications.values()) if publication.track and publication.track.kind == rtc.TrackKind.KIND_VIDEO]
            if video_tracks:
                self._create_video_stream(video_tracks[0])

        # Watch for new video tracks not yet published
        @room.on("track_subscribed")
        def on_track_subscribed(track: rtc.Track, publication: rtc.RemoteTrackPublication, participant: rtc.RemoteParticipant):
            if track.kind == rtc.TrackKind.KIND_VIDEO:
                self._create_video_stream(track)

    async def on_user_turn_completed(self, turn_ctx: ChatContext, new_message: ChatMessage) -> None:
        # Add the latest video frame, if any, to the new message
        if self._latest_frame:
            new_message.content.append(ImageContent(image=self._latest_frame))
            self._latest_frame = None

    # Helper method to buffer the latest video frame from the user's track
    def _create_video_stream(self, track: rtc.Track):
        # Close any existing stream (we only want one at a time)
        if self._video_stream is not None:
            old = self._video_stream
            self._video_stream = None
            asyncio.create_task(old.aclose())

        # Create a new stream to receive frames
        self._video_stream = rtc.VideoStream(track)
        async def read_stream():
            async for event in self._video_stream:
                # Store the latest frame for use later
                self._latest_frame = event.frame

        # Store the async task
        task = asyncio.create_task(read_stream())
        task.add_done_callback(lambda t: self._tasks.remove(t))
        self._tasks.append(task)

```

** Filename: `Required imports`**

```python
import asyncio
from livekit import rtc
from livekit.agents import Agent, get_job_context, ChatContext, ChatMessage
from livekit.agents.llm import ImageContent

```

** Filename: `agent.ts`**

```typescript
function createAssistant() {
  let latestFrame: VideoFrame | null = null;
  let videoStream: VideoStream | null = null;
  const tasks: Set<Task<void>> = new Set();

  const createVideoStream = (track: Track): void => {
    // Close any existing stream (we only want one at a time)
    if (videoStream !== null) {
      videoStream.cancel();
    }

    // Create a new stream to receive frames
    videoStream = new VideoStream(track);

    const readStream = async (controller: AbortController): Promise<void> => {
      if (!videoStream) return;

      for await (const event of videoStream) {
        if (controller.signal.aborted) return;
        // Store the latest frame for use later
        latestFrame = event.frame;
      }
    };

    // Store the async task
    const task = Task.from((controller) => readStream(controller));
    task.result.finally(() => tasks.delete(task));
    tasks.add(task);
  };

  return voice.Agent.create({
    instructions: 'You are a helpful voice AI assistant.',
    onEnter() {
      const room = getJobContext().room;

      // Find the first video track (if any) from the remote participant
      const remoteParticipants = Array.from(room.remoteParticipants.values());

      if (remoteParticipants.length > 0) {
        const remoteParticipant = remoteParticipants[0]!;
        const videoTracks = Array.from(remoteParticipant.trackPublications.values())
          .filter((pub) => pub.track?.kind === TrackKind.KIND_VIDEO)
          .map((pub) => pub.track!)
          .filter((track) => track !== undefined);

        if (videoTracks.length > 0) {
          createVideoStream(videoTracks[0]!);
        }
      }

      // Watch for new video tracks not yet published
      room.on(RoomEvent.TrackSubscribed, (track: Track) => {
        if (track.kind === TrackKind.KIND_VIDEO) {
          createVideoStream(track);
        }
      });
    },
    onUserTurnCompleted(ctx, chatCtx, newMessage) {
      // Add the latest video frame, if any, to the new message
      if (latestFrame !== null) {
        newMessage.content.push(
          llm.createImageContent({
            image: latestFrame,
          }),
        );
        latestFrame = null;
      }
    },
  });
}

```

** Filename: `Required imports`**

```typescript
import { Task, getJobContext, llm, voice } from '@livekit/agents';
import type { Track, VideoFrame } from '@livekit/rtc-node';
import { RoomEvent, TrackKind, VideoStream } from '@livekit/rtc-node';

```

### Video frame encoding

By default, `ImageContent` encodes video frames as JPEGs at their native size. To adjust the size of the encoded frames, set the `inference_width` and `inference_height` parameters. Each frame is resized to fit within the provided dimensions while maintaining the original aspect ratio. For more control, use the `encode` method of the `livekit.agents.utils.images` module and pass the result as a data URL:

** Filename: `agent.py`**

```python
image_bytes = encode(
    event.frame,
    EncodeOptions(
        format="PNG",
        resize_options=ResizeOptions(
            width=512,
            height=512,
            strategy="scale_aspect_fit"
        )
    )
)
image_content = ImageContent(
    image=f"data:image/png;base64,{base64.b64encode(image_bytes).decode('utf-8')}"
)

```

** Filename: `Required imports`**

```python
import base64
from livekit.agents.utils.images import encode, EncodeOptions, ResizeOptions

```

## Live video input

Available in:
- [ ] Node.js
- [x] Python

Live video input requires a realtime model with video support. Not all [realtime models](https://docs.livekit.io/agents/models/realtime.md) support video input. The following models support live video:

- [Gemini Live API](https://docs.livekit.io/agents/models/realtime/plugins/gemini.md#video-input)
- [OpenAI Realtime API](https://docs.livekit.io/agents/models/realtime/plugins/openai.md#video-input)

> ℹ️ **Video input with audio-only models**
> 
> Enabling `video_input` with an audio-only realtime model silently ignores the video frames — no error is raised but the model won't process video.

To start receiving video frames, set the `video_input` parameter to `True` in `RoomOptions`. Your agent automatically receives frames from the user's [camera](https://docs.livekit.io/transport/media/publish.md) or [screen sharing](https://docs.livekit.io/transport/media/screenshare.md) tracks, if available. Only the single most recently published video track is used.

By default, the agent samples one frame per second while the user speaks and one frame every three seconds otherwise. Each frame is resized to 1024x1024 and encoded to JPEG. To override the frame rate, set `video_sampler` on the `AgentSession` with a custom instance.

Video input is passive and has no effect on [turn detection](https://docs.livekit.io/agents/logic/turns.md). To leverage live video input in a non-conversational context, use [manual turn control](https://docs.livekit.io/agents/logic/turns.md#manual) and trigger LLM responses or tool calls on a timer or other schedule.

### Considerations

Both models consume tokens for each video frame, so higher frame rates increase cost. The two supported models handle video frames differently:

- **Gemini Live** streams video frames natively within its realtime protocol. Frames are encoded and sent inline alongside the audio session. Each frame is tokenized based on its dimensions. See [Gemini token counting](https://ai.google.dev/gemini-api/docs/tokens) for details.
- **OpenAI Realtime API** sends each video frame as an image message in the conversation context. Each frame consumes input tokens and counts against the context window. See [OpenAI image token calculation](https://developers.openai.com/docs/guides/images-vision#calculating-costs) for details.

### Examples

- **[Gemini Live video input](https://docs.livekit.io/agents/models/realtime/plugins/gemini.md#video-input)**: Use live video input with Gemini Live.

- **[OpenAI Realtime video input](https://docs.livekit.io/agents/models/realtime/plugins/openai.md#video-input)**: Enable video input with OpenAI Realtime API.

## Video output

Virtual avatars add lifelike video output for your voice AI agents. An avatar provider joins the LiveKit room as a secondary participant and publishes synchronized audio and video tracks, giving your agent a visual presence.

The `AgentSession` sends its audio output to the avatar worker instead of directly to the room. The avatar worker uses this audio to generate synchronized lip movements and gestures, then publishes the resulting audio and video tracks to the room.

### Adding an avatar to your agent

To add a virtual avatar:

1. Install the avatar plugin and set up API keys for your chosen provider.
2. Create an `AgentSession` as in the [voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md).
3. Create an `AvatarSession` and configure it as necessary.
4. Start the avatar session, passing in the `AgentSession` instance.

The following example uses [Anam](https://docs.livekit.io/agents/models/avatar/plugins/anam.md):

** Filename: `agent.py`**

```python
server = AgentServer()

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: agents.JobContext):
   session = AgentSession(
      # ... stt, llm, tts, etc.
   )

   avatar = anam.AvatarSession(
      persona_config=anam.PersonaConfig(
         name="...",  # Name of the avatar to use.
         avatarId="...",  # ID of the avatar to use.
      ),
   )

   # Start the avatar and wait for it to join
   await avatar.start(session, room=ctx.room)

   # Start your agent session with the user
   await session.start(
      # ... room, agent, room_options, etc....
   )

```

** Filename: `Required imports`**

```python
from livekit import agents
from livekit.agents import AgentServer, AgentSession
from livekit.plugins import anam

```

** Filename: `agent.ts`**

```typescript
export default defineAgent({
  entry: async (ctx: JobContext) => {
    await ctx.connect();

    const agent = voice.Agent.create({
      instructions: 'You are a helpful assistant.',
    });

    const session = new voice.AgentSession({
      // ... llm, stt, tts, etc.
    });

    await session.start({
      agent,
      room: ctx.room,
    });

    const avatar = new bey.AvatarSession({
      avatarId: '...', // ID of the avatar to use
    });
    await avatar.start(session, ctx.room);
  },
});

```

** Filename: `Required imports`**

```typescript
import { type JobContext, defineAgent, voice } from '@livekit/agents';
import * as bey from '@livekit/agents-plugin-bey';

```

### Frontend integration

In your frontend, distinguish between the agent (your Python or Node.js program) and the avatar worker. You can identify an avatar worker as an `agent` participant with the attribute `lk.publish_on_behalf`:

**JavaScript**:

In React apps, use the [useVoiceAssistant hook](https://docs.livekit.io/reference/components/react/hook/usevoiceassistant.md) to get the correct audio and video tracks automatically:

```typescript
const {
  agent, // The agent participant
  audioTrack, // the worker's audio track
  videoTrack, // the worker's video track
} = useVoiceAssistant();

```

With the lower-level SDK, find participants by kind and attribute:

```typescript
const participants = Array.from(room.remoteParticipants.values());
const agent = participants.find(
  p => p.kind === ParticipantKind.AGENT && !p.attributes['lk.publish_on_behalf']
);
const avatarWorker = participants.find(
  p => p.kind === ParticipantKind.AGENT && p.attributes['lk.publish_on_behalf'] === agent?.identity
);

```

---

**Swift**:

```swift
let agent = room.remoteParticipants.values.first {
    $0.kind == .agent && $0.attributes["lk.publish_on_behalf"] == nil
}
let avatarWorker = room.remoteParticipants.values.first {
    $0.kind == .agent && $0.attributes["lk.publish_on_behalf"] == agent?.identity?.stringValue
}

```

---

**Android**:

```kotlin
val agent = room.remoteParticipants.values.firstOrNull {
    it.kind == Participant.Kind.AGENT &&
        it.agentAttributes.lkPublishOnBehalf == null
}
val avatarWorker = room.remoteParticipants.values.firstOrNull {
    it.kind == Participant.Kind.AGENT &&
        it.agentAttributes.lkPublishOnBehalf == agent?.identity?.value
}

```

---

**Flutter**:

```dart
final agent = room.remoteParticipants.values.firstWhereOrNull(
  (p) => p.kind == ParticipantKind.AGENT &&
      (p.attributes['lk.publish_on_behalf'] == null ||
       p.attributes['lk.publish_on_behalf']!.isEmpty),
);
final avatarWorker = room.remoteParticipants.values.firstWhereOrNull(
  (p) => p.kind == ParticipantKind.AGENT &&
      p.attributes['lk.publish_on_behalf'] == agent?.identity,
);

```

For more details on building frontends with avatars, see [Virtual avatars](https://docs.livekit.io/frontends/build/virtual-avatars.md) in the frontends section. For step-by-step setup guides for each avatar provider, see [Virtual avatar models](https://docs.livekit.io/agents/models/avatar.md).

---

This document was rendered at 2026-08-28T04:22:12.960Z.
For the latest version of this document, see [https://docs.livekit.io/agents/multimodality/vision/video.md](https://docs.livekit.io/agents/multimodality/vision/video.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

