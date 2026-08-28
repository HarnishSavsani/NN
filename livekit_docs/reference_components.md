# Reference: UI Components

Detailed components and custom hooks reference for React and Android Compose UI.

- **Total pages in this section**: 156
- **Successful retrieves**: 155
- **API References / Placeholders**: 1

## Table of Contents

1. [reference/components/agents-ui/](#page-1) (✓)
2. [reference/components/android](#page-2) (✓)
3. [reference/components/react](#page-3) (✗)
4. [reference/components/android/samples](#page-4) (✓)
5. [reference/components/react/installation](#page-5) (✓)
6. [reference/components/react/guide](#page-6) (✓)
7. [reference/components/agents-ui/block/agent-session-view-01](#page-7) (✓)
8. [reference/components/agents-ui/component/agent-control-bar](#page-8) (✓)
9. [reference/components/agents-ui/component/agent-track-control](#page-9) (✓)
10. [reference/components/agents-ui/component/agent-track-toggle](#page-10) (✓)
11. [reference/components/agents-ui/component/agent-audio-visualizer-bar](#page-11) (✓)
12. [reference/components/agents-ui/component/agent-audio-visualizer-grid](#page-12) (✓)
13. [reference/components/agents-ui/component/agent-audio-visualizer-radial](#page-13) (✓)
14. [reference/components/agents-ui/component/agent-audio-visualizer-wave](#page-14) (✓)
15. [reference/components/agents-ui/component/agent-audio-visualizer-aura](#page-15) (✓)
16. [reference/components/agents-ui/component/agent-session-provider](#page-16) (✓)
17. [reference/components/agents-ui/component/agent-disconnect-button](#page-17) (✓)
18. [reference/components/agents-ui/component/start-audio-button](#page-18) (✓)
19. [reference/components/agents-ui/component/agent-chat-indicator](#page-19) (✓)
20. [reference/components/agents-ui/component/agent-chat-transcript](#page-20) (✓)
21. [reference/components/agents-ui/component/nextjs-api-token-route](#page-21) (✓)
22. [reference/components/agents-ui/component/react-shader-toy](#page-22) (✓)
23. [reference/components/android/concepts/building-blocks](#page-23) (✓)
24. [reference/components/android/concepts/rendering-a-track](#page-24) (✓)
25. [reference/components/android/concepts/roomscope](#page-25) (✓)
26. [reference/components/android/concepts/scopes](#page-26) (✓)
27. [reference/components/react/concepts/building-blocks](#page-27) (✓)
28. [reference/components/react/concepts/livekit-room-component](#page-28) (✓)
29. [reference/components/react/concepts/contexts](#page-29) (✓)
30. [reference/components/react/concepts/loops](#page-30) (✓)
31. [reference/components/react/concepts/custom-components](#page-31) (✓)
32. [reference/components/react/concepts/style-components](#page-32) (✓)
33. [reference/components/react/concepts/rendering-video](#page-33) (✓)
34. [reference/components/react/concepts/rendering-audio](#page-34) (✓)
35. [reference/components/react/hook/useagent](#page-35) (✓)
36. [reference/components/react/hook/useagentexpression](#page-36) (✓)
37. [reference/components/react/hook/useaudioplayback](#page-37) (✓)
38. [reference/components/react/hook/useaudiowaveform](#page-38) (✓)
39. [reference/components/react/hook/usechat](#page-39) (✓)
40. [reference/components/react/hook/usechattoggle](#page-40) (✓)
41. [reference/components/react/hook/useclearpinbutton](#page-41) (✓)
42. [reference/components/react/hook/useconnectionqualityindicator](#page-42) (✓)
43. [reference/components/react/hook/useconnectionstate](#page-43) (✓)
44. [reference/components/react/hook/usecreatelayoutcontext](#page-44) (✓)
45. [reference/components/react/hook/usedatachannel](#page-45) (✓)
46. [reference/components/react/hook/usedisconnectbutton](#page-46) (✓)
47. [reference/components/react/hook/useensurecreatelayoutcontext](#page-47) (✓)
48. [reference/components/react/hook/useensurelayoutcontext](#page-48) (✓)
49. [reference/components/react/hook/useensureparticipant](#page-49) (✓)
50. [reference/components/react/hook/useensureroom](#page-50) (✓)
51. [reference/components/react/hook/useensuresession](#page-51) (✓)
52. [reference/components/react/hook/useensuretrackref](#page-52) (✓)
53. [reference/components/react/hook/useevents](#page-53) (✓)
54. [reference/components/react/hook/usefacingmode](#page-54) (✓)
55. [reference/components/react/hook/usefocustoggle](#page-55) (✓)
56. [reference/components/react/hook/usegridlayout](#page-56) (✓)
57. [reference/components/react/hook/useisencrypted](#page-57) (✓)
58. [reference/components/react/hook/useismuted](#page-58) (✓)
59. [reference/components/react/hook/useisrecording](#page-59) (✓)
60. [reference/components/react/hook/useisspeaking](#page-60) (✓)
61. [reference/components/react/hook/usekrispnoisefilter](#page-61) (✓)
62. [reference/components/react/hook/uselayoutcontext](#page-62) (✓)
63. [reference/components/react/hook/uselivekitroom](#page-63) (✓)
64. [reference/components/react/hook/uselocalparticipant](#page-64) (✓)
65. [reference/components/react/hook/uselocalparticipantpermissions](#page-65) (✓)
66. [reference/components/react/hook/usemaybelayoutcontext](#page-66) (✓)
67. [reference/components/react/hook/usemaybeparticipantcontext](#page-67) (✓)
68. [reference/components/react/hook/usemayberoomcontext](#page-68) (✓)
69. [reference/components/react/hook/usemaybesessioncontext](#page-69) (✓)
70. [reference/components/react/hook/usemaybetrackrefcontext](#page-70) (✓)
71. [reference/components/react/hook/usemediadevices](#page-71) (✓)
72. [reference/components/react/hook/usemediadeviceselect](#page-72) (✓)
73. [reference/components/react/hook/usemultibandtrackvolume](#page-73) (✓)
74. [reference/components/react/hook/usepagination](#page-74) (✓)
75. [reference/components/react/hook/useparticipantattribute](#page-75) (✓)
76. [reference/components/react/hook/useparticipantattributes](#page-76) (✓)
77. [reference/components/react/hook/useparticipantcontext](#page-77) (✓)
78. [reference/components/react/hook/useparticipantinfo](#page-78) (✓)
79. [reference/components/react/hook/useparticipantpermissions](#page-79) (✓)
80. [reference/components/react/hook/useparticipants](#page-80) (✓)
81. [reference/components/react/hook/useparticipanttile](#page-81) (✓)
82. [reference/components/react/hook/useparticipanttracks](#page-82) (✓)
83. [reference/components/react/hook/usepersistentuserchoices](#page-83) (✓)
84. [reference/components/react/hook/usepinnedtracks](#page-84) (✓)
85. [reference/components/react/hook/usepreviewdevice](#page-85) (✓)
86. [reference/components/react/hook/usepreviewtracks](#page-86) (✓)
87. [reference/components/react/hook/useremoteparticipant](#page-87) (✓)
88. [reference/components/react/hook/useremoteparticipants](#page-88) (✓)
89. [reference/components/react/hook/useroomcontext](#page-89) (✓)
90. [reference/components/react/hook/useroominfo](#page-90) (✓)
91. [reference/components/react/hook/userpc](#page-91) (✓)
92. [reference/components/react/hook/usesequentialroomconnectdisconnect](#page-92) (✓)
93. [reference/components/react/hook/usesession](#page-93) (✓)
94. [reference/components/react/hook/usesessioncontext](#page-94) (✓)
95. [reference/components/react/hook/usesessionmessages](#page-95) (✓)
96. [reference/components/react/hook/usesortedparticipants](#page-96) (✓)
97. [reference/components/react/hook/usespeakingparticipants](#page-97) (✓)
98. [reference/components/react/hook/usestartaudio](#page-98) (✓)
99. [reference/components/react/hook/usestartvideo](#page-99) (✓)
100. [reference/components/react/hook/useswipe](#page-100) (✓)
101. [reference/components/react/hook/usetextstream](#page-101) (✓)
102. [reference/components/react/hook/usetoken](#page-102) (✓)
103. [reference/components/react/hook/usetrackbyname](#page-103) (✓)
104. [reference/components/react/hook/usetrackmutedindicator](#page-104) (✓)
105. [reference/components/react/hook/usetrackrefcontext](#page-105) (✓)
106. [reference/components/react/hook/usetracks](#page-106) (✓)
107. [reference/components/react/hook/usetracktoggle](#page-107) (✓)
108. [reference/components/react/hook/usetracktranscription](#page-108) (✓)
109. [reference/components/react/hook/usetrackvolume](#page-109) (✓)
110. [reference/components/react/hook/usetranscriptions](#page-110) (✓)
111. [reference/components/react/hook/usevisualstableupdate](#page-111) (✓)
112. [reference/components/react/hook/usevoiceassistant](#page-112) (✓)
113. [reference/components/react/component/audioconference](#page-113) (✓)
114. [reference/components/react/component/audiotrack](#page-114) (✓)
115. [reference/components/react/component/audiovisualizer](#page-115) (✓)
116. [reference/components/react/component/barvisualizer](#page-116) (✓)
117. [reference/components/react/component/carousellayout](#page-117) (✓)
118. [reference/components/react/component/chat](#page-118) (✓)
119. [reference/components/react/component/chatentry](#page-119) (✓)
120. [reference/components/react/component/chattoggle](#page-120) (✓)
121. [reference/components/react/component/clearpinbutton](#page-121) (✓)
122. [reference/components/react/component/connectionqualityindicator](#page-122) (✓)
123. [reference/components/react/component/connectionstate](#page-123) (✓)
124. [reference/components/react/component/connectionstatetoast](#page-124) (✓)
125. [reference/components/react/component/controlbar](#page-125) (✓)
126. [reference/components/react/component/disconnectbutton](#page-126) (✓)
127. [reference/components/react/component/focuslayout](#page-127) (✓)
128. [reference/components/react/component/focuslayoutcontainer](#page-128) (✓)
129. [reference/components/react/component/focustoggle](#page-129) (✓)
130. [reference/components/react/component/gridlayout](#page-130) (✓)
131. [reference/components/react/component/layoutcontext](#page-131) (✓)
132. [reference/components/react/component/layoutcontextprovider](#page-132) (✓)
133. [reference/components/react/component/livekitroom](#page-133) (✓)
134. [reference/components/react/component/mediadevicemenu](#page-134) (✓)
135. [reference/components/react/component/mediadeviceselect](#page-135) (✓)
136. [reference/components/react/component/participantaudiotile](#page-136) (✓)
137. [reference/components/react/component/participantcontext](#page-137) (✓)
138. [reference/components/react/component/participantcontextifneeded](#page-138) (✓)
139. [reference/components/react/component/participantloop](#page-139) (✓)
140. [reference/components/react/component/participantname](#page-140) (✓)
141. [reference/components/react/component/participanttile](#page-141) (✓)
142. [reference/components/react/component/prejoin](#page-142) (✓)
143. [reference/components/react/component/roomaudiorenderer](#page-143) (✓)
144. [reference/components/react/component/roomcontext](#page-144) (✓)
145. [reference/components/react/component/roomname](#page-145) (✓)
146. [reference/components/react/component/sessionprovider](#page-146) (✓)
147. [reference/components/react/component/startaudio](#page-147) (✓)
148. [reference/components/react/component/startmediabutton](#page-148) (✓)
149. [reference/components/react/component/toast](#page-149) (✓)
150. [reference/components/react/component/trackloop](#page-150) (✓)
151. [reference/components/react/component/trackmutedindicator](#page-151) (✓)
152. [reference/components/react/component/trackrefcontext](#page-152) (✓)
153. [reference/components/react/component/tracktoggle](#page-153) (✓)
154. [reference/components/react/component/videoconference](#page-154) (✓)
155. [reference/components/react/component/videotrack](#page-155) (✓)
156. [reference/components/react/component/voiceassistantcontrolbar](#page-156) (✓)

---

<a name="page-1"></a>
## Page 1: reference/components/agents-ui/
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui.md

LiveKit docs › Agents UI › Framework › Overview

---

# Agents UI overview

> Agents UI is the fastest way to build multi-modal, agentic experiences on top of LiveKit's platform primitives.

Agents UI is a component library built on top of [shadcn/ui](https://ui.shadcn.com/) and [AI Elements](https://ai-sdk.dev/elements) to accelerate the creation of agentic applications built with LiveKit's real-time platform. It provides pre-built components for controlling IO, managing sessions, rendering transcripts, visualizing audio streams, and more.

- **[Unicorn Studio](https://www.unicorn.studio/)**: The AgentAudioVisualizerAura component was designed in partnership with Unicorn Studio

## Getting started

Learn about prerequisites, installation, and usage of the Agents UI components to build your own agentic frontends with LiveKit.

- **[Agents UI overview](https://docs.livekit.io/frontends/agents-ui.md)**: The fastest way to build web-based, multi-modal, agentic experiences on top of LiveKit's platform primitives

## Components

### Media controls

- [AgentControlBar](https://docs.livekit.io/reference/components/agents-ui/component/agent-control-bar.md)
- [AgentTrackControl](https://docs.livekit.io/reference/components/agents-ui/component/agent-track-control.md)
- [AgentTrackToggle](https://docs.livekit.io/reference/components/agents-ui/component/agent-track-toggle.md)

### Audio visualizers

- [AgentAudioVisualizerBar](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-bar.md)
- [AgentAudioVisualizerGrid](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-grid.md)
- [AgentAudioVisualizerRadial](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-radial.md)
- [AgentAudioVisualizerWave](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-wave.md)
- [AgentAudioVisualizerAura](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-aura.md)

### Session management

- [AgentSessionProvider](https://docs.livekit.io/reference/components/agents-ui/component/agent-session-provider.md)
- [AgentDisconnectButton](https://docs.livekit.io/reference/components/agents-ui/component/agent-disconnect-button.md)
- [StartAudioButton](https://docs.livekit.io/reference/components/agents-ui/component/start-audio-button.md)

### Chat components

- [AgentChatTranscript](https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-transcript.md)
- [AgentChatIndicator](https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-indicator.md)

### Misc components

- [ReactShaderToy](https://docs.livekit.io/reference/components/agents-ui/component/react-shader-toy.md)

## Source code

- **[GitHub repository](https://github.com/livekit/components-js/tree/main/packages/shadcn)**: React source code for the Agents UI Shadcn components.

---

This document was rendered at 2026-08-28T04:22:10.517Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui.md](https://docs.livekit.io/reference/components/agents-ui.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-2"></a>
## Page 2: reference/components/android
**Original URL:** https://docs.livekit.io/reference/components/android  
**Source MD URL:** https://docs.livekit.io/reference/components/android.md

LiveKit docs › Android Components › Getting started › Installation

---

# Android Components

> LiveKit Android Components are the easiest way to build realtime audio/video apps with Jetpack Compose on Android.

## Installation

**Groovy**:

In your app's `build.gradle` file:

```groovy
dependencies {
    implementation "io.livekit:livekit-android-compose-components:<current version>"
}

```

---

**Kotlin**:

In your app's `build.gradle.kts` file:

```kotlin

dependencies {
    implementation("io.livekit:livekit-android-compose-components:<current version>")
}

```

See our [releases page](https://github.com/livekit/components-android/releases) for information on the latest version of the SDK.

You'll also need JitPack as one of your repositories.

**Groovy**:

In your root project's `settings.gradle` file:

```groovy
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()

        maven { url 'https://jitpack.io' }
    }
}

```

---

**Kotlin**:

In your root project's `settings.gradle.kts` file:

```kotlin
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()

        maven { url = URI("https://jitpack.io") }
    }
}

```

---

This document was rendered at 2026-08-28T04:22:10.525Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/android.md](https://docs.livekit.io/reference/components/android.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-3"></a>
## Page 3: reference/components/react
**Original URL:** https://docs.livekit.io/reference/components/react  
**Source MD URL:** https://docs.livekit.io/reference/components/react.md

> [!NOTE]
> API Reference or page content could not be fetched as raw markdown.
> View the live content directly at the original URL: [https://docs.livekit.io/reference/components/react](https://docs.livekit.io/reference/components/react).
> Detail: Failed with status code 404


---

<a name="page-4"></a>
## Page 4: reference/components/android/samples
**Original URL:** https://docs.livekit.io/reference/components/android/samples  
**Source MD URL:** https://docs.livekit.io/reference/components/android/samples.md

LiveKit docs › Android Components › Getting started › Samples

---

# Samples

See our sample apps for some examples of usage of the Android Components SDK:

- [Meet Example App](https://github.com/livekit-examples/android-components-meet): A simple teleconferencing app that connects to a LiveKit server.
- [Livestreaming Example App](https://github.com/livekit-examples/android-livestream): A fleshed out livestreaming experience that allows a user to broadcast to viewers as well as let them join the stream as a host.

---

This document was rendered at 2026-08-28T04:22:12.381Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/android/samples.md](https://docs.livekit.io/reference/components/android/samples.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-5"></a>
## Page 5: reference/components/react/installation
**Original URL:** https://docs.livekit.io/reference/components/react/installation  
**Source MD URL:** https://docs.livekit.io/reference/components/react/installation.md

LiveKit docs › React components › Getting started › Installation

---

# Installation

> Learn how to install and set up the @livekit/components-react package for React.

Use your favorite package manager to install the LiveKit Components package and its dependencies:

**yarn**:

```shell
yarn add @livekit/components-react @livekit/components-styles livekit-client

```

---

**npm**:

```shell
npm install @livekit/components-react @livekit/components-styles livekit-client

```

---

**pnpm**:

```shell
pnpm install @livekit/components-react @livekit/components-styles livekit-client

```

> ℹ️ **Note**
> 
> When installing the `@livekit/components-react` npm package, it's important to note that it relies on the `livekit-client` and `@livekit/components-styles` packages. This dependency is necessary for the package to function properly.

---

This document was rendered at 2026-08-28T04:22:12.380Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/installation.md](https://docs.livekit.io/reference/components/react/installation.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-6"></a>
## Page 6: reference/components/react/guide
**Original URL:** https://docs.livekit.io/reference/components/react/guide  
**Source MD URL:** https://docs.livekit.io/reference/components/react/guide.md

LiveKit docs › React components › Getting started › Best practices

---

# Best practices

> Recommendations for creating apps using LiveKit React components.

## Use LiveKit components for lower-level features

You can create custom React components for your LiveKit app. For lower-level features (for example, mic toggle), however, LiveKit components are built using utility state handling hooks. LiveKit strongly recommends you use these instead of creating your own implementation because they manage React state handling and have been rigorously tested. Lower-level features include input device toggling, and audio and video tracks:

- [StartAudio](https://docs.livekit.io/reference/components/react/component/startaudio.md)
- [StartMediaButton](https://docs.livekit.io/reference/components/react/component/startmediabutton.md)
- [TrackToggle](https://docs.livekit.io/reference/components/react/component/tracktoggle.md)
- [TrackLoop](https://docs.livekit.io/reference/components/react/component/trackloop.md)

If you do create custom components, use the provided hooks for state. For example, to create a custom mic toggle button, use `useTrackToggle`:

```typescript
const { buttonProps, enabled } = useTrackToggle(props);
  return (
    <button ref={ref} {...buttonProps}>
      {(showIcon ?? true) && getSourceIcon(props.source, enabled)}
      {props.children}
    </button>
  );

```

## Using hooks for current state

LiveKit recommends using [hooks](https://docs.livekit.io/reference/components/react/concepts/building-blocks.md#hooks) to get the most current information about room state. For example, to get a list of active tracks or participants in a room:

- [useParticipants](https://docs.livekit.io/reference/components/react/hook/useparticipants.md)
- [useTracks](https://docs.livekit.io/reference/components/react/hook/usetracks.md)

## Updating props for the LiveKitRoom component

Updating props for the `LiveKitRoom` component should _not_ result in the component being repeatedly unmounted and remounted. This results in `Client initiated disconnect` errors and cause users to be repeatedly disconnected and reconnected to the room.

---

This document was rendered at 2026-08-28T04:22:12.408Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/guide.md](https://docs.livekit.io/reference/components/react/guide.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-7"></a>
## Page 7: reference/components/agents-ui/block/agent-session-view-01
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/block/agent-session-view-01  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/block/agent-session-view-01.md

LiveKit docs › Agents UI › Blocks › AgentSessionView - 01

---

# Agent Session View - 01

> A complete realtime agent session view with transcript, audio visualizer, and media controls.

## Usage

**AgentSessionView_01** preview:

```tsx
'use client';

import { useSession } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentSessionView_01 } from '@/components/agents-ui/blocks/agent-session-view-01/components/agent-session-block';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <AgentSessionView_01
        preConnectMessage="Agent is listening, ask it a question"
        isPreConnectBufferEnabled={true}
        controls={{"leave":true,"microphone":true,"chat":true,"camera":true,"screenShare":true}}
        audioVisualizer={{"type":"aura","colorShift":0.3}}
      />
    </AgentSessionProvider>
  );
}
```

## Features

- Render a complete agent session surface with transcript and controls.
- Toggle chat, camera, and screen share support in the control bar.
- Show a pre-connect shimmer prompt before the first message arrives.
- Configure multiple audio visualizer styles and variant-specific options.
- Pass a custom `className` to extend layout styling.

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-session-view-01

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `ref?` | Ref<HTMLElement> | – |
| `className?` | string | – |
| `themeMode?` | enum | – |
| `preConnectMessage?` | string | `Agent is listening, ask it a question` |
| `supportsChatInput?` | boolean | `true` |
| `supportsVideoInput?` | boolean | `true` |
| `supportsScreenShare?` | boolean | `true` |
| `isPreConnectBufferEnabled?` | boolean | `true` |
| `audioVisualizerType?` | enum | – |
| `audioVisualizerColor?` | `#${string}` | – |
| `audioVisualizerColorShift?` | number | – |
| `audioVisualizerBarCount?` | number | – |
| `audioVisualizerGridRowCount?` | number | – |
| `audioVisualizerGridColumnCount?` | number | – |
| `audioVisualizerRadialBarCount?` | number | – |
| `audioVisualizerRadialRadius?` | number | – |
| `audioVisualizerWaveLineWidth?` | number | – |

---

This document was rendered at 2026-08-28T04:22:14.082Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/block/agent-session-view-01.md](https://docs.livekit.io/reference/components/agents-ui/block/agent-session-view-01.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-8"></a>
## Page 8: reference/components/agents-ui/component/agent-control-bar
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-control-bar  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-control-bar.md

LiveKit docs › Agents UI › Components › Media controls › AgentControlBar

---

# Agent Control Bar

> A control bar for managing media tracks (microphone, camera, screen share), opening the chat input, and disconnecting the agent session.

## Usage

**AgentControlBar** preview:

```tsx
'use client';

import { useSession } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentControlBar } from '@/components/agents-ui/agent-control-bar';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <AgentControlBar
        variant="livekit"
        isChatOpen={false}
        isConnected={true}
        controls={{"leave":true,"microphone":true,"screenShare":true,"camera":true,"chat":true}}
      />
    </AgentSessionProvider>
  );
}
```

## Features

- Configure which controls are visible: `microphone`, `camera`, `screenShare`, `chat`, and `leave`
- Select from three styles: `default`, `outline`, and `livekit`
- Control chat input visibility with `isChatOpen` and `onIsChatOpenChange`
- Persist user device preferences with `saveUserChoices` (enabled by default)
- Handle device errors

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-control-bar

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `variant?` | enum | `default` |
| `controls?` | AgentControlBarControls | `{
  leave: true,
  microphone: true,
  screenShare: true,
  camera: true,
  chat: true,
}` |
| `saveUserChoices?` | boolean | `true` |
| `isConnected?` | boolean | – |
| `isChatOpen?` | boolean | – |
| `onDisconnect?` | () => void | – |
| `onIsChatOpenChange?` | (open: boolean) => void | – |
| `onDeviceError?` | (error: { source: Source; error: Error; }) => void | – |
| `ref?` | Ref<HTMLDivElement> | – |
| `...props?` | ComponentProps<'div'> | |

---

This document was rendered at 2026-08-28T04:22:14.110Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-control-bar.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-control-bar.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-9"></a>
## Page 9: reference/components/agents-ui/component/agent-track-control
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-track-control  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-track-control.md

LiveKit docs › Agents UI › Components › Media controls › AgentTrackControl

---

# Agent Track Control

> A UI control for managing media tracks (microphone, camera, screen share).

## Usage

**AgentTrackControl** preview:

```tsx
'use client';

import { useSession, useAgent } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const { audioTrack } = useAgent();
  const handlePressedChange = (pressed: boolean) => console.log('pressed', pressed);
  const handleMediaDeviceError = (error: Error) => console.log('error', error);
  const handleActiveDeviceChange = (deviceId: string) => console.log('deviceId', deviceId);

  return (
    <AgentTrackControl
      variant="default"
      source="microphone"
      pressed={false}
      pending={false}
      disabled={false}
      // provide audioTrack to render an audio visualizer
      audioTrack={audioTrack}
      onPressedChange={handlePressedChange}
      onMediaDeviceError={handleMediaDeviceError}
      onActiveDeviceChange={handleActiveDeviceChange}
    />
  );
}
  
export function DemoWrapper() {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <Demo />
    </AgentSessionProvider>
  );
}
```

## Features

- Toggle the capture of a client's media input (microphone, camera, screen share)
- Select from five sizes: `icon`, `sm`, `md`, `lg`, and `xl`
- Select from three styles: `default`, `outline`, and `livekit`
- Renders an audio visualizer when an audio track is provided
- Displays a select dropdown when multiple input devices are available

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-track-control

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `kind` | enum | – |
| `source` | enum | – |
| `pressed?` | boolean | – |
| `pending?` | boolean | – |
| `disabled?` | boolean | – |
| `audioTrack?` | TrackReferenceOrPlaceholder | – |
| `className?` | string | – |
| `onPressedChange?` | (pressed: boolean) => void | – |
| `onMediaDeviceError?` | (error: Error) => void | – |
| `onActiveDeviceChange?` | (deviceId: string) => void | – |

---

This document was rendered at 2026-08-28T04:22:14.141Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-track-control.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-track-control.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-10"></a>
## Page 10: reference/components/agents-ui/component/agent-track-toggle
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-track-toggle  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-track-toggle.md

LiveKit docs › Agents UI › Components › Media controls › AgentTrackToggle

---

# Agent Track Toggle

> A UI toggle for capturing a client's media input (microphone, camera, screen share).

## Usage

**AgentTrackToggle** preview:

```tsx
'use client';

import { useSession } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentTrackToggle } from '@/components/agents-ui/agent-track-toggle';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');
  
export function Demo() {
  const session = useSession(TOKEN_SOURCE);
  const handlePressedChange = (pressed: boolean) => console.log('pressed', pressed);

  return (
    <AgentSessionProvider session={session}>
      <AgentTrackToggle
        variant="default"
        source="microphone"
        pressed={false}
        pending={false}
        disabled={false}
        onPressedChange={handlePressedChange}
      />
    </AgentSessionProvider>
  );
}
```

## Features

- Toggle the capture of a client's media input (microphone, camera, screen share)
- Select from five sizes: `icon`, `sm`, `md`, `lg`, and `xl`
- Select from three styles: `default`, `outline`, and `livekit`

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-track-toggle

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `size?` | enum | `default` |
| `variant?` | enum | `default` |
| `ref?` | Ref<HTMLButtonElement> | – |
| `source` | enum | – |
| `pending?` | boolean | – |
| `pressed?` | boolean | – |
| `defaultPressed?` | boolean | – |
| `onPressedChange?` | (pressed: boolean) => void | – |
| `...props?` | ComponentProps<'button'> | |

---

This document was rendered at 2026-08-28T04:22:14.163Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-track-toggle.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-track-toggle.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-11"></a>
## Page 11: reference/components/agents-ui/component/agent-audio-visualizer-bar
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-bar  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-bar.md

LiveKit docs › Agents UI › Components › Audio visualizers › AgentAudioVisualizerBar

---

# Agent Audio Visualizer – Bar

> An audio visualization of linear bouncing bars.

## Usage

**AgentAudioVisualizerBar** preview:

```tsx
'use client';

import { useSession, useAgent } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentAudioVisualizerBar } from '@/components/agents-ui/agent-audio-visualizer-bar';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const { audioTrack, state } = useAgent();

  return (
    <AgentAudioVisualizerBar
      size="lg"
      color={undefined}
      barCount={5}
      state={state}
      audioTrack={audioTrack}
    />
  );
}

export default function DemoWrapper({ session }) {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <Demo />
    </AgentSessionProvider>
  );
}
```

## Features

- Visualize an agent's audio track
- Configure the number of bars used in the visualizer
- Select from five sizes: `icon`, `sm`, `md`, `lg`, and `xl`
- Responds to agent state with unique animations

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-audio-visualizer-bar

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `size?` | enum | `md` |
| `state?` | enum | `connecting` |
| `color?` | `#${string}` | – |
| `barCount?` | number | – |
| `audioTrack?` | LocalAudioTrack | RemoteAudioTrack | TrackReferenceOrPlaceholder | – |
| `volumeBands?` | number[] | – |
| `className?` | string | – |
| `children?` | ReactNode | – |
| `ref?` | Ref<HTMLDivElement> | – |
| `...props?` | ComponentProps<'div'> | |

---

This document was rendered at 2026-08-28T04:22:14.165Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-bar.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-bar.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-12"></a>
## Page 12: reference/components/agents-ui/component/agent-audio-visualizer-grid
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-grid  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-grid.md

LiveKit docs › Agents UI › Components › Audio visualizers › AgentAudioVisualizerGrid

---

# Agent Audio Visualizer – Grid

> An audio visualization of a grid of particles.

## Usage

**AgentAudioVisualizerGrid** preview:

```tsx
'use client';

import { useSession, useAgent } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentAudioVisualizerGrid } from '@/components/agents-ui/agent-audio-visualizer-grid';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const { audioTrack, state } = useAgent();

  return (
    <AgentAudioVisualizerGrid
      size="lg"
      color={undefined}
      radius={3}
      interval={100}
      rowCount={15}
      columnCount={15}
      state={state}
      audioTrack={audioTrack}
    />
  );
}

export default function DemoWrapper({ session }) {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <Demo />
    </AgentSessionProvider>
  );
}
```

## Features

- Visualize an agent's audio track
- Configure the speed, row and column size
- Select from five sizes: `icon`, `sm`, `md`, `lg`, and `xl`
- Responds to agent state with unique animations
- Apply a `transformer` function to generate custom CSS properties for each grid cell

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-audio-visualizer-grid

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `radius?` | number | – |
| `interval?` | number | `100` |
| `rowCount?` | number | `5` |
| `columnCount?` | number | `5` |
| `className?` | string | – |
| `size?` | enum | `md` |
| `state?` | enum | `connecting` |
| `color?` | `#${string}` | – |
| `audioTrack?` | LocalAudioTrack | RemoteAudioTrack | TrackReferenceOrPlaceholder | – |
| `volumeBands?` | number[] | – |
| `children?` | ReactNode | – |
| `ref?` | Ref<HTMLDivElement> | – |
| `...props?` | ComponentProps<'div'> | |

---

This document was rendered at 2026-08-28T04:22:14.192Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-grid.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-grid.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-13"></a>
## Page 13: reference/components/agents-ui/component/agent-audio-visualizer-radial
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-radial  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-radial.md

LiveKit docs › Agents UI › Components › Audio visualizers › AgentAudioVisualizerRadial

---

# Agent Audio Visualizer – Radial

> An audio visualization of a radial bouncing bar.

## Usage

**AgentAudioVisualizerRadial** preview:

```tsx
'use client';

import { useSession, useAgent } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentAudioVisualizerRadial } from '@/components/agents-ui/agent-audio-visualizer-radial';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const { audioTrack, state } = useAgent();

  return (
    <AgentAudioVisualizerRadial
      size="lg"
      color={undefined}
      radius={undefined}
      state={state}
      audioTrack={audioTrack}
    />
  );
}

export default function DemoWrapper({ session }) {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <Demo />
    </AgentSessionProvider>
  );
}
```

## Features

- Visualize an agent's audio track
- Customize the number of bars and radius of the visualizer
- Select from five sizes: `icon`, `sm`, `md`, `lg`, and `xl`
- Responds to agent state with unique animations

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-audio-visualizer-radial

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `size?` | enum | `md` |
| `state?` | enum | `connecting` |
| `color?` | `#${string}` | – |
| `radius?` | number | – |
| `barCount?` | number | – |
| `audioTrack?` | LocalAudioTrack | RemoteAudioTrack | TrackReferenceOrPlaceholder | – |
| `volumeBands?` | number[] | – |
| `className?` | string | – |
| `ref?` | Ref<HTMLDivElement> | – |
| `...props?` | ComponentProps<'div'> | |

---

This document was rendered at 2026-08-28T04:22:14.174Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-radial.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-radial.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-14"></a>
## Page 14: reference/components/agents-ui/component/agent-audio-visualizer-wave
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-wave  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-wave.md

LiveKit docs › Agents UI › Components › Audio visualizers › AgentAudioVisualizerWave

---

# Agent Audio Visualizer – Wave

> A shader based audio visualization of a sine wave.

## Usage

**AgentAudioVisualizerWave** preview:

```tsx
'use client';

import { useSession, useAgent } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentAudioVisualizerWave } from '@/components/agents-ui/agent-audio-visualizer-wave';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const { audioTrack, state } = useAgent();

  return (
    <AgentAudioVisualizerWave
      size="xl"
      color="#1FD5F9"
      blur={0.1}
      lineWidth={2}
      audioTrack={audioTrack}
      state={state}
      colorShift={0.3}
    />
  );
}

export default function DemoWrapper({ session }) {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <Demo />
    </AgentSessionProvider>
  );
}
```

## Features

- Visualize an agent's audio track
- Customize the color, line width and smoothing of the wave
- Select from five sizes: `icon`, `sm`, `md`, `lg`, and `xl`
- Responds to agent state with unique animations

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-audio-visualizer-wave

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `size?` | enum | `lg` |
| `state?` | enum | `speaking` |
| `color?` | `#${string}` | – |
| `colorShift?` | number | `0.05` |
| `lineWidth?` | number | – |
| `blur?` | number | – |
| `audioTrack?` | LocalAudioTrack | RemoteAudioTrack | TrackReferenceOrPlaceholder | – |
| `volume?` | number | – |
| `className?` | string | – |
| `ref?` | Ref<HTMLDivElement> | – |
| `...props?` | ComponentProps<'div'> | |

---

This document was rendered at 2026-08-28T04:22:14.184Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-wave.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-wave.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-15"></a>
## Page 15: reference/components/agents-ui/component/agent-audio-visualizer-aura
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-aura  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-aura.md

LiveKit docs › Agents UI › Components › Audio visualizers › AgentAudioVisualizerAura

---

# Agent Audio Visualizer – Aura

> A shader based audio visualization of a pulsing energy field.

## Usage

**AgentAudioVisualizerAura** preview:

```tsx
'use client';

    
import { useTheme } from 'next-themes';
import { useSession, useAgent } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentAudioVisualizerAura } from '@/components/agents-ui/agent-audio-visualizer-aura';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const { resolvedTheme: theme } = useTheme();
  const { audioTrack, state } = useAgent();

  return (
    <AgentAudioVisualizerAura
      size="xl"
      color="#1FD5F9"
      colorShift={0.1}
      state={state}
      themeMode={theme}
      audioTrack={audioTrack}
    />
  );
}

export default function DemoWrapper({ session }) {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <Demo />
    </AgentSessionProvider>
  );
}
```

> ℹ️ **Note**
> 
> This component was designed in partnership with Unicorn Studio.

- **[Unicorn Studio](https://www.unicorn.studio/)**: Create jaw-dropping motion and interaction in minutes — no code. Embed with a few clicks.

## Features

- Visualize an agent's audio track
- Customize the color and color shift of the aura
- Select from five sizes: `icon`, `sm`, `md`, `lg`, and `xl`
- Responds to agent state with unique animations
- Light and dark mode support

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-audio-visualizer-aura

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `size?` | enum | `lg` |
| `state?` | enum | `connecting` |
| `color?` | `#${string}` | `#1FD5F9` |
| `colorShift?` | number | `0.05` |
| `themeMode?` | enum | – |
| `audioTrack?` | LocalAudioTrack | RemoteAudioTrack | TrackReferenceOrPlaceholder | – |
| `volume?` | number | – |
| `ref?` | Ref<HTMLDivElement> | – |
| `...props?` | ComponentProps<'div'> | |

---

This document was rendered at 2026-08-28T04:22:14.189Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-aura.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-audio-visualizer-aura.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-16"></a>
## Page 16: reference/components/agents-ui/component/agent-session-provider
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-session-provider  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-session-provider.md

LiveKit docs › Agents UI › Components › Session management › AgentSessionProvider

---

# Agent Session Provider

> A context provider for the LiveKit agent session.

## Usage

**AgentSessionProvider** preview:

```tsx
'use client';

import { useSession } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      {/* Agent UI application components go here */}
    </AgentSessionProvider>
  );
}
```

## Features

- Provides the agent session to the descendant components
- Ensures remote participants’ audio tracks (microphones and screen share) are audible

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-session-provider

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `session` | UseSessionReturn | – |
| `children` | ReactNode | – |
| `room?` | Room | – |
| `volume?` | number | – |
| `muted?` | boolean | – |

---

This document was rendered at 2026-08-28T04:22:14.189Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-session-provider.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-session-provider.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-17"></a>
## Page 17: reference/components/agents-ui/component/agent-disconnect-button
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-disconnect-button  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-disconnect-button.md

LiveKit docs › Agents UI › Components › Session management › AgentDisconnectButton

---

# Agent Disconnect Button

> A button for disconnecting the agent session.

## Usage

**AgentDisconnectButton** preview:

```tsx
'use client';

import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentDisconnectButton } from '@/components/agents-ui/agent-disconnect-button';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export default function Demo({ session }) {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <AgentDisconnectButton
        size="default"
        variant="destructive"
        disabled={false}
      >
        End Call
      </AgentDisconnectButton>
    </AgentSessionProvider>
  );
}
```

## Features

- Customizable with `icon` and `children` props
- Calls `session.end()` when clicked

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-disconnect-button

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `icon?` | ReactNode | – |
| `size?` | enum | `default` |
| `variant?` | enum | `destructive` |
| `children?` | ReactNode | – |
| `onClick?` | (event: MouseEvent<HTMLButtonElement, MouseEvent>) => void | – |
| `ref?` | Ref<HTMLButtonElement> | – |
| `...props?` | ComponentProps<'button'> | |

---

This document was rendered at 2026-08-28T04:22:14.227Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-disconnect-button.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-disconnect-button.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-18"></a>
## Page 18: reference/components/agents-ui/component/start-audio-button
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/start-audio-button  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/start-audio-button.md

LiveKit docs › Agents UI › Components › Session management › StartAudioButton

---

# Start Audio Button

> A button for starting the agent session's audio track when the browser blocks audio playback.

## Usage

**StartAudioButton** preview:

```tsx
'use client';

import { useSession } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { StartAudioButton } from '@/components/agents-ui/start-audio-button';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <StartAudioButton label="Start Audio"/>
    </AgentSessionProvider>
  );
}
```

## Features

- Displays a button for starting the agent session's audio tracks when the browser blocks audio playback

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/start-audio-button

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `size?` | enum | `default` |
| `variant?` | enum | `default` |
| `room?` | Room | – |
| `label` | string | – |
| `ref?` | Ref<HTMLButtonElement> | – |
| `...props?` | ComponentProps<'button'> | |

---

This document was rendered at 2026-08-28T04:22:14.208Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/start-audio-button.md](https://docs.livekit.io/reference/components/agents-ui/component/start-audio-button.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-19"></a>
## Page 19: reference/components/agents-ui/component/agent-chat-indicator
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-indicator  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-indicator.md

LiveKit docs › Agents UI › Components › Chat components › AgentChatIndicator

---

# Agent Chat Indicator

> An animated chat indicator for asynchronous states.

## Usage

**AgentChatIndicator** preview:

```tsx
import { AgentChatIndicator } from '@/components/agents-ui/agent-chat-indicator';

export function Demo() {
  return (
    <AgentChatIndicator
      size={undefined}
    />
  );
}
```

## Features

- Display a pulsing chat indicator
- Select from three sizes: `sm`, `md`, and `lg`
- Communicate asynchronous agent states to the user

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-chat-indicator

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `size?` | enum | `md` |
| `className?` | string | – |
| `ref?` | Ref<HTMLSpanElement> | – |
| `...props?` | ComponentProps<'span'> | |

---

This document was rendered at 2026-08-28T04:22:14.211Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-indicator.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-indicator.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-20"></a>
## Page 20: reference/components/agents-ui/component/agent-chat-transcript
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-transcript  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-transcript.md

LiveKit docs › Agents UI › Components › Chat components › AgentChatTranscript

---

# Agent Chat Transcript

> A chat transcript for displaying conversational history.

## Usage

**AgentChatTranscript** preview:

```tsx
'use client';

import { 
  useSession, 
  useAgent,
  useSessionContext,
  useSessionMessages, 
} from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import { AgentChatTranscript } from '@/components/agents-ui/agent-chat-transcript';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const { state } = useAgent();
  const session = useSessionContext();
  const { messages } = useSessionMessages(session);

  return (
    <AgentChatTranscript
      agentState={state}
      messages={messages}
    />
  );
}

export default function DemoWrapper({ session }) {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <Demo />
    </AgentSessionProvider>
  );
}
```

## Features

- Display the session's chat history in a styled list
- Renders the [`AgentChatIndicator`](https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-indicator.md) when the `agentState` is "thinking"
- Supports both plain text and markdown formatting
- Automatically scrolls to the latest message
- Handles message updates and deletions

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-chat-transcript

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `autoScroll?` | boolean | `true` |
| `scrollAnchor?` | boolean | "user" | "other" | "any" | – |
| `scrollButtonRender?` | any | – |
| `scrollButtonBehavior?` | any | – |
| `scrollButtonDirection?` | any | – |
| `agentState?` | enum | – |
| `messages?` | ReceivedMessage[] | `[]` |
| `className?` | string | – |
| `ref?` | Ref<HTMLDivElement> | – |
| `...props?` | ComponentProps<'div'> , ComponentProps<typeof MessageScrollerProvider>, ComponentProps<typeof MessageScrollerViewport>, ComponentProps<typeof MessageScrollerContent> | |

---

This document was rendered at 2026-08-28T04:22:14.238Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-transcript.md](https://docs.livekit.io/reference/components/agents-ui/component/agent-chat-transcript.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-21"></a>
## Page 21: reference/components/agents-ui/component/nextjs-api-token-route
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/nextjs-api-token-route  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/nextjs-api-token-route.md

LiveKit docs › Agents UI › Components › Miscellaneous › NextJS API Token Route

---

# Next.js API Token Route

> A NextJS API route to generate a LiveKit session token while keeping your API keys private.

## Usage

1. Add your LiveKit API keys to a `.env.local` file in your project root.

```env
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret
LIVEKIT_URL=your-livekit-url

```
2. Create a new  [TokenSource](https://docs.livekit.io/frontends/build/authentication/endpoint.md) that points your new `/api/token` endpoint.

```tsx
'use client';

import { useSession } from '@livekit/components-react';
import { AgentSessionProvider } from '@/components/agents-ui/agent-session-provider';
import MyAgent from '@/components/my-agent';

const TOKEN_SOURCE = TokenSource.endpoint('/api/token');

export function Demo() {
  const session = useSession(TOKEN_SOURCE);

  return (
    <AgentSessionProvider session={session}>
      <MyAgent />
    </AgentSessionProvider>
  );
}

```

## Features

- Generates a LiveKit session token using a NextJS API route
- Keeps your API keys private

> 🔥 **This route requires authentication in production**
> 
> This route is insecure by default to enable local development.

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/nextjs-api-token-route

```

---

This document was rendered at 2026-08-28T04:22:14.275Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/nextjs-api-token-route.md](https://docs.livekit.io/reference/components/agents-ui/component/nextjs-api-token-route.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-22"></a>
## Page 22: reference/components/agents-ui/component/react-shader-toy
**Original URL:** https://docs.livekit.io/reference/components/agents-ui/component/react-shader-toy  
**Source MD URL:** https://docs.livekit.io/reference/components/agents-ui/component/react-shader-toy.md

LiveKit docs › Agents UI › Components › Miscellaneous › ReactShaderToy

---

# React Shader Toy

> Easily render ShaderToy based shaders.

> ℹ️ **Note**
> 
> This component was forked from Rysana's [react-shaders](https://rysana.com/docs/react-shaders) and modified to work with the latest version of [React](https://react.dev/) and [Next.js](https://nextjs.org/).

## Usage

**ReactShaderToy** preview:

```tsx
'use client';

import { ReactShaderToy } from '@/components/agents-ui/react-shader-toy';

const fs = `
void mainImage( out vec4 fragColor, in vec2 fragCoord ) {
  vec2 uv = fragCoord/iResolution.xy;
  vec3 col = 0.5 + 0.5*cos(iTime+uv.xyx+vec3(0,2,4));
  fragColor = vec4(col,1.0);
}
`;

export function Demo() {
  return <ReactShaderToy fs={fs} />;
}
```

## Features

- Easily create and render [ShaderToy](https://www.shadertoy.com/) shaders in your React application
- Provide custom uniforms and textures
- Provide custom WebGL context attributes

## Installation

```bash
pnpm dlx shadcn@latest add @agents-ui/agent-audio-visualizer-bar

```

## Props

| Prop name | Type | Default |
| --------- | ---- | ------- |
| `fs` | string | – |
| `vs?` | string | ``attribute vec3 aVertexPosition;
void main(void) {
    gl_Position = vec4(aVertexPosition, 1.0);
}`` |
| `textures?` | TextureParams[] | `[]` |
| `uniforms?` | Uniforms | – |
| `clearColor?` | Vector4<number> | `[0, 0, 0, 1]` |
| `precision?` | enum | `highp` |
| `style?` | CSSProperties | – |
| `contextAttributes?` | Record<string, unknown> | `{}` |
| `lerp?` | number | `1` |
| `devicePixelRatio?` | number | `1` |
| `onDoneLoadingTextures?` | () => void | – |
| `onError?` | ((error: string) => void) & ReactEventHandler<HTMLCanvasElement> | `console.error` |
| `onWarning?` | (warning: string) => void | `console.warn` |
| `animateWhenNotVisible?` | boolean | – |

---

This document was rendered at 2026-08-28T04:22:14.290Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/agents-ui/component/react-shader-toy.md](https://docs.livekit.io/reference/components/agents-ui/component/react-shader-toy.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-23"></a>
## Page 23: reference/components/android/concepts/building-blocks
**Original URL:** https://docs.livekit.io/reference/components/android/concepts/building-blocks  
**Source MD URL:** https://docs.livekit.io/reference/components/android/concepts/building-blocks.md

LiveKit docs › Android Components › Concepts › Building Blocks

---

# Building Blocks

> A short tour through everything you need to build your next LiveKit app.

## Components

Components are the basic building blocks of your LiveKit application, enriched with additional functionality and LiveKit state.

### Scopes

Scopes help manage the LiveKit state as well as providing a CompositionLocal for simplifying passing data down into your composables.

- [RoomScope](https://docs.livekit.io/reference/components-android/livekit-compose-components/io.livekit.android.compose.local/-room-scope.html.md): This scope is the basis for using LiveKit within composables.
- [ParticipantScope](https://docs.livekit.io/reference/components-android/livekit-compose-components/io.livekit.android.compose.local/-participant-scope.html.md): This scope provides a CompositionLocal for a participant.

### UI Composables

This library provides UI composables that will form the basis for your LiveKit application.

- [VideoTrackView](https://docs.livekit.io/reference/components-android/livekit-compose-components/io.livekit.android.compose.ui/-video-track-view.html.md): Displays a video track.
- [CameraPreview](https://docs.livekit.io/reference/components-android/livekit-compose-components/io.livekit.android.compose.ui/-camera-preview.html.md): Provides a preview of the camera to be used prior to connecting to LiveKit.

## State Handling

We provide a wide range of `remember` functions that make state management easier. Some hooks are foundational and are needed for almost every live app, while others are only needed if you want to build some custom components and go low-level.

Often used and important hooks are:

- [rememberTracks](https://docs.livekit.io/reference/components-android/livekit-compose-components/io.livekit.android.compose.state/remember-tracks.html.md): The rememberTracks state returns an array of current tracks that can be looped, filtered, and processed.
- [rememberParticipants](https://docs.livekit.io/reference/components-android/livekit-compose-components/io.livekit.android.compose.state/remember-participants.html.md): The rememberParticipants state returns all participants (local and remote) of the current room.
- [rememberTrackMuted](https://docs.livekit.io/reference/components-android/livekit-compose-components/io.livekit.android.compose.state/remember-track-muted.html.md): The rememberTrackMuted state allows you to simply implement your own muted indicator.

Additionally, LiveKit class members marked with the `@FlowObservable` can be observed and converted into Compose State with the `io.livekit.android.util.flow` utility function.

> 💡 **Tip**
> 
> Avoid using class member values directly, as that may result in Compose not updating when the values change.

```kotlin
// Avoid!
// val roomName = room.name

// Instead, use its flow and collect as state.
val roomName by room::name.flow.collectAsState()

```

---

This document was rendered at 2026-08-28T04:22:14.297Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/android/concepts/building-blocks.md](https://docs.livekit.io/reference/components/android/concepts/building-blocks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-24"></a>
## Page 24: reference/components/android/concepts/rendering-a-track
**Original URL:** https://docs.livekit.io/reference/components/android/concepts/rendering-a-track  
**Source MD URL:** https://docs.livekit.io/reference/components/android/concepts/rendering-a-track.md

LiveKit docs › Android Components › Concepts › Rendering a single Track

---

# Rendering a single track

To demonstrate how to build a UI to render a single video stream, imagine this scenario:

We have a LiveKit Room with three Participants who are constantly streaming a camera feed into the room. In our example, the Participants are not human, but webcams streaming from "Berlin", "New York" and "Tokyo". For unknown reasons, we only want to see the stream from "Tokyo".

We start by creating a new composable and get all the camera tracks with `rememberTracks([Track.Source.Camera])`. In the returned array of `TrackReferences` we look for the Tokyo stream. Since we know that all webcam participants are named after their cities, we look for the `tokyo` participant.

```kotlin
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import io.livekit.android.compose.state.rememberTracks
import io.livekit.android.room.track.Track
import io.livekit.android.util.flow

@Composable
fun CityVideoRenderer() {
    val trackRefs = rememberTracks(listOf(Track.Source.CAMERA))
    val tokyoCamTrackRef = trackRefs.find { trackRef ->
        trackRef.participant::name.flow.collectAsState().value == "tokyo"
    }

    // ...
}

```

Now that we have found the correct stream, we can move on to building the UI to display it. We can do this by using the `VideoTrackView` composable and passing it the track reference. If the Tokyo track reference is not found, we will display a UI to indicate this instead.

```kotlin
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import io.livekit.android.compose.state.rememberTracks
import io.livekit.android.compose.ui.VideoTrackView
import io.livekit.android.room.track.Track
import io.livekit.android.util.flow

@Composable
fun CityVideoRenderer() {
    val trackRefs = rememberTracks(listOf(Track.Source.CAMERA))
    val tokyoCamTrackRef = trackRefs.find { trackRef ->
        trackRef.participant::name.flow.collectAsState().value == "tokyo"
    }

    if (tokyoCamTrackRef != null) {
        VideoTrackView(trackReference = tokyoCamTrackRef)
    } else {
        BasicText(text = "Tokyo is offline")
    }
}


```

With our UI in place, we need to provide rememberTracks with the proper scope to return the tracks of a LiveKit Room. We do this by nesting everything inside a RoomScope.

```kotlin
import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import io.livekit.android.compose.local.RoomScope
import io.livekit.android.compose.state.rememberTracks
import io.livekit.android.compose.ui.VideoTrackView
import io.livekit.android.room.track.Track
import io.livekit.android.util.flow

@Composable
fun CityVideoRenderer() {
    val trackRefs = rememberTracks(listOf(Track.Source.CAMERA))
    val tokyoCamTrackRef = trackRefs.find { trackRef ->
        trackRef.participant::name.flow.collectAsState().value == "tokyo"
    }

    if (tokyoCamTrackRef != null) {
        VideoTrackView(trackReference = tokyoCamTrackRef)
    } else {
        BasicText(text = "Tokyo is offline")
    }
}

@Composable
fun MyPage() {
    RoomScope {
        CityVideoRenderer()
    }
}

```

---

This document was rendered at 2026-08-28T04:22:14.316Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/android/concepts/rendering-a-track.md](https://docs.livekit.io/reference/components/android/concepts/rendering-a-track.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-25"></a>
## Page 25: reference/components/android/concepts/roomscope
**Original URL:** https://docs.livekit.io/reference/components/android/concepts/roomscope  
**Source MD URL:** https://docs.livekit.io/reference/components/android/concepts/roomscope.md

LiveKit docs › Android Components › Concepts › RoomScope

---

# The RoomScope

The `RoomScope` composable is the root of your LiveKit application. It handles the Room object creation and connection, and sets the `RoomLocal` for its child composables.

```tsx
import androidx.compose.runtime.Composable
import io.livekit.android.compose.local.RoomScope

@Composable
fun MyLiveKitApp() {
    RoomScope(
        url = "server-url",
        token = "access-token",
        connect = true
    ) {
        /* Your composables go here */
    }
}

```

---

This document was rendered at 2026-08-28T04:22:14.319Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/android/concepts/roomscope.md](https://docs.livekit.io/reference/components/android/concepts/roomscope.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-26"></a>
## Page 26: reference/components/android/concepts/scopes
**Original URL:** https://docs.livekit.io/reference/components/android/concepts/scopes  
**Source MD URL:** https://docs.livekit.io/reference/components/android/concepts/scopes.md

LiveKit docs › Android Components › Concepts › Scopes

---

# Scopes

> Learn how scopes in LiveKit components provide easy access to the parent state for nested composables.

## What is a Scope

Scopes are CompositionLocalProviders that are used to allow child composables to access parent state without the need to pass it via method arguments throughout composition. In return, this means that if a composable depends on some scope you have to make sure that this scope is provided somewhere higher up in the composition.

```kotlin
// ✅ This works!
// rememberRoomInfo depends on the RoomLocal which is provided by RoomScope.
@Composable
fun MyPage() {
  RoomScope {
    val roomInfo = rememberRoomInfo()
  }
}

// ✅ This works!
// The RoomScope does not have to be an immediate parent of the composable needing RoomLocal.
@Composable
fun MyPage() {
    RoomScope {
        MyCustomComposable()
    }
}

@Composable
fun MyCustomComposable() {
    val roomInfo = rememberRoomInfo()
}

// ❌ This will cause an error!
// rememberRoomInfo depends on a parent scope to provide the RoomLocal.
@Composable
fun MyPage() {
  RoomScope {}
  val roomInfo = rememberRoomInfo()
}


```

The two most important scopes are:

## RoomScope

The RoomScope provides the [Room](https://docs.livekit.io/reference/client-sdk-android/livekit-android-sdk/io.livekit.android.room/-room/index.html.md) object as a composition local.

```kotlin
/* 1️⃣ RoomScope provides the RoomLocal. */
RoomScope(
  url = "server-url",
  token = "user-access-token",
  connect = true,
) {
  /* 2️⃣ rememberRoomInfo uses the RoomLocal to retrieve information about the room. */
  val roomInfo = rememberRoomInfo()
}

```

## ParticipantScope

The ParticipantScope provides a [Participant](https://docs.livekit.io/reference/client-sdk-android/livekit-android-sdk/io.livekit.android.room.participant/-participant/index.html.md) object as a composition local.

```kotlin
/* 1️⃣ ParticipantScope provides the ParticipantLocal. */
ParticipantScope(participant = room.localParticipant) {

  /* 2️⃣ rememberParticipantTrackReferences uses the ParticipantLocal to get the participant's tracks. */
  val participantTracks = rememberParticipantTrackReferences()
}

```

---

This document was rendered at 2026-08-28T04:22:14.311Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/android/concepts/scopes.md](https://docs.livekit.io/reference/components/android/concepts/scopes.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-27"></a>
## Page 27: reference/components/react/concepts/building-blocks
**Original URL:** https://docs.livekit.io/reference/components/react/concepts/building-blocks  
**Source MD URL:** https://docs.livekit.io/reference/components/react/concepts/building-blocks.md

LiveKit docs › React components › Concepts › Building blocks

---

# Building blocks

> A short tour through everything you need to build your next LiveKit app.

## Components

Components are the basic building blocks of your LiveKit application, enriched with additional functionality and LiveKit state. Most components are simply a wrapper around a standard HTML element. This allows you to pass standard HTML attributes like `classNames` and `padding` directly to the underlying HTML element to style it exactly how you want.

### Prefabricated components

Prefabs use components under the hood and add additional features, styles, but also reasonable defaults. They are designed to be opinionated and aren't meant to be extended. Prefabs include the following:

- [VideoConference](https://docs.livekit.io/reference/components/react/component/videoconference.md): This component is the default setup of a classic LiveKit video conferencing app.
- [AudioConference](https://docs.livekit.io/reference/components/react/component/audioconference.md): This component is the default setup of a classic LiveKit audio conferencing app.
- [PreJoin](https://docs.livekit.io/reference/components/react/component/prejoin.md): The PreJoin prefab component is normally presented to the user before they enter a room.
- [ControlBar](https://docs.livekit.io/reference/components/react/component/controlbar.md): The ControlBar prefab component gives the user the basic user interface to control their media devices and leave the room.
- [Chat](https://docs.livekit.io/reference/components/react/component/chat.md): The Chat component adds a basic chat functionality to the LiveKit room. The messages are distributed to all participants in the room.

## Hooks

There are a wide range of React hooks that give you fine-grained control to build the app you want. Some hooks are foundational and are needed for almost every LiveKit app, while others are only needed if you want to build some custom components and go low-level.

The most important and frequently used hooks are the following:

- [useTracks](https://docs.livekit.io/reference/components/react/hook/usetracks.md): The useTracks hook returns an array of current tracks that can be looped, filtered, and processed.
- [useParticipants](https://docs.livekit.io/reference/components/react/hook/useparticipants.md): The useParticipants hook returns all participants (local and remote) of the current room.
- [useConnectionState](https://docs.livekit.io/reference/components/react/hook/useconnectionstate.md): The useConnectionState hook allows you to simply implement your own ConnectionState component.

---

This document was rendered at 2026-08-28T04:22:14.328Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/concepts/building-blocks.md](https://docs.livekit.io/reference/components/react/concepts/building-blocks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-28"></a>
## Page 28: reference/components/react/concepts/livekit-room-component
**Original URL:** https://docs.livekit.io/reference/components/react/concepts/livekit-room-component  
**Source MD URL:** https://docs.livekit.io/reference/components/react/concepts/livekit-room-component.md

LiveKit docs › React components › Concepts › LiveKitRoom component

---

# Room Context Setup

While the `LiveKitRoom` component has historically been used as the root of LiveKit applications, we recommend using the `RoomContext.Provider` directly for more control over room lifecycle and state management. This approach gives you more flexibility while still providing the necessary context for LiveKit components.

```tsx
import * as React from 'react';
import { RoomContext } from '@livekit/components-react';
import { Room } from 'livekit-client';

const MyLiveKitApp = () => {
  const [room] = useState(() => new Room({}));
  
  // You can manage room connection lifecycle here
  useEffect(() => {
    room.connect('your-server-url', 'your-token');
    return () => {
      room.disconnect();
    };
  }, [room]);

  return (
    <RoomContext.Provider value={room}>
      {/* Your components go here */}
    </RoomContext.Provider>
  );
};

```

This pattern offers several advantages:

1. Direct control over Room instantiation and configuration
2. Explicit connection lifecycle management
3. Ability to handle connection states and errors more granularly
4. Better integration with application state management

All LiveKit components that previously worked with `LiveKitRoom` will work identically with this setup, as they rely on the `RoomContext` being available in the component tree.

---

This document was rendered at 2026-08-28T04:22:14.325Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/concepts/livekit-room-component.md](https://docs.livekit.io/reference/components/react/concepts/livekit-room-component.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-29"></a>
## Page 29: reference/components/react/concepts/contexts
**Original URL:** https://docs.livekit.io/reference/components/react/concepts/contexts  
**Source MD URL:** https://docs.livekit.io/reference/components/react/concepts/contexts.md

LiveKit docs › React components › Concepts › Contexts

---

# Contexts

> Learn how contexts in LiveKit components provide easy access to the parent state for nested components.

## What is a context

[Contexts](https://react.dev/learn/passing-data-deeply-with-context) are used to allow child components to access parent state without having to pass it down the component tree via props. However, this means that if a component depends on a context, you must make sure that context is provided somewhere up the component tree.

```tsx

// ✅ This works!
// ConnectionState depends on the RoomContext which is provided by LiveKitRoom.
<LiveKitRoom>
  <ConnectionState />
</LiveKitRoom>

// ✅ This works!
// The context provider (LiveKitRoom) does not have to be an immediate parent of the component (ConnectionState) needing the context.
<LiveKitRoom>
    <div>
        <ConnectionState />
    </div>
</LiveKitRoom>

// ❌ This will cause an error!
// ConnectionState depends on a parent component to provide the RoomContext.
<LiveKitRoom></LiveKitRoom>
<ConnectionState />

```

If you only use LiveKit Components without creating custom components yourself, you don't need to interact with the contexts. Just make sure that the component tree meets the context requirements of all components. If it doesn't, you'll get an error message telling you which context is missing.

The two most important contexts are:

## Room context

The `RoomContext` provides the [Room](https://docs.livekit.io/reference/client-sdk-js/classes/Room.html.md) object as a context. While previously this was primarily provided through the `LiveKitRoom` component, we recommend using `RoomContext.Provider` directly:

```tsx
const MyApp = () => {
  const [room] = useState(() => new Room());
  
  useEffect(() => {
    room.connect('server-url', 'user-access-token');
    return () => room.disconnect();
  }, [room]);

  return (
    <RoomContext.Provider value={room}>
      {/* Components that need room context */}
      <ConnectionState />
    </RoomContext.Provider>
  );
};

```

This approach gives you more control over the Room lifecycle while still providing the necessary context for all LiveKit components.

## Participant context

The `ParticipantContext` provides a [Participant](https://docs.livekit.io/client-sdk-js/classes/Room.html) object to all child components.

```tsx
/* 1️⃣ ParticipantTile provides the ParticipantContext. */
<ParticipantTile>
  {/* 2️⃣ ParticipantName uses the ParticipantContext to get the participant name. */}
  <ParticipantName />
</ParticipantTile>

```

## Accessing contexts

Context access is not required to build an application using LiveKit Components. However, if you want to build custom components that depend on a context, you can use one of the hooks we provide. For example, you can use the [`useRoomContext`](https://docs.livekit.io/reference/components/react/hook/useroomcontext.md) hook to access the `Room` object and the [`useParticipantContext`](https://docs.livekit.io/reference/components/react/hook/useparticipantcontext.md) hook to access the `Participant` object.

---

This document was rendered at 2026-08-28T04:22:14.329Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/concepts/contexts.md](https://docs.livekit.io/reference/components/react/concepts/contexts.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-30"></a>
## Page 30: reference/components/react/concepts/loops
**Original URL:** https://docs.livekit.io/reference/components/react/concepts/loops  
**Source MD URL:** https://docs.livekit.io/reference/components/react/concepts/loops.md

LiveKit docs › React components › Concepts › Loop components

---

# Loop Components

Loop components are a thin layer on top of basic JS for-loops, creating a dedicated React context (`TrackRefContext` or `ParticipantContext`) on each iteration. They accept a child component to use as a template for all elements of the passed array.

## Track Loop

The `TrackLoop` component loops over an array of `TrackReferences` and creates a `TrackRefContext` for every item. We can use it for example to loop over all camera tracks of the room and render them with the `ParticipantTile` component.

```tsx
const cameraTracks = useTracks([Track.Source.Camera]);

<TrackLoop tracks={cameraTracks}>
  <ParticipantTile />
</TrackLoop>;

```

We can nest any other component inside the loop if we need more flexibility or control. If we want to build our own ParticipantTile for full control over styling, we could do this:

```tsx
function MyParticipantTile() {
  return (
    <div style={{ position: 'relative' }}>
      <TrackRefContext.Consumer>
        {(track) => track && <VideoTrack {...track} />}
      </TrackRefContext.Consumer>
    </div>
  );
}

```

And then pass it as a template to the `TrackLoop`.

```tsx
const cameraTracks = useTracks([Track.Source.Camera]);

<TrackLoop tracks={cameraTracks}>
  <MyParticipantTile />
</TrackLoop>;

```

> 💡 **Tip**
> 
> How is this different from the `ParticipantLoop`? One Participant can have more than one Track. E.g. it is not uncommon to loop over all camera as well as screen share tracks.

For more details check out the [TrackLoop](https://docs.livekit.io/reference/components/react/component/trackloop.md) page.

## Participant Loop

The `ParticipantLoop` component loops over an array of Participants and creates a distinct `ParticipantContext` for each child. As an example, to render a list of all the participants' names in the room, we could simply do the following:

```tsx
import { useParticipants, ParticipantLoop, ParticipantName } from `@livekit/react`;

const participants = useParticipants();

<ParticipantLoop participants={participants}>
  // ParticipantName is a LiveKit component that uses the ParticipantContext
  // to render the name of a participant.
  <ParticipantName />
</ParticipantLoop>

```

For more details take a look at the [ParticipantLoop](https://docs.livekit.io/reference/components/react/component/participantloop.md) API page.

## Filter Loops

In order to loop over only a subset of the tracks, you will need to filter the tracks before passing them as a property to the `TrackLoop`. Use the standard [Array.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) function to do so.

```tsx
const tracks = useTracks([
  { source: Track.Source.Camera, withPlaceholder: true },
  { source: Track.Source.ScreenShare, withPlaceholder: false },
]);

const screenShareTracks = tracks.filter(
  (track) => track.publication.source === Track.Source.ScreenShare,
);

// Loop only over screen share tracks.
<TrackLoop tracks={screenShareTracks}>
  <ParticipantTile />
</TrackLoop>;

```

## Default Template

Both loops have in common that they only accept one or no child. If no child is provided the default template is used. If a child is provided, it is used as a template for every item of the loop.

```tsx
// TrackLoop will use the default template.
<TrackLoop trackRefs={tracks}/>

// TrackLoop will use MyComponent as a template.
<TrackLoop trackRefs={tracks}>
  <MyComponent />
</TrackLoop>

```

---

This document was rendered at 2026-08-28T04:22:14.346Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/concepts/loops.md](https://docs.livekit.io/reference/components/react/concepts/loops.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-31"></a>
## Page 31: reference/components/react/concepts/custom-components
**Original URL:** https://docs.livekit.io/reference/components/react/concepts/custom-components  
**Source MD URL:** https://docs.livekit.io/reference/components/react/concepts/custom-components.md

LiveKit docs › React components › Concepts › Custom components

---

# Custom Components

We try to offer a comprehensive set of components that allow you to build something valuable quickly. But we are aware that it would be utopian to think that a limited set of components can cover all wishes and ideas. This is why we made extensibility and customization a central part of LiveKit Components.

## React hooks

Almost every component is accompanied by a React hook with the same name, prefixed with the word `use`. For example, the `ConnectionQualityIndicator` is being built with the `useConnectionQualityIndicator` hook. The same hooks that are used to create LiveKit components can also be used for custom components.

## Custom component example

The best way to see how easy it is to create a custom component is to give a quick example. Let's create a "CustomConnectionQualityIndicator" to replace the existing "ConnectionQualityIndicator".

The default indicator uses icons to indicate how good a subscriber's connection quality is, and we could use it like this:

```tsx
//...
<ParticipantTile>
  <ParticipantName />
  <ConnectionQualityIndicator />
</ParticipantTile>
//...

```

This would display the name of the participant and the quality of the connection as an icon. Suppose that instead of an icon representation, we want a textual representation of the connection status. If a user Ana has a good connection quality, we want it to say "Ana has a good connection quality".

This can be easily achieved with a custom LiveKit component:

```tsx
// 1️⃣ Import the react hook.
import { useConnectionQualityIndicator } from '@livekit/components-react';

// 2️⃣ Define a custom React component.
export function CustomConnectionQualityIndicator(props: HTMLAttributes<HTMLSpanElement>) {
  /**
   * 3️⃣ By using this hook, we inherit all the state management and logic and can focus on our
   * implementation.
   */
  const { quality } = useConnectionQualityIndicator();

  // We create a little helper function to convert the ConnectionQuality to a string.
  function qualityToText(quality: ConnectionQuality): string {
    switch (quality) {
      case ConnectionQuality.Unknown:
        return 'unknown';
      case ConnectionQuality.Poor:
        return 'poor';
      case ConnectionQuality.Good:
        return 'good';
      case ConnectionQuality.Excellent:
        return 'excellent';
    }
  }

  return <span {...props}>{` has a ${qualityToText(quality)} connection quality.`} </span>;
}

```

Now we can replace the default quality indicator with our new `CustomConnectionQualityIndicator` as follows:

```tsx
//...
<ParticipantTile>
  <ParticipantName />
  {/* Custom component: Here we replace the provided <ConnectionQualityIndicator />  with our own implementation. */}
  <CustomConnectionQualityIndicator />
</ParticipantTile>
//...

```

As you can see, it's super easy to create your own components in no time. 🚀

> 💡 **Tip**
> 
> If you want to replace a component, as we did here. Often the quickest way is to copy the current implementation and use it as a starting point for your implementation.

---

This document was rendered at 2026-08-28T04:22:14.363Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/concepts/custom-components.md](https://docs.livekit.io/reference/components/react/concepts/custom-components.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-32"></a>
## Page 32: reference/components/react/concepts/style-components
**Original URL:** https://docs.livekit.io/reference/components/react/concepts/style-components  
**Source MD URL:** https://docs.livekit.io/reference/components/react/concepts/style-components.md

LiveKit docs › React components › Concepts › Style components

---

# Styling LiveKit Components

## Our approach to styling

All LiveKit components come with carefully designed and beautiful styles that you can use right out of the box. If you're happy with the default styles, that's perfect, but if not, we've got you covered too! We do everything we can to give you the freedom to simply override, extend and change the styles to your liking.

## Use the default LiveKit theme

To add styling from our `@livekit/components-styles` package install and import it.

```ts
import '@livekit/components-styles';

```

Our carefully crafted default theme can be applied by adding the data attribute `data-lk-theme="default"` to the `<LiveKitRoom/>` or any HTML container. This will provide all LiveKit components with their default styles and give you access to the theme.

```tsx
// 🅰️ Set the scope of the theme directly on the `LiveKitRoom` component
<LiveKitRoom data-lk-theme="default" >
  {/* Use the color defined in LiveKit default theme. */}
  <button style={{ background: 'var(--lk-danger)' }} >My Button</button>
</LiveKitRoom>

// 🅱️ or on any regular HTML element.
<div data-lk-theme="default" >
  <LiveKitRoom >
  </LiveKitRoom>
</div>


```

## Style LiveKit Components like an HTML element

Almost all LiveKit components are built on a basic HTML element. For example, the `TrackMutedIndicator` component is just a div with some hooks that deal with status (e.g. whether a camera track is muted or not). This means that you can treat the `TrackMutedIndicator` component like a div and pass `className` or `style` properties to apply styling.

```tsx
// Apply custom styling like you would with a regular div element.
<TrackMutedIndictor className="your-classes" style={{ padding: '1rem' }} />

```

## Change global color palette

All components share a small but carefully selected color palette. Each color from the palette is saved as a CSS custom property (CSS variable). You can find the palette [here](https://github.com/livekit/components-js/blob/main/packages/styles/scss/themes/default.scss). Override them as you normally would with CSS custom properties to customize them to your liking.

```css
/* Excerpt of the color palette  */
:root {
  --lk-fg: #111;
  --lk-fg-secondary: #333;
  --lk-fg-tertiary: #555;

  --lk-bg: #fff;
  --lk-bg-secondary: #f5f5f5;
  --lk-bg-tertiary: #fafafa;

  --lk-accent-fg: #fff;
  --lk-accent-bg: #1f8cf9;

  --lk-danger-fg: #fff;
  --lk-danger: #f91f31;
  --lk-danger-text: #6d0311;
  --lk-danger-bg: #fecdd4;

  --lk-success-fg: #fff;
  --lk-success: #1ff968;
  --lk-success-text: #036d26;
  --lk-success-bg: #cdfedd;

  --lk-control-fg: var(--fg);
  --lk-control-bg: var(--bg-secondary);

  --lk-connection-excellent: #06db4d;
  --lk-connection-good: #f9b11f;
  --lk-connection-poor: #f91f31;
  ...

```

## Use of HTML custom data attributes in LiveKit Components

[Custom data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes) are an easy way to store additional information on standard HTML elements. We use data attributes on many elements to show what state the component is in, or to provide additional information that can be used for styling.

> 💡 **Tip**
> 
> All data attributes in LiveKit Components start with `data-lk-`

For example, the `ConnectionQualityIndicator` shows the connection quality of a participant. The component renders an HTML div element and we add the custom data attribute `data-lk-quality` to it. The value of the custom data attribute is updated according to the current connection quality and can take the values "unknown", "poor", "good" and "excellent".

```tsx
// Participant with an excellent connection.
<div data-lk-quality="excellent">
  {/* ... */}
</div>

// Participant with a poor connection.
<div data-lk-quality="poor">
  {/* ... */}
</div>

```

The data attributes are simple HTML attributes, so we can access them via CSS. For example, to update the ConnectionQualityIndicator background, we can use the attribute selector to change the styles according to the value of the data attribute:

```css
[data-lk-quality='excellent'] {
  background-color: green;
}
[data-lk-quality='poor'] {
  background-color: red;
}

```

> 💡 **Tip**
> 
> Currently it is not documented which data attribute is used for which component. At the moment it is best to open the inspector and check which data attribute is used.

---

This document was rendered at 2026-08-28T04:22:14.349Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/concepts/style-components.md](https://docs.livekit.io/reference/components/react/concepts/style-components.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-33"></a>
## Page 33: reference/components/react/concepts/rendering-video
**Original URL:** https://docs.livekit.io/reference/components/react/concepts/rendering-video  
**Source MD URL:** https://docs.livekit.io/reference/components/react/concepts/rendering-video.md

LiveKit docs › React components › Concepts › Rendering video tracks

---

# Rendering a single track

To demonstrate how to build a UI to render a single video stream, imagine this scenario:

We have a LiveKit Room with three Participants who are constantly streaming a camera feed into the room. In our example, the Participants are not human, but webcams streaming from "Berlin", "New York" and "Tokyo". For unknown reasons, we only want to see the stream from "Tokyo".

We start by creating a new React component and get all the camera tracks with `useTracks([Track.Source.Camera])`. In the returned array of `TrackReferences` we look for the Tokyo stream. Since we know that all webcam participants are named after their cities, we look for the `tokyo` participant.

```tsx
import { useTracks } from '@livekit/components-react';
import { Track } from 'livekit-client';

function CityVideoRenderer() {
  const trackRefs = useTracks([Track.Source.Camera]);
  const tokyoCamTrackRef = trackRefs.find((trackRef) => trackRef.participant.name === 'tokyo');

  return <>TODO</>;
}

```

Now that we have found the correct stream, we can move on to building the UI to display it. We can do this by importing the `VideoTrack` component and passing it the track reference. If the Tokyo track reference is not found, we will display a UI to indicate this instead.

```tsx
import { useTracks, VideoTrack } from '@livekit/components-react';
import { Track } from 'livekit-client';

function CityVideoRenderer() {
  const trackRefs = useTracks([Track.Source.Camera]);
  const tokyoCamTrackRef = trackRefs.find((trackRef) => trackRef.participant.name === 'tokyo');

  return (
    <>
      {tokyoCamTrackRef ? <VideoTrack trackRef={tokyoCamTrackRef} /> : <div>Tokyo is offline</div>}
    </>
  );
}

```

With our UI in place, we need to provide useTracks with the proper context to return the tracks of a LiveKit Room. We do this by nesting everything inside the `<LiveKitRoom>` component.

```tsx
import { LiveKitRoom, useTracks, VideoTrack } from '@livekit/components-react';
import { Track } from 'livekit-client';

function CityVideoRenderer() {
  const trackRefs = useTracks([Track.Source.Camera]);
  const tokyoCamTrackRef = trackRefs.find((trackRef) => trackRef.participant.name === 'tokyo');

  return (
    <>
      {tokyoCamTrackRef ? <VideoTrack trackRef={tokyoCamTrackRef} /> : <div>Tokyo is offline</div>}
    </>
  );
}

function MyPage() {
  return (
    <LiveKitRoom>
      <CityVideoRenderer />
    </LiveKitRoom>
  );
}

```

---

This document was rendered at 2026-08-28T04:22:14.355Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/concepts/rendering-video.md](https://docs.livekit.io/reference/components/react/concepts/rendering-video.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-34"></a>
## Page 34: reference/components/react/concepts/rendering-audio
**Original URL:** https://docs.livekit.io/reference/components/react/concepts/rendering-audio  
**Source MD URL:** https://docs.livekit.io/reference/components/react/concepts/rendering-audio.md

LiveKit docs › React components › Concepts › Rendering audio tracks

---

# Audio rendering with React Components

> Different ways to render audio with React Components

There are two primary methods for rendering (making audio tracks audible) audio with React Components, each offering distinct benefits and suited for different use cases.

## Render all audio tracks within the room

The [`RoomAudioRenderer`](https://docs.livekit.io/reference/components/react/component/roomaudiorenderer.md) component simplifies audio management in LiveKit Rooms by rendering all audio tracks together. It's a straightforward and often optimal solution. Just import `RoomAudioRenderer` and place it in your `LiveKitRoom` component for seamless audio integration.

```tsx
<LiveKitRoom audio={true} video={true} token={token}>
  <RoomAudioRenderer />
</LiveKitRoom>

```

> 💡 **Tip**
> 
> Utilizing the `RoomAudioRenderer` ensures automatic benefits from future server-side performance enhancements without requiring any modifications to your existing code.

## Full control and ownership of the audio rendering process

For complete control over individual audio Tracks, including muting and volume adjustments at the track level, you can craft a custom audio renderer using the [`useTracks`](https://docs.livekit.io/reference/components/react/hook/usetracks.md) hook alongside the [`<AudioTrack/>`](https://docs.livekit.io/reference/components/react/component/audiotrack.md) component. For example, this level of control can be used to create spatial audio applications where you may want to adjust each audio track based on the distance between participants.

```js
  const tracks = useTracks([
    Track.Source.Microphone,
    Track.Source.ScreenShareAudio,
    Track.Source.Unknown,
  ]).filter((ref) => !isLocal(ref.participant) && ref.publication.kind === Track.Kind.Audio);

  return (
    <div style={{ display: 'none' }}>
      {tracks.map((trackRef) => (
        <AudioTrack
          key={getTrackReferenceId(trackRef)}
          trackRef={trackRef}
          volume={volume}
          muted={muted}
        />
      ))}
    </div>
  );

```

Depending on your application it is possible that audio tracks have an unknown source. To render these as well, we include the `Track.Source.Unknown` in the array of sources passed to the `useTracks` hook, but then filter out the tracks that are not of kind `Audio`.

---

This document was rendered at 2026-08-28T04:22:14.366Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/concepts/rendering-audio.md](https://docs.livekit.io/reference/components/react/concepts/rendering-audio.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-35"></a>
## Page 35: reference/components/react/hook/useagent
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useagent  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useagent.md

LiveKit docs › React components › Hooks › useAgent

---

# useAgent

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

useAgent encapculates all agent state, normalizing some quirks around how LiveKit Agents work.

## Import

```typescript
import { useAgent } from "@livekit/components-react";

```

## Properties

- **`session`** _(SessionStub)_ (optional): 

## Returns

```typescript
UseAgentReturn;

```

---

This document was rendered at 2026-08-28T04:22:14.357Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useagent.md](https://docs.livekit.io/reference/components/react/hook/useagent.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-36"></a>
## Page 36: reference/components/react/hook/useagentexpression
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useagentexpression  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useagentexpression.md

LiveKit docs › React components › Hooks › useAgentExpression

---

# useAgentExpression

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

useAgentExpression returns the agent's current emotional delivery, as published by Expressive Mode.

Reads the transcript stream the session already subscribes to, so it adds no second text stream handler. The mood decays back to null after `ttlTurns` agent turns without a new expression, so a feeling doesn't outlive the moment that produced it.

## Import

```typescript
import { useAgentExpression } from "@livekit/components-react";

```

## Usage

```tsx
const { mood, expression } = useAgentExpression();
return <span title={expression ?? undefined}>{mood ?? "neutral"}</span>;

```

## Properties

- **`opts.ttlTurns`** _(number)_ (optional): Agent turns an expression survives before the mood decays to null. `0` disables decay.

## Returns

```typescript
UseAgentExpressionReturn;

```

---

This document was rendered at 2026-08-28T04:22:14.361Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useagentexpression.md](https://docs.livekit.io/reference/components/react/hook/useagentexpression.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-37"></a>
## Page 37: reference/components/react/hook/useaudioplayback
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useaudioplayback  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useaudioplayback.md

LiveKit docs › React components › Hooks › useAudioPlayback

---

# useAudioPlayback

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

In many browsers to start audio playback, the user must perform a user-initiated event such as clicking a button. The `useAudioPlayback` hook returns an object with a boolean `canPlayAudio` flag that indicates whether audio playback is allowed in the current context, as well as a `startAudio` function that can be called in a button `onClick` callback to start audio playback in the current context.

## Import

```typescript
import { useAudioPlayback } from "@livekit/components-react";

```

## Properties

- **`room`** _(Room)_ (optional): 

## Returns

```typescript
{
  canPlayAudio: boolean;
  startAudio: () => Promise<void>;
}

```

---

This document was rendered at 2026-08-28T04:22:14.420Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useaudioplayback.md](https://docs.livekit.io/reference/components/react/hook/useaudioplayback.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-38"></a>
## Page 38: reference/components/react/hook/useaudiowaveform
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useaudiowaveform  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useaudiowaveform.md

LiveKit docs › React components › Hooks › useAudioWaveform

---

# useAudioWaveform

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

## Import

```typescript
import { useAudioWaveform } from "@livekit/components-react";

```

## Properties

- **`options.barCount`** _(number)_ (optional): 

- **`options.updateInterval`** _(number)_ (optional): 

- **`options.volMultiplier`** _(number)_ (optional): 

- **`trackOrTrackReference`** _(LocalAudioTrack | RemoteAudioTrack | TrackReferenceOrPlaceholder)_ (optional): 

## Returns

```typescript
{
    bars: number[];
}

```

---

This document was rendered at 2026-08-28T04:22:14.419Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useaudiowaveform.md](https://docs.livekit.io/reference/components/react/hook/useaudiowaveform.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-39"></a>
## Page 39: reference/components/react/hook/usechat
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usechat  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usechat.md

LiveKit docs › React components › Hooks › useChat

---

# useChat

The `useChat` hook provides chat functionality for a LiveKit room.

## Import

```typescript
import { useChat } from "@livekit/components-react";

```

## Remarks

Message history is not persisted and will be lost if the component is refreshed. You may want to persist message history in the browser, a cache or a database.

## Usage

```tsx
function ChatComponent() {
  const { chatMessages, send, isSending } = useChat();

  return (
    <div>
      {chatMessages.map((msg) => (
        <div key={msg.timestamp}>
          {msg.from?.identity}: {msg.message}
        </div>
      ))}
      <button disabled={isSending} onClick={() => send("Hello!")}>
        Send Message
      </button>
    </div>
  );
}

```

## Returns

An object containing: - `chatMessages` - Array of received chat messages - `send` - Function to send a new message - `isSending` - Boolean indicating if a message is currently being sent

```typescript
{
    send: (message: string, options?: import('livekit-client').SendTextOptions) => Promise<ReceivedChatMessage>;
    chatMessages: ReceivedChatMessage[];
    isSending: boolean;
}

```

---

This document was rendered at 2026-08-28T04:22:14.425Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usechat.md](https://docs.livekit.io/reference/components/react/hook/usechat.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-40"></a>
## Page 40: reference/components/react/hook/usechattoggle
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usechattoggle  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usechattoggle.md

LiveKit docs › React components › Hooks › useChatToggle

---

# useChatToggle

The `useChatToggle` hook provides state and functions for toggling the chat window.

## Import

```typescript
import { useChatToggle } from "@livekit/components-react";

```

## Remarks

Depends on the `LayoutContext` to work properly.

## Properties

- **`input.props`** _(React.ButtonHTMLAttributes<HTMLButtonElement>)_: 

## Returns

```typescript
{
    mergedProps: React.ButtonHTMLAttributes<HTMLButtonElement> & {
        className: string;
        onClick: () => void;
        'aria-pressed': string;
        'data-lk-unread-msgs': string;
    };
}

```

---

This document was rendered at 2026-08-28T04:22:14.449Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usechattoggle.md](https://docs.livekit.io/reference/components/react/hook/usechattoggle.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-41"></a>
## Page 41: reference/components/react/hook/useclearpinbutton
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useclearpinbutton  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useclearpinbutton.md

LiveKit docs › React components › Hooks › useClearPinButton

---

# useClearPinButton

The `useClearPinButton` hook provides props for the [ClearPinButton()](https://docs.livekit.io/react/component/clearpinbutton.md) or your custom implementation of it component. It adds the `onClick` handler to signal the `LayoutContext` that the tile in focus should be cleared.

## Import

```typescript
import { useClearPinButton } from "@livekit/components-react";

```

## Returns

```typescript
{
    buttonProps: ClearPinButtonProps & {
        className: string;
        disabled: boolean;
        onClick: () => void;
    };
}

```

---

This document was rendered at 2026-08-28T04:22:14.439Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useclearpinbutton.md](https://docs.livekit.io/reference/components/react/hook/useclearpinbutton.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-42"></a>
## Page 42: reference/components/react/hook/useconnectionqualityindicator
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useconnectionqualityindicator  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useconnectionqualityindicator.md

LiveKit docs › React components › Hooks › useConnectionQualityIndicator

---

# useConnectionQualityIndicator

The `useConnectionQualityIndicator` hook provides props for the `ConnectionQualityIndicator` or your custom implementation of it component.

## Import

```typescript
import { useConnectionQualityIndicator } from "@livekit/components-react";

```

## Usage

```tsx
const { quality } = useConnectionQualityIndicator();
// or
const { quality } = useConnectionQualityIndicator({ participant });

```

## Properties

- **`options.participant`** _(Participant)_ (optional): 

## Returns

```typescript
{
  className: "lk-connection-quality";
  quality: import("livekit-client").ConnectionQuality;
}

```

---

This document was rendered at 2026-08-28T04:22:14.443Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useconnectionqualityindicator.md](https://docs.livekit.io/reference/components/react/hook/useconnectionqualityindicator.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-43"></a>
## Page 43: reference/components/react/hook/useconnectionstate
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useconnectionstate  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useconnectionstate.md

LiveKit docs › React components › Hooks › useConnectionState

---

# useConnectionState

The `useConnectionState` hook allows you to simply implement your own `ConnectionState` component.

## Import

```typescript
import { useConnectionState } from "@livekit/components-react";

```

## Usage

```tsx
const connectionState = useConnectionState(room);

```

## Properties

- **`room`** _(Room)_ (optional): 

## Returns

```typescript
import("livekit-client").ConnectionState;

```

---

This document was rendered at 2026-08-28T04:22:14.443Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useconnectionstate.md](https://docs.livekit.io/reference/components/react/hook/useconnectionstate.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-44"></a>
## Page 44: reference/components/react/hook/usecreatelayoutcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usecreatelayoutcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usecreatelayoutcontext.md

LiveKit docs › React components › Hooks › useCreateLayoutContext

---

# useCreateLayoutContext

## Import

```typescript
import { useCreateLayoutContext } from "@livekit/components-react";

```

## Returns

```typescript
LayoutContextType;

```

---

This document was rendered at 2026-08-28T04:22:14.549Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usecreatelayoutcontext.md](https://docs.livekit.io/reference/components/react/hook/usecreatelayoutcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-45"></a>
## Page 45: reference/components/react/hook/usedatachannel
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usedatachannel  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usedatachannel.md

LiveKit docs › React components › Hooks › useDataChannel

---

# useDataChannel

The `useDataChannel` hook returns the ability to send and receive messages. Pass an optional `topic` to narrow down which messages are returned in the messages array.

## Import

```typescript
import { useDataChannel } from "@livekit/components-react";

```

## Remarks

There is only one data channel. Passing a `topic` does not open a new data channel. It is only used to filter out messages with no or a different `topic`.

## Usage

### Example 1

```tsx
// Send messages to all participants via the 'chat' topic.
const { message: latestMessage, send } = useDataChannel("chat", (msg) =>
  console.log("message received", msg)
);

```

### Example 2

```tsx
// Receive all messages (no topic filtering)
const { message: latestMessage, send } = useDataChannel((msg) =>
  console.log("message received", msg)
);

```

## Properties

- **`topic`** _(T)_: 

- **`onMessage`** _((msg: ReceivedDataMessage<T>) => void)_ (optional): 

## Returns

```typescript
UseDataChannelReturnType<T>;

```

---

This document was rendered at 2026-08-28T04:22:14.461Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usedatachannel.md](https://docs.livekit.io/reference/components/react/hook/usedatachannel.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-46"></a>
## Page 46: reference/components/react/hook/usedisconnectbutton
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usedisconnectbutton  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usedisconnectbutton.md

LiveKit docs › React components › Hooks › useDisconnectButton

---

# useDisconnectButton

The `useDisconnectButton` hook is used to implement the `DisconnectButton` or your custom implementation of it. It adds onClick handler to the button to disconnect from the room.

## Import

```typescript
import { useDisconnectButton } from "@livekit/components-react";

```

## Usage

```tsx
const { buttonProps } = useDisconnectButton(buttonProps);
return <button {...buttonProps}>Disconnect</button>;

```

## Properties

- **`props.stopTracks`** _(boolean)_ (optional): 

## Returns

```typescript
{
    buttonProps: DisconnectButtonProps & {
        className: string;
        onClick: () => void;
        disabled: boolean;
    };
}

```

---

This document was rendered at 2026-08-28T04:22:14.477Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usedisconnectbutton.md](https://docs.livekit.io/reference/components/react/hook/usedisconnectbutton.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-47"></a>
## Page 47: reference/components/react/hook/useensurecreatelayoutcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useensurecreatelayoutcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useensurecreatelayoutcontext.md

LiveKit docs › React components › Hooks › useEnsureCreateLayoutContext

---

# useEnsureCreateLayoutContext

## Import

```typescript
import { useEnsureCreateLayoutContext } from "@livekit/components-react";

```

## Properties

- **`layoutContext`** _(LayoutContextType)_ (optional): 

## Returns

```typescript
LayoutContextType;

```

---

This document was rendered at 2026-08-28T04:22:14.479Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useensurecreatelayoutcontext.md](https://docs.livekit.io/reference/components/react/hook/useensurecreatelayoutcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-48"></a>
## Page 48: reference/components/react/hook/useensurelayoutcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useensurelayoutcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useensurelayoutcontext.md

LiveKit docs › React components › Hooks › useEnsureLayoutContext

---

# useEnsureLayoutContext

Ensures that a layout context is provided, either via context or explicitly as a parameter. If not inside a `LayoutContext` and no layout context is provided, an error is thrown.

## Import

```typescript
import { useEnsureLayoutContext } from "@livekit/components-react";

```

## Properties

- **`layoutContext`** _(LayoutContextType)_ (optional): 

## Returns

```typescript
LayoutContextType;

```

---

This document was rendered at 2026-08-28T04:22:14.510Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useensurelayoutcontext.md](https://docs.livekit.io/reference/components/react/hook/useensurelayoutcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-49"></a>
## Page 49: reference/components/react/hook/useensureparticipant
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useensureparticipant  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useensureparticipant.md

LiveKit docs › React components › Hooks › useEnsureParticipant

---

# useEnsureParticipant

Ensures that a participant is provided, either via context or explicitly as a parameter. If not inside a `ParticipantContext` and no participant is provided, an error is thrown.

## Import

```typescript
import { useEnsureParticipant } from "@livekit/components-react";

```

## Properties

- **`participant`** _(Participant)_ (optional): 

## Returns

```typescript
Participant;

```

---

This document was rendered at 2026-08-28T04:22:14.551Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useensureparticipant.md](https://docs.livekit.io/reference/components/react/hook/useensureparticipant.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-50"></a>
## Page 50: reference/components/react/hook/useensureroom
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useensureroom  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useensureroom.md

LiveKit docs › React components › Hooks › useEnsureRoom

---

# useEnsureRoom

Ensures that a room is provided, either via context or explicitly as a parameter. If no room is provided, an error is thrown.

## Import

```typescript
import { useEnsureRoom } from "@livekit/components-react";

```

## Properties

- **`room`** _(Room)_ (optional): 

## Returns

```typescript
Room;

```

---

This document was rendered at 2026-08-28T04:22:14.551Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useensureroom.md](https://docs.livekit.io/reference/components/react/hook/useensureroom.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-51"></a>
## Page 51: reference/components/react/hook/useensuresession
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useensuresession  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useensuresession.md

LiveKit docs › React components › Hooks › useEnsureSession

---

# useEnsureSession

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

Ensures that a session is provided, either via context or explicitly as a parameter. If no session is provided, an error is thrown.

## Import

```typescript
import { useEnsureSession } from "@livekit/components-react";

```

## Properties

- **`session`** _(UseSessionReturn)_ (optional): 

## Returns

```typescript
UseSessionReturn;

```

---

This document was rendered at 2026-08-28T04:22:14.554Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useensuresession.md](https://docs.livekit.io/reference/components/react/hook/useensuresession.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-52"></a>
## Page 52: reference/components/react/hook/useensuretrackref
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useensuretrackref  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useensuretrackref.md

LiveKit docs › React components › Hooks › useEnsureTrackRef

---

# useEnsureTrackRef

Ensures that a track reference is provided, either via context or explicitly as a parameter. If not inside a `TrackRefContext` and no track reference is provided, an error is thrown.

## Import

```typescript
import { useEnsureTrackRef } from "@livekit/components-react";

```

## Properties

- **`trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): 

## Returns

```typescript
TrackReferenceOrPlaceholder;

```

---

This document was rendered at 2026-08-28T04:22:14.626Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useensuretrackref.md](https://docs.livekit.io/reference/components/react/hook/useensuretrackref.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-53"></a>
## Page 53: reference/components/react/hook/useevents
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useevents  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useevents.md

LiveKit docs › React components › Hooks › useEvents

---

# useEvents

## Import

```typescript
import { useEvents } from "@livekit/components-react";

```

## Properties

- **`event`** _(Event)_: 

- **`handlerFn`** _(Callback | undefined)_: 

- **`undefined`** _(undefined)_: 

- **`dependencies`** _(React.DependencyList)_ (optional): 

## Returns

```typescript
void

```

---

This document was rendered at 2026-08-28T04:22:14.562Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useevents.md](https://docs.livekit.io/reference/components/react/hook/useevents.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-54"></a>
## Page 54: reference/components/react/hook/usefacingmode
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usefacingmode  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usefacingmode.md

LiveKit docs › React components › Hooks › useFacingMode

---

# useFacingMode

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

Try to determine the `facingMode` of a local participant video track.

## Import

```typescript
import { useFacingMode } from "@livekit/components-react";

```

## Remarks

Works only on local video tracks.

## Properties

- **`trackReference`** _(TrackReferenceOrPlaceholder)_: 

## Returns

```typescript
"user" | "environment" | "left" | "right" | "undefined";

```

---

This document was rendered at 2026-08-28T04:22:14.588Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usefacingmode.md](https://docs.livekit.io/reference/components/react/hook/usefacingmode.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-55"></a>
## Page 55: reference/components/react/hook/usefocustoggle
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usefocustoggle  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usefocustoggle.md

LiveKit docs › React components › Hooks › useFocusToggle

---

# useFocusToggle

The `useFocusToggle` hook is used to implement the `FocusToggle` or your custom implementation of it. The `TrackReferenceOrPlaceholder` is used to register a onClick handler and to identify the track to focus on.

## Import

```typescript
import { useFocusToggle } from "@livekit/components-react";

```

## Usage

```tsx
const { mergedProps, inFocus } = useFocusToggle({ trackRef, props: yourButtonProps });
return <button {...mergedProps}>{inFocus ? "Unfocus" : "Focus"}</button>;

```

## Properties

- **`input.props`** _(React.ButtonHTMLAttributes<HTMLButtonElement>)_: 

- **`input.trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): 

## Returns

```typescript
{
    mergedProps: React.ButtonHTMLAttributes<HTMLButtonElement> & {
        className: string;
        onClick: (event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => void;
    };
    inFocus: boolean;
}

```

---

This document was rendered at 2026-08-28T04:22:14.577Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usefocustoggle.md](https://docs.livekit.io/reference/components/react/hook/usefocustoggle.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-56"></a>
## Page 56: reference/components/react/hook/usegridlayout
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usegridlayout  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usegridlayout.md

LiveKit docs › React components › Hooks › useGridLayout

---

# useGridLayout

The `useGridLayout` hook tries to select the best layout to fit all tiles. If the available screen space is not enough, it will reduce the number of maximum visible tiles and select a layout that still works visually within the given limitations. As the order of tiles changes over time, the hook tries to keep visual updates to a minimum while trying to display important tiles such as speaking participants or screen shares.

## Import

```typescript
import { useGridLayout } from "@livekit/components-react";

```

## Usage

```tsx
const { layout } = useGridLayout(gridElement, trackCount);

```

## Properties

- **`gridElement`** _(React.RefObject<HTMLDivElement>)_: 

- **`trackCount`** _(number)_: 

- **`undefined`** _(undefined)_: 

## Returns

```typescript
{
  layout: GridLayoutInfo;
  containerWidth: number;
  containerHeight: number;
}

```

---

This document was rendered at 2026-08-28T04:22:14.587Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usegridlayout.md](https://docs.livekit.io/reference/components/react/hook/usegridlayout.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-57"></a>
## Page 57: reference/components/react/hook/useisencrypted
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useisencrypted  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useisencrypted.md

LiveKit docs › React components › Hooks › useIsEncrypted

---

# useIsEncrypted

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

## Import

```typescript
import { useIsEncrypted } from "@livekit/components-react";

```

## Properties

- **`options.room`** _(Room)_ (optional): 

- **`participant`** _(Participant)_ (optional): 

## Returns

```typescript
boolean;

```

---

This document was rendered at 2026-08-28T04:22:14.580Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useisencrypted.md](https://docs.livekit.io/reference/components/react/hook/useisencrypted.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-58"></a>
## Page 58: reference/components/react/hook/useismuted
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useismuted  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useismuted.md

LiveKit docs › React components › Hooks › useIsMuted

---

# useIsMuted

The `useIsMuted` hook is used to implement the `TrackMutedIndicator` or your custom implementation of it. It returns a `boolean` that indicates if the track is muted or not.

## Import

```typescript
import { useIsMuted } from "@livekit/components-react";

```

## Usage

With a track reference

```tsx
const isMuted = useIsMuted(track);

```

## Properties

- **`trackRef`** _(TrackReferenceOrPlaceholder)_: A `TrackReference` indicating the track to monitor.

## Returns

boolean indicating if the track is muted

```typescript
boolean;

```

---

This document was rendered at 2026-08-28T04:22:14.593Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useismuted.md](https://docs.livekit.io/reference/components/react/hook/useismuted.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-59"></a>
## Page 59: reference/components/react/hook/useisrecording
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useisrecording  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useisrecording.md

LiveKit docs › React components › Hooks › useIsRecording

---

# useIsRecording

The `useIsRecording` hook returns a `boolean` that indicates if the room is currently being recorded.

## Import

```typescript
import { useIsRecording } from "@livekit/components-react";

```

## Usage

```tsx
const isRecording = useIsRecording();

```

## Properties

- **`room`** _(Room)_ (optional): 

## Returns

```typescript
boolean;

```

---

This document was rendered at 2026-08-28T04:22:14.615Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useisrecording.md](https://docs.livekit.io/reference/components/react/hook/useisrecording.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-60"></a>
## Page 60: reference/components/react/hook/useisspeaking
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useisspeaking  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useisspeaking.md

LiveKit docs › React components › Hooks › useIsSpeaking

---

# useIsSpeaking

The `useIsSpeaking` hook returns a `boolean` that indicates if the participant is speaking or not.

## Import

```typescript
import { useIsSpeaking } from "@livekit/components-react";

```

## Usage

```tsx
const isSpeaking = useIsSpeaking(participant);

```

## Properties

- **`participant`** _(Participant)_ (optional): 

## Returns

```typescript
boolean;

```

---

This document was rendered at 2026-08-28T04:22:14.598Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useisspeaking.md](https://docs.livekit.io/reference/components/react/hook/useisspeaking.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-61"></a>
## Page 61: reference/components/react/hook/usekrispnoisefilter
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usekrispnoisefilter  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usekrispnoisefilter.md

LiveKit docs › React components › Hooks › useKrispNoiseFilter

---

# useKrispNoiseFilter

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

Enable the Krisp enhanced noise cancellation feature for local audio tracks.

Defaults to the localParticipant's microphone track publication, but you can override this behavior by passing in a different track reference.

## Import

```typescript
import { useKrispNoiseFilter } from "@livekit/components-react/krisp";

```

## Remarks

This filter requires that you install the `@livekit/krisp-noise-filter` package and is supported only on [LiveKit Cloud](https://cloud.livekit.io).

## Usage

```tsx
const krisp = useKrispNoiseFilter();
return (
  <input
    type="checkbox"
    onChange={(ev) => krisp.setNoiseFilterEnabled(ev.target.checked)}
    checked={krisp.isNoiseFilterEnabled}
    disabled={krisp.isNoiseFilterPending}
  />
);

```

## Properties

- **`options.trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): The track reference to use for the noise filter (defaults: local microphone track)

## Returns

Use `setIsNoiseFilterEnabled` to enable/disable the noise filter.

```typescript
{
  setNoiseFilterEnabled: (enable: boolean) => Promise<void>;
  isNoiseFilterEnabled: boolean;
  isNoiseFilterPending: boolean;
  processor: KrispNoiseFilterProcessor | undefined;
}

```

---

This document was rendered at 2026-08-28T04:22:14.611Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usekrispnoisefilter.md](https://docs.livekit.io/reference/components/react/hook/usekrispnoisefilter.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-62"></a>
## Page 62: reference/components/react/hook/uselayoutcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/uselayoutcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/uselayoutcontext.md

LiveKit docs › React components › Hooks › useLayoutContext

---

# useLayoutContext

Ensures that a layout context is provided via context. If no layout context is provided, an error is thrown.

## Import

```typescript
import { useLayoutContext } from "@livekit/components-react";

```

## Returns

```typescript
LayoutContextType;

```

---

This document was rendered at 2026-08-28T04:22:14.609Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/uselayoutcontext.md](https://docs.livekit.io/reference/components/react/hook/uselayoutcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-63"></a>
## Page 63: reference/components/react/hook/uselivekitroom
**Original URL:** https://docs.livekit.io/reference/components/react/hook/uselivekitroom  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/uselivekitroom.md

LiveKit docs › React components › Hooks › useLiveKitRoom

---

# useLiveKitRoom

The `useLiveKitRoom` hook is used to implement the `LiveKitRoom` or your custom implementation of it. It returns a `Room` instance and HTML props that should be applied to the root element of the component.

## Import

```typescript
import { useLiveKitRoom } from "@livekit/components-react";

```

## Usage

```tsx
const { room, htmlProps } = useLiveKitRoom();
return <div {...htmlProps}>...</div>;

```

## Properties

- **`props.serverUrl`** _(string | undefined)_: URL to the LiveKit server. For example: `wss://<domain>.livekit.cloud` To simplify the implementation, `undefined` is also accepted as an intermediate value, but only with a valid string url can the connection be established.

- **`props.token`** _(string | undefined)_: A user specific access token for a client to authenticate to the room. This token is necessary to establish a connection to the room. To simplify the implementation, `undefined` is also accepted as an intermediate value, but only with a valid string token can the connection be established.

- **`props.audio`** _(AudioCaptureOptions | boolean)_ (optional): Publish audio immediately after connecting to your LiveKit room.

- **`props.connect`** _(boolean)_ (optional): If set to true a connection to LiveKit room is initiated.

- **`props.connectOptions`** _(RoomConnectOptions)_ (optional): Define options how to connect to the LiveKit server.

- **`props.onConnected`** _(() => void)_ (optional): 

- **`props.onDisconnected`** _((reason?: DisconnectReason) => void)_ (optional): 

- **`props.onEncryptionError`** _((error: Error) => void)_ (optional): 

- **`props.onError`** _((error: Error) => void)_ (optional): 

- **`props.onMediaDeviceFailure`** _((failure?: MediaDeviceFailure, kind?: MediaDeviceKind) => void)_ (optional): 

- **`props.options`** _(RoomOptions)_ (optional): Options for when creating a new room. When you pass your own room instance to this component, these options have no effect. Instead, set the options directly in the room instance.

- **`props.room`** _(Room)_ (optional): Optional room instance. By passing your own room instance you overwrite the `options` parameter, make sure to set the options directly on the room instance itself.

- **`props.screen`** _(ScreenShareCaptureOptions | boolean)_ (optional): Publish screen share immediately after connecting to your LiveKit room.

- **`props.simulateParticipants`** _(number | undefined)_ (optional): 

- **`props.video`** _(VideoCaptureOptions | boolean)_ (optional): Publish video immediately after connecting to your LiveKit room.

## Returns

```typescript
{
  room: Room | undefined;
  htmlProps: HTMLAttributes<T>;
}

```

---

This document was rendered at 2026-08-28T04:22:14.610Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/uselivekitroom.md](https://docs.livekit.io/reference/components/react/hook/uselivekitroom.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-64"></a>
## Page 64: reference/components/react/hook/uselocalparticipant
**Original URL:** https://docs.livekit.io/reference/components/react/hook/uselocalparticipant  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/uselocalparticipant.md

LiveKit docs › React components › Hooks › useLocalParticipant

---

# useLocalParticipant

The `useLocalParticipant` hook returns the local participant and the associated state around the participant.

## Import

```typescript
import { useLocalParticipant } from "@livekit/components-react";

```

## Usage

```tsx
const { localParticipant } = useLocalParticipant();

```

## Properties

- **`options.room`** _(Room)_ (optional): The room to use. If not provided, the hook will use the room from the context.

## Returns

```typescript
{
  isMicrophoneEnabled: boolean;
  isScreenShareEnabled: boolean;
  isCameraEnabled: boolean;
  microphoneTrack: TrackPublication | undefined;
  cameraTrack: TrackPublication | undefined;
  lastMicrophoneError: Error | undefined;
  lastCameraError: Error | undefined;
  localParticipant: LocalParticipant;
}

```

---

This document was rendered at 2026-08-28T04:22:14.633Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/uselocalparticipant.md](https://docs.livekit.io/reference/components/react/hook/uselocalparticipant.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-65"></a>
## Page 65: reference/components/react/hook/uselocalparticipantpermissions
**Original URL:** https://docs.livekit.io/reference/components/react/hook/uselocalparticipantpermissions  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/uselocalparticipantpermissions.md

LiveKit docs › React components › Hooks › useLocalParticipantPermissions

---

# useLocalParticipantPermissions

The `useLocalParticipantPermissions` hook returns the local participant's permissions.

## Import

```typescript
import { useLocalParticipantPermissions } from "@livekit/components-react";

```

## Usage

```tsx
const { canPublish, canPublishData } = useLocalParticipantPermissions();

```

## Returns

```typescript
ParticipantPermission | undefined;

```

---

This document was rendered at 2026-08-28T04:22:14.652Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/uselocalparticipantpermissions.md](https://docs.livekit.io/reference/components/react/hook/uselocalparticipantpermissions.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-66"></a>
## Page 66: reference/components/react/hook/usemaybelayoutcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usemaybelayoutcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usemaybelayoutcontext.md

LiveKit docs › React components › Hooks › useMaybeLayoutContext

---

# useMaybeLayoutContext

Returns a layout context from the `LayoutContext` if it exists, otherwise `undefined`.

## Import

```typescript
import { useMaybeLayoutContext } from "@livekit/components-react";

```

## Returns

```typescript
LayoutContextType | undefined;

```

---

This document was rendered at 2026-08-28T04:22:14.676Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usemaybelayoutcontext.md](https://docs.livekit.io/reference/components/react/hook/usemaybelayoutcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-67"></a>
## Page 67: reference/components/react/hook/usemaybeparticipantcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usemaybeparticipantcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usemaybeparticipantcontext.md

LiveKit docs › React components › Hooks › useMaybeParticipantContext

---

# useMaybeParticipantContext

Returns a participant from the `ParticipantContext` if it exists, otherwise `undefined`.

## Import

```typescript
import { useMaybeParticipantContext } from "@livekit/components-react";

```

## Returns

```typescript
Participant | undefined;

```

---

This document was rendered at 2026-08-28T04:22:14.679Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usemaybeparticipantcontext.md](https://docs.livekit.io/reference/components/react/hook/usemaybeparticipantcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-68"></a>
## Page 68: reference/components/react/hook/usemayberoomcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usemayberoomcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usemayberoomcontext.md

LiveKit docs › React components › Hooks › useMaybeRoomContext

---

# useMaybeRoomContext

Returns the room context if it exists, otherwise undefined.

## Import

```typescript
import { useMaybeRoomContext } from "@livekit/components-react";

```

## Returns

```typescript
Room | undefined;

```

---

This document was rendered at 2026-08-28T04:22:14.695Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usemayberoomcontext.md](https://docs.livekit.io/reference/components/react/hook/usemayberoomcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-69"></a>
## Page 69: reference/components/react/hook/usemaybesessioncontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usemaybesessioncontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usemaybesessioncontext.md

LiveKit docs › React components › Hooks › useMaybeSessionContext

---

# useMaybeSessionContext

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

Returns the session context if it exists, otherwise undefined.

## Import

```typescript
import { useMaybeSessionContext } from "@livekit/components-react";

```

## Returns

```typescript
UseSessionReturn | undefined;

```

---

This document was rendered at 2026-08-28T04:22:14.719Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usemaybesessioncontext.md](https://docs.livekit.io/reference/components/react/hook/usemaybesessioncontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-70"></a>
## Page 70: reference/components/react/hook/usemaybetrackrefcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usemaybetrackrefcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usemaybetrackrefcontext.md

LiveKit docs › React components › Hooks › useMaybeTrackRefContext

---

# useMaybeTrackRefContext

Returns a track reference from the `TrackRefContext` if it exists, otherwise `undefined`.

## Import

```typescript
import { useMaybeTrackRefContext } from "@livekit/components-react";

```

## Returns

```typescript
TrackReferenceOrPlaceholder | undefined;

```

---

This document was rendered at 2026-08-28T04:22:14.701Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usemaybetrackrefcontext.md](https://docs.livekit.io/reference/components/react/hook/usemaybetrackrefcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-71"></a>
## Page 71: reference/components/react/hook/usemediadevices
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usemediadevices  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usemediadevices.md

LiveKit docs › React components › Hooks › useMediaDevices

---

# useMediaDevices

The `useMediaDevices` hook returns the list of media devices of a given kind.

## Import

```typescript
import { useMediaDevices } from "@livekit/components-react";

```

## Usage

```tsx
const videoDevices = useMediaDevices({ kind: "videoinput" });
const audioDevices = useMediaDevices({ kind: "audioinput" });

```

## Properties

- **`undefined`** _(undefined)_: 

## Returns

```typescript
MediaDeviceInfo[]

```

---

This document was rendered at 2026-08-28T04:22:14.738Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usemediadevices.md](https://docs.livekit.io/reference/components/react/hook/usemediadevices.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-72"></a>
## Page 72: reference/components/react/hook/usemediadeviceselect
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usemediadeviceselect  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usemediadeviceselect.md

LiveKit docs › React components › Hooks › useMediaDeviceSelect

---

# useMediaDeviceSelect

The `useMediaDeviceSelect` hook is used to implement the `MediaDeviceSelect` component and returns o.a. the list of devices of a given kind (audioinput or videoinput), the currently active device and a function to set the the active device.

## Import

```typescript
import { useMediaDeviceSelect } from "@livekit/components-react";

```

## Usage

```tsx
const { devices, activeDeviceId, setActiveMediaDevice } = useMediaDeviceSelect({
  kind: "audioinput"
});

```

## Properties

- **`input.kind`** _(MediaDeviceKind)_: 

- **`input.onError`** _((e: Error) => void)_ (optional): this callback gets called if an error is thrown when failing to select a device and also if a user denied permissions, eventhough the `requestPermissions` option is set to `true`. Most commonly this will emit a MediaDeviceError

- **`input.requestPermissions`** _(boolean)_ (optional): this will call getUserMedia if the permissions are not yet given to enumerate the devices with device labels. in some browsers multiple calls to getUserMedia result in multiple permission prompts. It's generally advised only flip this to true, once a (preview) track has been acquired successfully with the appropriate permissions.

- **`input.room`** _(Room)_ (optional): 

- **`input.track`** _(LocalAudioTrack | LocalVideoTrack)_ (optional): 

## Returns

```typescript
{
    devices: MediaDeviceInfo[];
    className: string;
    activeDeviceId: string;
    setActiveMediaDevice: (id: string, options?: import('@livekit/components-core').SetMediaDeviceOptions) => Promise<void>;
}

```

---

This document was rendered at 2026-08-28T04:22:14.716Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usemediadeviceselect.md](https://docs.livekit.io/reference/components/react/hook/usemediadeviceselect.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-73"></a>
## Page 73: reference/components/react/hook/usemultibandtrackvolume
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usemultibandtrackvolume  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usemultibandtrackvolume.md

LiveKit docs › React components › Hooks › useMultibandTrackVolume

---

# useMultibandTrackVolume

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

Hook for tracking the volume of an audio track across multiple frequency bands using the Web Audio API.

## Import

```typescript
import { useMultibandTrackVolume } from "@livekit/components-react";

```

## Properties

- **`options.analyserOptions`** _(AnalyserOptions)_ (optional): 

- **`options.bands`** _(number)_ (optional): 

- **`options.hiPass`** _(number)_ (optional): cut off of frequency bins on the higher end Note: this is not a frequency measure, but in relation to analyserOptions.fftSize,

- **`options.loPass`** _(number)_ (optional): cut off of frequency bins on the lower end Note: this is not a frequency measure, but in relation to analyserOptions.fftSize,

- **`options.updateInterval`** _(number)_ (optional): update should run every x ms

- **`trackOrTrackReference`** _(LocalAudioTrack | RemoteAudioTrack | TrackReferenceOrPlaceholder)_ (optional): 

## Returns

```typescript
number[]

```

---

This document was rendered at 2026-08-28T04:22:14.743Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usemultibandtrackvolume.md](https://docs.livekit.io/reference/components/react/hook/usemultibandtrackvolume.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-74"></a>
## Page 74: reference/components/react/hook/usepagination
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usepagination  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usepagination.md

LiveKit docs › React components › Hooks › usePagination

---

# usePagination

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

The `usePagination` hook implements simple pagination logic for use with arrays.

## Import

```typescript
import { usePagination } from "@livekit/components-react";

```

## Usage

```tsx
const tracks = useTracks();
const pagination = usePagination(4, tracks);

<TrackLoop tracks={pagination.tracks} />;

```

## Properties

- **`itemPerPage`** _(number)_: 

- **`trackReferences`** _(TrackReferenceOrPlaceholder[])_: 

## Returns

```typescript
{
    totalPageCount: number;
    nextPage: () => void;
    prevPage: () => void;
    setPage: (num: number) => void;
    firstItemIndex: number;
    lastItemIndex: number;
    tracks: TrackReferenceOrPlaceholder[];
    currentPage: number;
}

```

---

This document was rendered at 2026-08-28T04:22:14.744Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usepagination.md](https://docs.livekit.io/reference/components/react/hook/usepagination.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-75"></a>
## Page 75: reference/components/react/hook/useparticipantattribute
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantattribute  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantattribute.md

LiveKit docs › React components › Hooks › useParticipantAttribute

---

# useParticipantAttribute

The `useParticipantAttribute` hook returns the latest value of a given attribute key of a participant. It requires a `Participant` object passed as property in the `UseParticipantAttributesOptions` or via the `ParticipantContext`.

## Import

```typescript
import { useParticipantAttribute } from "@livekit/components-react";

```

## Usage

```tsx
const myAttributeValue = useParticipantAttribute("targetAttributeName");

```

## Properties

- **`attributeKey`** _(string)_: 

- **`options.participant`** _(Participant)_ (optional): 

## Returns

```typescript
string;

```

---

This document was rendered at 2026-08-28T04:22:14.743Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useparticipantattribute.md](https://docs.livekit.io/reference/components/react/hook/useparticipantattribute.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-76"></a>
## Page 76: reference/components/react/hook/useparticipantattributes
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantattributes  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantattributes.md

LiveKit docs › React components › Hooks › useParticipantAttributes

---

# useParticipantAttributes

## Import

```typescript
import { useParticipantAttributes } from "@livekit/components-react";

```

## Properties

- **`props.participant`** _(Participant)_ (optional): 

## Returns

```typescript
{
  attributes: Readonly<Record<string, string>> | undefined;
}

```

---

This document was rendered at 2026-08-28T04:22:14.796Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useparticipantattributes.md](https://docs.livekit.io/reference/components/react/hook/useparticipantattributes.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-77"></a>
## Page 77: reference/components/react/hook/useparticipantcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantcontext.md

LiveKit docs › React components › Hooks › useParticipantContext

---

# useParticipantContext

Ensures that a participant is provided via context. If not inside a `ParticipantContext`, an error is thrown.

## Import

```typescript
import { useParticipantContext } from "@livekit/components-react";

```

## Returns

```typescript
Participant;

```

---

This document was rendered at 2026-08-28T04:22:14.814Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useparticipantcontext.md](https://docs.livekit.io/reference/components/react/hook/useparticipantcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-78"></a>
## Page 78: reference/components/react/hook/useparticipantinfo
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantinfo  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantinfo.md

LiveKit docs › React components › Hooks › useParticipantInfo

---

# useParticipantInfo

## Import

```typescript
import { useParticipantInfo } from "@livekit/components-react";

```

## Properties

- **`props.participant`** _(Participant)_ (optional): 

## Returns

```typescript
{
  identity: string | undefined;
  name: string | undefined;
  metadata: string | undefined;
}

```

---

This document was rendered at 2026-08-28T04:22:14.817Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useparticipantinfo.md](https://docs.livekit.io/reference/components/react/hook/useparticipantinfo.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-79"></a>
## Page 79: reference/components/react/hook/useparticipantpermissions
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantpermissions  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useparticipantpermissions.md

LiveKit docs › React components › Hooks › useParticipantPermissions

---

# useParticipantPermissions

## Import

```typescript
import { useParticipantPermissions } from "@livekit/components-react";

```

## Properties

- **`options.participant`** _(Participant)_ (optional): 

## Returns

```typescript
ParticipantPermission | undefined;

```

---

This document was rendered at 2026-08-28T04:22:14.825Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useparticipantpermissions.md](https://docs.livekit.io/reference/components/react/hook/useparticipantpermissions.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-80"></a>
## Page 80: reference/components/react/hook/useparticipants
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useparticipants  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useparticipants.md

LiveKit docs › React components › Hooks › useParticipants

---

# useParticipants

The `useParticipants` hook returns all participants (local and remote) of the current room.

## Import

```typescript
import { useParticipants } from "@livekit/components-react";

```

## Remarks

To optimize performance, you can use the `updateOnlyOn` property to decide on what `RoomEvents` the hook updates.

## Usage

```tsx
const participants = useParticipants();
<ParticipantLoop participants={participants}>
  <ParticipantName />
</ParticipantLoop>;

```

## Properties

- **`options.room`** _(Room)_ (optional): The room to use. If not provided, the hook will use the room from the context.

- **`options.updateOnlyOn`** _(RoomEvent[])_ (optional): To optimize performance, you can use the `updateOnlyOn` property to decide on what RoomEvents the hook updates. By default it updates on all relevant RoomEvents to keep the returned participants array up to date. The minimal set of non-overwriteable `RoomEvents` is: `[RoomEvent.ParticipantConnected, RoomEvent.ParticipantDisconnected, RoomEvent.ConnectionStateChanged]`

## Returns

```typescript
(import('livekit-client').RemoteParticipant | import('livekit-client').LocalParticipant)[]

```

---

This document was rendered at 2026-08-28T04:22:14.829Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useparticipants.md](https://docs.livekit.io/reference/components/react/hook/useparticipants.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-81"></a>
## Page 81: reference/components/react/hook/useparticipanttile
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useparticipanttile  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useparticipanttile.md

LiveKit docs › React components › Hooks › useParticipantTile

---

# useParticipantTile

The `useParticipantTile` hook is used to implement the `ParticipantTile` and returns the props needed to render the tile.

## Import

```typescript
import { useParticipantTile } from "@livekit/components-react";

```

## Remarks

The returned props include many data attributes that are useful for CSS styling purposes because they indicate the state of the participant and the track. For example: `data-lk-audio-muted`, `data-lk-video-muted`, `data-lk-speaking`, `data-lk-local-participant`, `data-lk-source`, `data-lk-facing-mode`.

## Properties

- **`input.htmlProps`** _(React.HTMLAttributes<T>)_: 

- **`input.disableSpeakingIndicator`** _(boolean)_ (optional): 

- **`input.onParticipantClick`** _((event: ParticipantClickEvent) => void)_ (optional): 

- **`input.trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): The track reference to display.

## Returns

```typescript
{
  elementProps: React.HTMLAttributes<T>;
}

```

---

This document was rendered at 2026-08-28T04:22:14.827Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useparticipanttile.md](https://docs.livekit.io/reference/components/react/hook/useparticipanttile.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-82"></a>
## Page 82: reference/components/react/hook/useparticipanttracks
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useparticipanttracks  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useparticipanttracks.md

LiveKit docs › React components › Hooks › useParticipantTracks

---

# useParticipantTracks

`useParticipantTracks` is a custom React that allows you to get tracks of a specific participant only, by specifiying the participant's identity. If the participant identity is not passed the hook will try to get the participant from a participant context.

## Import

```typescript
import { useParticipantTracks } from "@livekit/components-react";

```

## Properties

- **`sources`** _(Array<TrackSource>)_: 

## Returns

```typescript
Array<TrackReference>;

```

---

This document was rendered at 2026-08-28T04:22:14.853Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useparticipanttracks.md](https://docs.livekit.io/reference/components/react/hook/useparticipanttracks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-83"></a>
## Page 83: reference/components/react/hook/usepersistentuserchoices
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usepersistentuserchoices  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usepersistentuserchoices.md

LiveKit docs › React components › Hooks › usePersistentUserChoices

---

# usePersistentUserChoices

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

A hook that provides access to user choices stored in local storage, such as selected media devices and their current state (on or off), as well as the user name.

## Import

```typescript
import { usePersistentUserChoices } from "@livekit/components-react";

```

## Properties

- **`options.defaults`** _(Partial<LocalUserChoices>)_ (optional): The default value to use if reading from local storage returns no results or fails.

- **`options.preventLoad`** _(boolean)_ (optional): Whether to prevent loading user choices from persistent storage and use `defaults` instead.

- **`options.preventSave`** _(boolean)_ (optional): Whether to prevent saving to persistent storage.

## Returns

```typescript
{
    userChoices: LocalUserChoices;
    saveAudioInputEnabled: (isEnabled: boolean) => void;
    saveVideoInputEnabled: (isEnabled: boolean) => void;
    saveAudioInputDeviceId: (deviceId: string) => void;
    saveVideoInputDeviceId: (deviceId: string) => void;
    saveUsername: (username: string) => void;
}

```

---

This document was rendered at 2026-08-28T04:22:14.856Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usepersistentuserchoices.md](https://docs.livekit.io/reference/components/react/hook/usepersistentuserchoices.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-84"></a>
## Page 84: reference/components/react/hook/usepinnedtracks
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usepinnedtracks  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usepinnedtracks.md

LiveKit docs › React components › Hooks › usePinnedTracks

---

# usePinnedTracks

The `usePinnedTracks` hook returns a array of the pinned tracks of the current room.

## Import

```typescript
import { usePinnedTracks } from "@livekit/components-react";

```

## Remarks

To function properly, this hook must be called within a `LayoutContext`.

## Usage

```tsx
const pinnedTracks = usePinnedTracks();

```

## Properties

- **`layoutContext`** _(LayoutContextType)_ (optional): 

## Returns

```typescript
TrackReferenceOrPlaceholder[]

```

---

This document was rendered at 2026-08-28T04:22:14.845Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usepinnedtracks.md](https://docs.livekit.io/reference/components/react/hook/usepinnedtracks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-85"></a>
## Page 85: reference/components/react/hook/usepreviewdevice
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usepreviewdevice  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usepreviewdevice.md

LiveKit docs › React components › Hooks › usePreviewDevice

---

# usePreviewDevice

> 🔥 **Caution**
> 
> This API is deprecated: use `usePreviewTracks` instead

## Import

```typescript
import { usePreviewDevice } from "@livekit/components-react";

```

## Properties

- **`deviceId`** _(string)_: 

- **`enabled`** _(boolean)_: 

- **`kind`** _('videoinput' | 'audioinput')_: 

## Returns

```typescript
{
  selectedDevice: MediaDeviceInfo | undefined;
  localTrack: T | undefined;
  deviceError: Error | null;
}

```

---

This document was rendered at 2026-08-28T04:22:14.864Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usepreviewdevice.md](https://docs.livekit.io/reference/components/react/hook/usepreviewdevice.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-86"></a>
## Page 86: reference/components/react/hook/usepreviewtracks
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usepreviewtracks  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usepreviewtracks.md

LiveKit docs › React components › Hooks › usePreviewTracks

---

# usePreviewTracks

## Import

```typescript
import { usePreviewTracks } from "@livekit/components-react";

```

## Properties

- **`onError`** _((err: Error) => void)_ (optional): 

## Returns

```typescript
(LocalAudioTrack | LocalVideoTrack)[] | undefined

```

---

This document was rendered at 2026-08-28T04:22:14.869Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usepreviewtracks.md](https://docs.livekit.io/reference/components/react/hook/usepreviewtracks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-87"></a>
## Page 87: reference/components/react/hook/useremoteparticipant
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useremoteparticipant  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useremoteparticipant.md

LiveKit docs › React components › Hooks › useRemoteParticipant

---

# useRemoteParticipant

The `useRemoteParticipant` hook returns the first RemoteParticipant by either identity and/or based on the participant kind.

## Import

```typescript
import { useRemoteParticipant } from "@livekit/components-react";

```

## Remarks

To optimize performance, you can use the `updateOnlyOn` property to decide on what `ParticipantEvents` the hook updates.

## Usage

```tsx
const participant = useRemoteParticipant({ kind: ParticipantKind.Agent, identity: "myAgent" });

```

## Properties

- **`identifier`** _(ParticipantIdentifier)_: 

- **`options.updateOnlyOn`** _(ParticipantEvent[])_ (optional): To optimize performance, you can use the `updateOnlyOn` property to decide on what `ParticipantEvents` the hook updates. By default it updates on all relevant ParticipantEvents to keep the returned participant up to date.

## Returns

```typescript
RemoteParticipant | undefined;

```

---

This document was rendered at 2026-08-28T04:22:14.865Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useremoteparticipant.md](https://docs.livekit.io/reference/components/react/hook/useremoteparticipant.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-88"></a>
## Page 88: reference/components/react/hook/useremoteparticipants
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useremoteparticipants  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useremoteparticipants.md

LiveKit docs › React components › Hooks › useRemoteParticipants

---

# useRemoteParticipants

The `useRemoteParticipants` hook returns all remote participants (without the local) of the current room.

## Import

```typescript
import { useRemoteParticipants } from "@livekit/components-react";

```

## Remarks

To optimize performance, you can use the `updateOnlyOn` property to decide on what `RoomEvents` the hook updates.

## Usage

```tsx
const participants = useRemoteParticipants();
<ParticipantLoop participants={participants}>
  <ParticipantName />
</ParticipantLoop>;

```

## Properties

- **`options.room`** _(Room)_ (optional): The room to use. If not provided, the hook will use the room from the context.

- **`options.updateOnlyOn`** _(RoomEvent[])_ (optional): To optimize performance, you can use the `updateOnlyOn` property to decide on what RoomEvents the hook updates. By default it updates on all relevant RoomEvents to keep the returned participants array up to date. The minimal set of non-overwriteable `RoomEvents` is: `[RoomEvent.ParticipantConnected, RoomEvent.ParticipantDisconnected, RoomEvent.ConnectionStateChanged]`

## Returns

```typescript
RemoteParticipant[]

```

---

This document was rendered at 2026-08-28T04:22:14.881Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useremoteparticipants.md](https://docs.livekit.io/reference/components/react/hook/useremoteparticipants.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-89"></a>
## Page 89: reference/components/react/hook/useroomcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useroomcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useroomcontext.md

LiveKit docs › React components › Hooks › useRoomContext

---

# useRoomContext

Ensures that a room is provided via context. If no room is provided, an error is thrown.

## Import

```typescript
import { useRoomContext } from "@livekit/components-react";

```

## Returns

```typescript
Room;

```

---

This document was rendered at 2026-08-28T04:22:14.888Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useroomcontext.md](https://docs.livekit.io/reference/components/react/hook/useroomcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-90"></a>
## Page 90: reference/components/react/hook/useroominfo
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useroominfo  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useroominfo.md

LiveKit docs › React components › Hooks › useRoomInfo

---

# useRoomInfo

## Import

```typescript
import { useRoomInfo } from "@livekit/components-react";

```

## Properties

- **`options.room`** _(Room)_ (optional): 

## Returns

```typescript
{
  name: string;
  metadata: string | undefined;
}

```

---

This document was rendered at 2026-08-28T04:22:14.921Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useroominfo.md](https://docs.livekit.io/reference/components/react/hook/useroominfo.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-91"></a>
## Page 91: reference/components/react/hook/userpc
**Original URL:** https://docs.livekit.io/reference/components/react/hook/userpc  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/userpc.md

LiveKit docs › React components › Hooks › useRpc

---

# useRpc

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

Hook for declarative RPC method registration and outbound RPC calls.

Registers a handler for an incoming RPC method and returns a `performRpc` function for outbound calls. The handler is registered on mount and unregistered on unmount. Handler identity does not matter (captured by ref), so inline functions work without `useCallback`.

## Import

```typescript
import { useRpc } from "@livekit/components-react";

```

## Usage

```tsx
const { performRpc } = useRpc(
  session,
  "getUserLocation",
  async (payload: { highAccuracy: boolean }) => {
    const pos = await getPosition(payload.highAccuracy);
    return { lat: pos.coords.latitude, lng: pos.coords.longitude };
  }
);

```

## Properties

- **`handler`** _(RpcHandler<SerializerInput<S>, SerializerOutput<S>>)_: 

- **`methodName`** _(string)_: 

- **`session`** _(UseSessionReturn)_: 

## Returns

```typescript
UseRpcReturn;

```

---

This document was rendered at 2026-08-28T04:22:14.868Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/userpc.md](https://docs.livekit.io/reference/components/react/hook/userpc.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-92"></a>
## Page 92: reference/components/react/hook/usesequentialroomconnectdisconnect
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usesequentialroomconnectdisconnect  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usesequentialroomconnectdisconnect.md

LiveKit docs › React components › Hooks › useSequentialRoomConnectDisconnect

---

# useSequentialRoomConnectDisconnect

When calling room.disconnect() as part of a React useEffect cleanup function, it is possible for a room.connect(...) in the effect body to start running while the room.disconnect() is still running. This hook sequentializes these two operations, so they always happen in order and never overlap.

## Import

```typescript
import { useSequentialRoomConnectDisconnect } from "@livekit/components-react";

```

## Usage

```ts
const { connect, disconnect } = useSequentialRoomConnectDisconnect(room);

// Connecting to a room:
useEffect(() => {
  connect();
  return () => disconnect();
}, [connect, disconnect]);

```

## Properties

- **`room`** _(R)_: 

## Returns

```typescript
UseSequentialRoomConnectDisconnectResults<R>;

```

---

This document was rendered at 2026-08-28T04:22:14.890Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usesequentialroomconnectdisconnect.md](https://docs.livekit.io/reference/components/react/hook/usesequentialroomconnectdisconnect.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-93"></a>
## Page 93: reference/components/react/hook/usesession
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usesession  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usesession.md

LiveKit docs › React components › Hooks › useSession

---

# useSession

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

A Session represents a managed connection to a Room which can contain Agents.

## Import

```typescript
import { useSession } from "@livekit/components-react";

```

## Properties

- **`tokenSource`** _(TokenSourceConfigurable)_: 

## Returns

```typescript
UseSessionReturn;

```

---

This document was rendered at 2026-08-28T04:22:14.901Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usesession.md](https://docs.livekit.io/reference/components/react/hook/usesession.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-94"></a>
## Page 94: reference/components/react/hook/usesessioncontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usesessioncontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usesessioncontext.md

LiveKit docs › React components › Hooks › useSessionContext

---

# useSessionContext

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

Ensures that a session is provided via context. If no session is provided, an error is thrown.

## Import

```typescript
import { useSessionContext } from "@livekit/components-react";

```

## Returns

```typescript
UseSessionReturn;

```

---

This document was rendered at 2026-08-28T04:22:14.907Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usesessioncontext.md](https://docs.livekit.io/reference/components/react/hook/usesessioncontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-95"></a>
## Page 95: reference/components/react/hook/usesessionmessages
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usesessionmessages  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usesessionmessages.md

LiveKit docs › React components › Hooks › useSessionMessages

---

# useSessionMessages

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

## Import

```typescript
import { useSessionMessages } from "@livekit/components-react";

```

## Properties

- **`session`** _(UseSessionReturn)_ (optional): 

## Returns

```typescript
UseSessionMessagesReturn;

```

---

This document was rendered at 2026-08-28T04:22:14.928Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usesessionmessages.md](https://docs.livekit.io/reference/components/react/hook/usesessionmessages.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-96"></a>
## Page 96: reference/components/react/hook/usesortedparticipants
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usesortedparticipants  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usesortedparticipants.md

LiveKit docs › React components › Hooks › useSortedParticipants

---

# useSortedParticipants

The `useSortedParticipants` hook returns the participants sorted by importance.

## Import

```typescript
import { useSortedParticipants } from "@livekit/components-react";

```

## Properties

- **`participants`** _(Array<Participant>)_: 

## Returns

```typescript
Participant[]

```

---

This document was rendered at 2026-08-28T04:22:14.936Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usesortedparticipants.md](https://docs.livekit.io/reference/components/react/hook/usesortedparticipants.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-97"></a>
## Page 97: reference/components/react/hook/usespeakingparticipants
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usespeakingparticipants  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usespeakingparticipants.md

LiveKit docs › React components › Hooks › useSpeakingParticipants

---

# useSpeakingParticipants

The `useSpeakingParticipants` hook returns only the active speakers of all participants.

## Import

```typescript
import { useSpeakingParticipants } from "@livekit/components-react";

```

## Usage

```tsx
const activeSpeakers = useSpeakingParticipants();

```

## Returns

```typescript
import('livekit-client').Participant[]

```

---

This document was rendered at 2026-08-28T04:22:14.947Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usespeakingparticipants.md](https://docs.livekit.io/reference/components/react/hook/usespeakingparticipants.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-98"></a>
## Page 98: reference/components/react/hook/usestartaudio
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usestartaudio  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usestartaudio.md

LiveKit docs › React components › Hooks › useStartAudio

---

# useStartAudio

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

In many browsers to start audio playback, the user must perform a user-initiated event such as clicking a button. The `useStatAudio` hook returns an object with a boolean `canPlayAudio` flag that indicates whether audio playback is allowed in the current context, as well as a `startAudio` function that can be called in a button `onClick` callback to start audio playback in the current context.

## Import

```typescript
import { useStartAudio } from "@livekit/components-react";

```

## Properties

- **`input.props`** _(React.ButtonHTMLAttributes<HTMLButtonElement>)_: 

- **`input.room`** _(Room)_ (optional): 

## Returns

```typescript
{
    mergedProps: React.ButtonHTMLAttributes<HTMLButtonElement> & {
        className: string;
        onClick: () => void;
        style: {
            display: string;
        };
    };
    canPlayAudio: boolean;
}

```

---

This document was rendered at 2026-08-28T04:22:14.966Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usestartaudio.md](https://docs.livekit.io/reference/components/react/hook/usestartaudio.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-99"></a>
## Page 99: reference/components/react/hook/usestartvideo
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usestartvideo  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usestartvideo.md

LiveKit docs › React components › Hooks › useStartVideo

---

# useStartVideo

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

In some browsers to start video playback in low power mode, the user must perform a user-initiated event such as clicking a button. The `useStartVideo` hook returns an object with a boolean `canPlayVideo` flag that indicates whether video playback is allowed in the current context, as well as a `startVideo` function that can be called in a button `onClick` callback to start video playback in the current context.

## Import

```typescript
import { useStartVideo } from "@livekit/components-react";

```

## Properties

- **`input.props`** _(React.ButtonHTMLAttributes<HTMLButtonElement>)_: 

- **`input.room`** _(Room)_ (optional): 

## Returns

```typescript
{
    mergedProps: React.ButtonHTMLAttributes<HTMLButtonElement> & {
        className: string;
        onClick: () => void;
        style: {
            display: string;
        };
    };
    canPlayVideo: boolean;
}

```

---

This document was rendered at 2026-08-28T04:22:14.966Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usestartvideo.md](https://docs.livekit.io/reference/components/react/hook/usestartvideo.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-100"></a>
## Page 100: reference/components/react/hook/useswipe
**Original URL:** https://docs.livekit.io/reference/components/react/hook/useswipe  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/useswipe.md

LiveKit docs › React components › Hooks › useSwipe

---

# useSwipe

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

Simple implementation to detect horizontal swipe actions. Accepts callbacks for on right and left swipes.

## Import

```typescript
import { useSwipe } from "@livekit/components-react";

```

## Usage

```tsx
 <div
      onTouchStart={onTouchStart}
      onTouchMove={onTouchMove}
      onTouchEnd={onTouchEnd}
    >

```

## Properties

- **`element`** _(React.RefObject<HTMLElement>)_: 

## Returns

```typescript
void

```

---

This document was rendered at 2026-08-28T04:22:15.004Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/useswipe.md](https://docs.livekit.io/reference/components/react/hook/useswipe.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-101"></a>
## Page 101: reference/components/react/hook/usetextstream
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetextstream  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetextstream.md

LiveKit docs › React components › Hooks › useTextStream

---

# useTextStream

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

## Import

```typescript
import { useTextStream } from "@livekit/components-react";

```

## Usage

```tsx
const { textStreams } = useTextStream("my-topic");
return <div>{textStreams.map((textStream) => textStream.text)}</div>;

```

## Properties

- **`topic`** _(string)_: the topic to listen to

## Returns

an array of TextStreamData that holds the text, participantInfo, and streamInfo

```typescript
{
    textStreams: TextStreamData[];
}

```

---

This document was rendered at 2026-08-28T04:22:14.999Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetextstream.md](https://docs.livekit.io/reference/components/react/hook/usetextstream.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-102"></a>
## Page 102: reference/components/react/hook/usetoken
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetoken  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetoken.md

LiveKit docs › React components › Hooks › useToken

---

# useToken

The `useToken` hook fetches a token from the given token endpoint with the given user info.

## Import

```typescript
import { useToken } from "@livekit/components-react";

```

## Usage

```tsx
const token = useToken(<token-endpoint>, roomName, { userInfo: { identity, name }});

```

## Properties

- **`roomName`** _(string)_: 

- **`tokenEndpoint`** _(string | undefined)_: 

- **`options.userInfo`** _(UserInfo)_ (optional): 

## Returns

```typescript
string | undefined;

```

---

This document was rendered at 2026-08-28T04:22:15.028Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetoken.md](https://docs.livekit.io/reference/components/react/hook/usetoken.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-103"></a>
## Page 103: reference/components/react/hook/usetrackbyname
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetrackbyname  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetrackbyname.md

LiveKit docs › React components › Hooks › useTrackByName

---

# useTrackByName

This function `useTrackByName` allows you to access a track by referencing its track name. Inside the function, it ensures that the a valid `participant` reference is available by checking for both a passed participant argument and, if not available, a valid participant context.

## Import

```typescript
import { useTrackByName } from "@livekit/components-react";

```

## Properties

- **`name`** _(string)_: 

- **`participant`** _(Participant)_ (optional): 

## Returns

```typescript
import("@livekit/components-core").TrackReferenceOrPlaceholder;

```

---

This document was rendered at 2026-08-28T04:22:15.012Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetrackbyname.md](https://docs.livekit.io/reference/components/react/hook/usetrackbyname.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-104"></a>
## Page 104: reference/components/react/hook/usetrackmutedindicator
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetrackmutedindicator  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetrackmutedindicator.md

LiveKit docs › React components › Hooks › useTrackMutedIndicator

---

# useTrackMutedIndicator

The `useTrackMutedIndicator` hook is used to implement the `TrackMutedIndicator` component and returns the muted state of the given track.

## Import

```typescript
import { useTrackMutedIndicator } from "@livekit/components-react";

```

## Usage

```tsx
const { isMuted } = useTrackMutedIndicator(trackRef);

```

## Properties

- **`trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): 

## Returns

```typescript
TrackMutedIndicatorReturnType;

```

---

This document was rendered at 2026-08-28T04:22:15.022Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetrackmutedindicator.md](https://docs.livekit.io/reference/components/react/hook/usetrackmutedindicator.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-105"></a>
## Page 105: reference/components/react/hook/usetrackrefcontext
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetrackrefcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetrackrefcontext.md

LiveKit docs › React components › Hooks › useTrackRefContext

---

# useTrackRefContext

Ensures that a track reference is provided via context. If not inside a `TrackRefContext`, an error is thrown.

## Import

```typescript
import { useTrackRefContext } from "@livekit/components-react";

```

## Returns

```typescript
TrackReferenceOrPlaceholder;

```

---

This document was rendered at 2026-08-28T04:22:15.117Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetrackrefcontext.md](https://docs.livekit.io/reference/components/react/hook/usetrackrefcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-106"></a>
## Page 106: reference/components/react/hook/usetracks
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetracks  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetracks.md

LiveKit docs › React components › Hooks › useTracks

---

# useTracks

The `useTracks` hook returns an array of `TrackReference` or `TrackReferenceOrPlaceholder` depending on the provided `sources` property. If only subscribed tracks are desired, set the `onlySubscribed` property to `true`.

## Import

```typescript
import { useTracks } from "@livekit/components-react";

```

## Usage

### Example 1

```ts
// Return all camera track publications.
const trackReferences: TrackReference[] = useTracks([Track.Source.Camera]);

```

### Example 2

```ts
// Return all subscribed camera tracks as well as placeholders for
// participants without a camera subscription.
const trackReferencesWithPlaceholders: TrackReferenceOrPlaceholder[] = useTracks([
  { source: Track.Source.Camera, withPlaceholder: true }
]);

```

## Properties

- **`sources`** _(T)_ (optional): 

## Returns

```typescript
UseTracksHookReturnType<T>;

```

---

This document was rendered at 2026-08-28T04:22:15.112Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetracks.md](https://docs.livekit.io/reference/components/react/hook/usetracks.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-107"></a>
## Page 107: reference/components/react/hook/usetracktoggle
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetracktoggle  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetracktoggle.md

LiveKit docs › React components › Hooks › useTrackToggle

---

# useTrackToggle

The `useTrackToggle` hook is used to implement the `TrackToggle` component and returns state and functionality of the given track.

## Import

```typescript
import { useTrackToggle } from "@livekit/components-react";

```

## Usage

```tsx
const { buttonProps, enabled } = useTrackToggle(trackRef);
return <button {...buttonProps}>{enabled ? "disable" : "enable"}</button>;

```

## Properties

- **`input.room`** _(Room)_ (optional): 

## Returns

```typescript
{
  toggle: ((forceState?: boolean) => Promise<void>) |
    ((
      forceState?: boolean,
      captureOptions?: import("@livekit/components-core").CaptureOptionsBySource<T> | undefined
    ) => Promise<boolean | undefined>);
  enabled: boolean;
  pending: boolean;
  track: import("livekit-client").LocalTrackPublication | undefined;
  buttonProps: React.ButtonHTMLAttributes<HTMLButtonElement>;
}

```

---

This document was rendered at 2026-08-28T04:22:15.088Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetracktoggle.md](https://docs.livekit.io/reference/components/react/hook/usetracktoggle.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-108"></a>
## Page 108: reference/components/react/hook/usetracktranscription
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetracktranscription  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetracktranscription.md

LiveKit docs › React components › Hooks › useTrackTranscription

---

# useTrackTranscription

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

> 🔥 **Caution**
> 
> This API is deprecated: Use useTranscription instead

## Import

```typescript
import { useTrackTranscription } from "@livekit/components-react";

```

## Properties

- **`trackRef`** _(TrackReferenceOrPlaceholder | undefined)_: 

- **`options.bufferSize`** _(number)_ (optional): how many transcription segments should be buffered in state

- **`options.onTranscription`** _((newSegments: TranscriptionSegment[]) => void)_ (optional): optional callback for retrieving newly incoming transcriptions only

## Returns

An object consisting of `segments` with maximum length of opts.bufferSize

```typescript
{
    segments: ReceivedTranscriptionSegment[];
}

```

---

This document was rendered at 2026-08-28T04:22:15.082Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetracktranscription.md](https://docs.livekit.io/reference/components/react/hook/usetracktranscription.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-109"></a>
## Page 109: reference/components/react/hook/usetrackvolume
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetrackvolume  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetrackvolume.md

LiveKit docs › React components › Hooks › useTrackVolume

---

# useTrackVolume

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

Hook for tracking the volume of an audio track using the Web Audio API.

## Import

```typescript
import { useTrackVolume } from "@livekit/components-react";

```

## Properties

- **`trackOrTrackReference`** _(LocalAudioTrack | RemoteAudioTrack | TrackReference)_ (optional): 

## Returns

```typescript
number;

```

---

This document was rendered at 2026-08-28T04:22:15.083Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetrackvolume.md](https://docs.livekit.io/reference/components/react/hook/usetrackvolume.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-110"></a>
## Page 110: reference/components/react/hook/usetranscriptions
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usetranscriptions  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usetranscriptions.md

LiveKit docs › React components › Hooks › useTranscriptions

---

# useTranscriptions

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

useTranscriptions is a hook that returns the transcriptions for the given participant identities and track sids, if no options are provided, it will return all transcriptions

## Import

```typescript
import { useTranscriptions } from "@livekit/components-react";

```

## Usage

```tsx
const transcriptions = useTranscriptions();
return <div>{transcriptions.map((transcription) => transcription.text)}</div>;

```

## Properties

- **`opts.participantIdentities`** _(string[])_ (optional): 

- **`opts.room`** _(Room)_ (optional): 

- **`opts.trackSids`** _(string[])_ (optional): 

## Returns

```typescript
import('@livekit/components-core').TextStreamData[]

```

---

This document was rendered at 2026-08-28T04:22:15.076Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usetranscriptions.md](https://docs.livekit.io/reference/components/react/hook/usetranscriptions.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-111"></a>
## Page 111: reference/components/react/hook/usevisualstableupdate
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usevisualstableupdate  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usevisualstableupdate.md

LiveKit docs › React components › Hooks › useVisualStableUpdate

---

# useVisualStableUpdate

The `useVisualStableUpdate` hook is used to prevent visually jarring jumps and shifts of elements in an array. The algorithm only starts to update when there are more items than visually fit on a page. If this is the case, it will make sure that speaking participants move to the first page and are always visible.

## Import

```typescript
import { useVisualStableUpdate } from "@livekit/components-react";

```

## Remarks

Updating the array can occur because attendees leave or join a room, or because they mute/unmute or start speaking. The hook is used for the `GridLayout` and `CarouselLayout` components.

## Usage

```tsx
const trackRefs = useTracks();
const updatedTrackRefs = useVisualStableUpdate(trackRefs, itemPerPage);

```

## Properties

- **`maxItemsOnPage`** _(number)_: 

- **`trackReferences`** _(TrackReferenceOrPlaceholder[])_: 

- **`options.customSortFunction`** _((trackReferences: TrackReferenceOrPlaceholder[]) => TrackReferenceOrPlaceholder[])_ (optional): Overwrites the default sort function.

## Returns

```typescript
TrackReferenceOrPlaceholder[]

```

---

This document was rendered at 2026-08-28T04:22:15.103Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usevisualstableupdate.md](https://docs.livekit.io/reference/components/react/hook/usevisualstableupdate.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-112"></a>
## Page 112: reference/components/react/hook/usevoiceassistant
**Original URL:** https://docs.livekit.io/reference/components/react/hook/usevoiceassistant  
**Source MD URL:** https://docs.livekit.io/reference/components/react/hook/usevoiceassistant.md

LiveKit docs › React components › Hooks › useVoiceAssistant

---

# useVoiceAssistant

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

This hook looks for the first agent-participant in the room.

## Import

```typescript
import { useVoiceAssistant } from "@livekit/components-react";

```

## Remarks

This hook requires an agent running with livekit-agents >= 0.9.0

## Usage

```tsx
const { state, audioTrack, agentTranscriptions, agentAttributes } = useVoiceAssistant();

```

## Returns

```typescript
VoiceAssistant;

```

---

This document was rendered at 2026-08-28T04:22:15.115Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/hook/usevoiceassistant.md](https://docs.livekit.io/reference/components/react/hook/usevoiceassistant.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-113"></a>
## Page 113: reference/components/react/component/audioconference
**Original URL:** https://docs.livekit.io/reference/components/react/component/audioconference  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/audioconference.md

LiveKit docs › React components › Components › AudioConference

---

# AudioConference

This component is the default setup of a classic LiveKit audio conferencing app. It provides functionality like switching between participant grid view and focus view.

## Import

```typescript
import { AudioConference } from "@livekit/components-react";

```

## Remarks

The component is implemented with other LiveKit components like `FocusContextProvider`, `GridLayout`, `ControlBar`, `FocusLayoutContainer` and `FocusLayout`.

## Usage

```tsx
<LiveKitRoom>
  <AudioConference />
<LiveKitRoom>

```

---

This document was rendered at 2026-08-28T04:22:15.196Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/audioconference.md](https://docs.livekit.io/reference/components/react/component/audioconference.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-114"></a>
## Page 114: reference/components/react/component/audiotrack
**Original URL:** https://docs.livekit.io/reference/components/react/component/audiotrack  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/audiotrack.md

LiveKit docs › React components › Components › AudioTrack

---

# AudioTrack

The AudioTrack component is responsible for rendering participant audio tracks. This component must have access to the participant's context, or alternatively pass it a `Participant` as a property.

## Import

```typescript
import { AudioTrack } from "@livekit/components-react";

```

## Usage

```tsx
<ParticipantTile>
  <AudioTrack trackRef={trackRef} />
</ParticipantTile>

```

## Properties

- **`muted`** _(boolean)_ (optional): _(Optional)_ Mutes the audio track if set to `true`.

- **`onSubscriptionStatusChanged`** _((subscribed: boolean) => void)_ (optional): _(Optional)_

- **`trackRef`** _(TrackReference)_ (optional): _(Optional)_ The track reference of the track from which the audio is to be rendered.

- **`volume`** _(number)_ (optional): _(Optional)_ Sets the volume of the audio track. By default, the range is between `0.0` and `1.0`.

---

This document was rendered at 2026-08-28T04:22:15.122Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/audiotrack.md](https://docs.livekit.io/reference/components/react/component/audiotrack.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-115"></a>
## Page 115: reference/components/react/component/audiovisualizer
**Original URL:** https://docs.livekit.io/reference/components/react/component/audiovisualizer  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/audiovisualizer.md

LiveKit docs › React components › Components › AudioVisualizer

---

# AudioVisualizer

> 🔥 **Caution**
> 
> This API is deprecated: Use BarVisualizer instead

The AudioVisualizer component is used to visualize the audio volume of a given audio track.

## Import

```typescript
import { AudioVisualizer } from "@livekit/components-react";

```

## Remarks

Requires a `TrackReferenceOrPlaceholder` to be provided either as a property or via the `TrackRefContext`.

## Usage

```tsx
<AudioVisualizer />

```

## Properties

- **`trackRef`** _(TrackReference)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.125Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/audiovisualizer.md](https://docs.livekit.io/reference/components/react/component/audiovisualizer.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-116"></a>
## Page 116: reference/components/react/component/barvisualizer
**Original URL:** https://docs.livekit.io/reference/components/react/component/barvisualizer  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/barvisualizer.md

LiveKit docs › React components › Components › BarVisualizer

---

# BarVisualizer

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

Visualizes audio signals from a TrackReference as bars. If the `state` prop is set, it automatically transitions between VoiceAssistant states.

## Import

```typescript
import { BarVisualizer } from "@livekit/components-react";

```

## Remarks

For VoiceAssistant state transitions this component requires a voice assistant agent running with livekit-agents >= 0.9.0

## Usage

### Example 1

```tsx
function SimpleVoiceAssistant() {
  const { state, audioTrack } = useVoiceAssistant();
  return <BarVisualizer state={state} trackRef={audioTrack} />;
}

```

### Styling the BarVisualizer using CSS classes

```css
.lk-audio-bar {
 // Styles for "idle" bars
 }
.lk-audio-bar.lk-highlighted {
 // Styles for "active" bars
}

```

### Styling the BarVisualizer using CSS custom properties

```css
--lk-fg // for the "active" colour, note that this defines the main foreground colour for the whole "theme"
--lk-va-bg // for "idle" colour

```

### Using a custom bar template for the BarVisualizer

```tsx
<BarVisualizer>
  <div className="all the classes" />
</BarVisualizer>

```

the highlighted children will get a data prop of data-lk-highlighted for them to switch between active and idle bars in their own template bar

---

This document was rendered at 2026-08-28T04:22:15.144Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/barvisualizer.md](https://docs.livekit.io/reference/components/react/component/barvisualizer.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-117"></a>
## Page 117: reference/components/react/component/carousellayout
**Original URL:** https://docs.livekit.io/reference/components/react/component/carousellayout  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/carousellayout.md

LiveKit docs › React components › Components › CarouselLayout

---

# CarouselLayout

The `CarouselLayout` component displays a list of tracks in a scroll container. It will display as many tiles as possible and overflow the rest.

## Import

```typescript
import { CarouselLayout } from "@livekit/components-react";

```

## Remarks

To ensure visual stability when tiles are reordered due to track updates, the component uses the `useVisualStableUpdate` hook.

## Usage

```tsx
const tracks = useTracks([Track.Source.Camera]);
<CarouselLayout tracks={tracks}>
  <ParticipantTile />
</CarouselLayout>;

```

## Properties

- **`children`** _(React.ReactNode)_: 

- **`tracks`** _(TrackReferenceOrPlaceholder[])_: 

- **`orientation`** _('vertical' | 'horizontal')_ (optional): _(Optional)_ Place the tiles vertically or horizontally next to each other. If undefined orientation is guessed by the dimensions of the container.

---

This document was rendered at 2026-08-28T04:22:15.139Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/carousellayout.md](https://docs.livekit.io/reference/components/react/component/carousellayout.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-118"></a>
## Page 118: reference/components/react/component/chat
**Original URL:** https://docs.livekit.io/reference/components/react/component/chat  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/chat.md

LiveKit docs › React components › Components › Chat

---

# Chat

The Chat component provides ready-to-use chat functionality in a LiveKit room. Messages are distributed to all participants in the room in real-time.

## Import

```typescript
import { Chat } from "@livekit/components-react";

```

## Remarks

- Only users who are in the room at the time of dispatch will receive messages - Message history is not persisted between sessions - Requires `@livekit/components-styles` to be imported for styling

## Usage

```tsx
import "@livekit/components-styles";

function Room() {
  return (
    <LiveKitRoom data-lk-theme="default">
      <Chat />
    </LiveKitRoom>
  );
}

```

For custom styling, refer to: https://docs.livekit.io/reference/components/react/concepts/style-components/

## Properties

- **`messageFormatter`** _(MessageFormatter)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.157Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/chat.md](https://docs.livekit.io/reference/components/react/component/chat.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-119"></a>
## Page 119: reference/components/react/component/chatentry
**Original URL:** https://docs.livekit.io/reference/components/react/component/chatentry  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/chatentry.md

LiveKit docs › React components › Components › ChatEntry

---

# ChatEntry

The `ChatEntry` component holds and displays one chat message.

## Import

```typescript
import { ChatEntry } from "@livekit/components-react";

```

## Usage

```tsx
<Chat>
  <ChatEntry />
</Chat>

```

## Properties

- **`entry`** _(ReceivedChatMessage)_: The chat massage object to display.

- **`hideName`** _(boolean)_ (optional): _(Optional)_ Hide sender name. Useful when displaying multiple consecutive chat messages from the same person.

- **`hideTimestamp`** _(boolean)_ (optional): _(Optional)_ Hide message timestamp.

- **`messageFormatter`** _(MessageFormatter)_ (optional): _(Optional)_ An optional formatter for the message body.

---

This document was rendered at 2026-08-28T04:22:15.148Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/chatentry.md](https://docs.livekit.io/reference/components/react/component/chatentry.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-120"></a>
## Page 120: reference/components/react/component/chattoggle
**Original URL:** https://docs.livekit.io/reference/components/react/component/chattoggle  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/chattoggle.md

LiveKit docs › React components › Components › ChatToggle

---

# ChatToggle

The `ChatToggle` component is a button that toggles the visibility of the `Chat` component.

## Import

```typescript
import { ChatToggle } from "@livekit/components-react";

```

## Remarks

For the component to have any effect it has to live inside a `LayoutContext` context.

## Usage

```tsx
<LiveKitRoom>
  <ChatToggle />
</LiveKitRoom>

```

---

This document was rendered at 2026-08-28T04:22:15.332Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/chattoggle.md](https://docs.livekit.io/reference/components/react/component/chattoggle.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-121"></a>
## Page 121: reference/components/react/component/clearpinbutton
**Original URL:** https://docs.livekit.io/reference/components/react/component/clearpinbutton  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/clearpinbutton.md

LiveKit docs › React components › Components › ClearPinButton

---

# ClearPinButton

The `ClearPinButton` is a basic html button with the added ability to signal the `LayoutContext` that it should display the grid view again.

## Import

```typescript
import { ClearPinButton } from "@livekit/components-react";

```

## Remarks

This component works only inside a `LayoutContext`.

## Usage

```tsx
<LiveKitRoom>
  <ClearPinButton>Back to grid view</ClearPinButton>
</LiveKitRoom>

```

---

This document was rendered at 2026-08-28T04:22:15.166Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/clearpinbutton.md](https://docs.livekit.io/reference/components/react/component/clearpinbutton.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-122"></a>
## Page 122: reference/components/react/component/connectionqualityindicator
**Original URL:** https://docs.livekit.io/reference/components/react/component/connectionqualityindicator  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/connectionqualityindicator.md

LiveKit docs › React components › Components › ConnectionQualityIndicator

---

# ConnectionQualityIndicator

The `ConnectionQualityIndicator` shows the individual connection quality of a participant.

## Import

```typescript
import { ConnectionQualityIndicator } from "@livekit/components-react";

```

## Usage

```tsx
<ConnectionQualityIndicator />

```

---

This document was rendered at 2026-08-28T04:22:15.209Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/connectionqualityindicator.md](https://docs.livekit.io/reference/components/react/component/connectionqualityindicator.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-123"></a>
## Page 123: reference/components/react/component/connectionstate
**Original URL:** https://docs.livekit.io/reference/components/react/component/connectionstate  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/connectionstate.md

LiveKit docs › React components › Components › ConnectionState

---

# ConnectionState

The `ConnectionState` component displays the connection status of the room as strings (`"connected" | "connecting" | "disconnected" | "reconnecting"`).

## Import

```typescript
import { ConnectionState } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom>
  <ConnectionState />
</LiveKitRoom>

```

## Properties

- **`room`** _(Room)_ (optional): _(Optional)_ The room from which the connection status should be displayed.

---

This document was rendered at 2026-08-28T04:22:15.194Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/connectionstate.md](https://docs.livekit.io/reference/components/react/component/connectionstate.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-124"></a>
## Page 124: reference/components/react/component/connectionstatetoast
**Original URL:** https://docs.livekit.io/reference/components/react/component/connectionstatetoast  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/connectionstatetoast.md

LiveKit docs › React components › Components › ConnectionStateToast

---

# ConnectionStateToast

The `ConnectionStateToast` component displays a toast notification indicating the current connection state of the room.

## Import

```typescript
import { ConnectionStateToast } from "@livekit/components-react";

```

## Properties

- **`room`** _(Room)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.179Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/connectionstatetoast.md](https://docs.livekit.io/reference/components/react/component/connectionstatetoast.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-125"></a>
## Page 125: reference/components/react/component/controlbar
**Original URL:** https://docs.livekit.io/reference/components/react/component/controlbar  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/controlbar.md

LiveKit docs › React components › Components › ControlBar

---

# ControlBar

The `ControlBar` prefab gives the user the basic user interface to control their media devices (camera, microphone and screen share), open the `Chat` and leave the room.

## Import

```typescript
import { ControlBar } from "@livekit/components-react";

```

## Remarks

This component is built with other LiveKit components like `TrackToggle`, `DeviceSelectorButton`, `DisconnectButton` and `StartAudio`.

## Usage

```tsx
<LiveKitRoom>
  <ControlBar />
</LiveKitRoom>

```

## Properties

- **`controls`** _(ControlBarControls)_ (optional): _(Optional)_

_(Optional)_

- **`undefined`** _(undefined)_: 

- **`saveUserChoices`** _(boolean)_ (optional): _(Optional)_ If `true`, the user's device choices will be persisted. This will enable the user to have the same device choices when they rejoin the room.

- **`variation`** _('minimal' | 'verbose' | 'textOnly')_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.190Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/controlbar.md](https://docs.livekit.io/reference/components/react/component/controlbar.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-126"></a>
## Page 126: reference/components/react/component/disconnectbutton
**Original URL:** https://docs.livekit.io/reference/components/react/component/disconnectbutton  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/disconnectbutton.md

LiveKit docs › React components › Components › DisconnectButton

---

# DisconnectButton

The `DisconnectButton` is a basic html button with the added ability to disconnect from a LiveKit room. Normally this is the big red button that allows end users to leave the video or audio call.

## Import

```typescript
import { DisconnectButton } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom>
  <DisconnectButton>Leave room</DisconnectButton>
</LiveKitRoom>

```

## Properties

- **`stopTracks`** _(boolean)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.202Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/disconnectbutton.md](https://docs.livekit.io/reference/components/react/component/disconnectbutton.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-127"></a>
## Page 127: reference/components/react/component/focuslayout
**Original URL:** https://docs.livekit.io/reference/components/react/component/focuslayout  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/focuslayout.md

LiveKit docs › React components › Components › FocusLayout

---

# FocusLayout

The `FocusLayout` component is just a light wrapper around the `ParticipantTile` to display a single participant.

## Import

```typescript
import { FocusLayout } from "@livekit/components-react";

```

## Properties

- **`onParticipantClick`** _((evt: ParticipantClickEvent) => void)_ (optional): _(Optional)_

- **`trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): _(Optional)_ The track to display in the focus layout.

---

This document was rendered at 2026-08-28T04:22:15.222Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/focuslayout.md](https://docs.livekit.io/reference/components/react/component/focuslayout.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-128"></a>
## Page 128: reference/components/react/component/focuslayoutcontainer
**Original URL:** https://docs.livekit.io/reference/components/react/component/focuslayoutcontainer  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/focuslayoutcontainer.md

LiveKit docs › React components › Components › FocusLayoutContainer

---

# FocusLayoutContainer

The `FocusLayoutContainer` is a layout component that expects two children: A small side component: In a video conference, this is usually a carousel of participants who are not in focus. And a larger main component to display the focused participant. For example, with the `FocusLayout` component.

## Import

```typescript
import { FocusLayoutContainer } from "@livekit/components-react";

```

---

This document was rendered at 2026-08-28T04:22:15.250Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/focuslayoutcontainer.md](https://docs.livekit.io/reference/components/react/component/focuslayoutcontainer.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-129"></a>
## Page 129: reference/components/react/component/focustoggle
**Original URL:** https://docs.livekit.io/reference/components/react/component/focustoggle  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/focustoggle.md

LiveKit docs › React components › Components › FocusToggle

---

# FocusToggle

The `FocusToggle` puts the `ParticipantTile` in focus or removes it from focus.

## Import

```typescript
import { FocusToggle } from "@livekit/components-react";

```

## Remarks

This component needs to live inside `LayoutContext` to work properly.

## Usage

```tsx
<ParticipantTile>
  <FocusToggle />
</ParticipantTile>

```

## Properties

- **`trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.260Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/focustoggle.md](https://docs.livekit.io/reference/components/react/component/focustoggle.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-130"></a>
## Page 130: reference/components/react/component/gridlayout
**Original URL:** https://docs.livekit.io/reference/components/react/component/gridlayout  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/gridlayout.md

LiveKit docs › React components › Components › GridLayout

---

# GridLayout

The `GridLayout` component displays the nested participants in a grid where every participants has the same size. It also supports pagination if there are more participants than the grid can display.

## Import

```typescript
import { GridLayout } from "@livekit/components-react";

```

## Remarks

To ensure visual stability when tiles are reordered due to track updates, the component uses the `useVisualStableUpdate` hook.

## Usage

```tsx
<LiveKitRoom>
  <GridLayout tracks={tracks}>
    <ParticipantTile />
  </GridLayout>
<LiveKitRoom>

```

## Properties

- **`children`** _(React.ReactNode)_: 

- **`tracks`** _(TrackReferenceOrPlaceholder[])_:

---

This document was rendered at 2026-08-28T04:22:15.276Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/gridlayout.md](https://docs.livekit.io/reference/components/react/component/gridlayout.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-131"></a>
## Page 131: reference/components/react/component/layoutcontext
**Original URL:** https://docs.livekit.io/reference/components/react/component/layoutcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/layoutcontext.md

LiveKit docs › React components › Components › LayoutContext

---

# LayoutContext

## Import

```typescript
import { LayoutContext } from "@livekit/components-react";

```

---

This document was rendered at 2026-08-28T04:22:15.287Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/layoutcontext.md](https://docs.livekit.io/reference/components/react/component/layoutcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-132"></a>
## Page 132: reference/components/react/component/layoutcontextprovider
**Original URL:** https://docs.livekit.io/reference/components/react/component/layoutcontextprovider  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/layoutcontextprovider.md

LiveKit docs › React components › Components › LayoutContextProvider

---

# LayoutContextProvider

> ℹ️ **Note**
> 
> This feature is experimental and may change or be removed based on developer feedback and real-world usage.

## Import

```typescript
import { LayoutContextProvider } from "@livekit/components-react";

```

## Properties

- **`onPinChange`** _((state: PinState) => void)_ (optional): _(Optional)_

- **`onWidgetChange`** _((state: WidgetState) => void)_ (optional): _(Optional)_

- **`value`** _(LayoutContextType)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.286Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/layoutcontextprovider.md](https://docs.livekit.io/reference/components/react/component/layoutcontextprovider.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-133"></a>
## Page 133: reference/components/react/component/livekitroom
**Original URL:** https://docs.livekit.io/reference/components/react/component/livekitroom  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/livekitroom.md

LiveKit docs › React components › Components › LiveKitRoom

---

# LiveKitRoom

The `LiveKitRoom` component provides the room context to all its child components. It is generally the starting point of your LiveKit app and the root of the LiveKit component tree. It provides the room state as a React context to all child components, so you don't have to pass it yourself.

## Import

```typescript
import { LiveKitRoom } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom token="<livekit-token>" serverUrl="<url-to-livekit-server>" connect={true}>
  ...
</LiveKitRoom>

```

## Properties

- **`serverUrl`** _(string | undefined)_: URL to the LiveKit server. For example: `wss://<domain>.livekit.cloud` To simplify the implementation, `undefined` is also accepted as an intermediate value, but only with a valid string url can the connection be established.

- **`token`** _(string | undefined)_: A user specific access token for a client to authenticate to the room. This token is necessary to establish a connection to the room. To simplify the implementation, `undefined` is also accepted as an intermediate value, but only with a valid string token can the connection be established.

- **`audio`** _(AudioCaptureOptions | boolean)_ (optional): _(Optional)_ Publish audio immediately after connecting to your LiveKit room.

- **`connect`** _(boolean)_ (optional): _(Optional)_ If set to true a connection to LiveKit room is initiated.

- **`connectOptions`** _(RoomConnectOptions)_ (optional): _(Optional)_ Define options how to connect to the LiveKit server.

- **`onConnected`** _(() => void)_ (optional): _(Optional)_

- **`onDisconnected`** _((reason?: DisconnectReason) => void)_ (optional): _(Optional)_

- **`onEncryptionError`** _((error: Error) => void)_ (optional): _(Optional)_

- **`onError`** _((error: Error) => void)_ (optional): _(Optional)_

- **`onMediaDeviceFailure`** _((failure?: MediaDeviceFailure, kind?: MediaDeviceKind) => void)_ (optional): _(Optional)_

- **`options`** _(RoomOptions)_ (optional): _(Optional)_ Options for when creating a new room. When you pass your own room instance to this component, these options have no effect. Instead, set the options directly in the room instance.

- **`room`** _(Room)_ (optional): _(Optional)_ Optional room instance. By passing your own room instance you overwrite the `options` parameter, make sure to set the options directly on the room instance itself.

- **`screen`** _(ScreenShareCaptureOptions | boolean)_ (optional): _(Optional)_ Publish screen share immediately after connecting to your LiveKit room.

- **`simulateParticipants`** _(number | undefined)_ (optional): _(Optional)_

- **`video`** _(VideoCaptureOptions | boolean)_ (optional): _(Optional)_ Publish video immediately after connecting to your LiveKit room.

---

This document was rendered at 2026-08-28T04:22:15.308Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/livekitroom.md](https://docs.livekit.io/reference/components/react/component/livekitroom.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-134"></a>
## Page 134: reference/components/react/component/mediadevicemenu
**Original URL:** https://docs.livekit.io/reference/components/react/component/mediadevicemenu  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/mediadevicemenu.md

LiveKit docs › React components › Components › MediaDeviceMenu

---

# MediaDeviceMenu

The `MediaDeviceMenu` component is a button that opens a menu that lists all media devices and allows the user to select them.

## Import

```typescript
import { MediaDeviceMenu } from "@livekit/components-react";

```

## Remarks

This component is implemented with the `MediaDeviceSelect` LiveKit components.

## Usage

```tsx
<LiveKitRoom>
  <MediaDeviceMenu />
</LiveKitRoom>

```

## Properties

- **`initialSelection`** _(string)_ (optional): _(Optional)_

- **`kind`** _(MediaDeviceKind)_ (optional): _(Optional)_

- **`onActiveDeviceChange`** _((kind: MediaDeviceKind, deviceId: string) => void)_ (optional): _(Optional)_

- **`requestPermissions`** _(boolean)_ (optional): _(Optional)_ this will call getUserMedia if the permissions are not yet given to enumerate the devices with device labels. in some browsers multiple calls to getUserMedia result in multiple permission prompts. It's generally advised only flip this to true, once a (preview) track has been acquired successfully with the appropriate permissions.

- **`tracks`** _(Partial<Record<MediaDeviceKind, LocalAudioTrack | LocalVideoTrack | undefined>>)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.335Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/mediadevicemenu.md](https://docs.livekit.io/reference/components/react/component/mediadevicemenu.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-135"></a>
## Page 135: reference/components/react/component/mediadeviceselect
**Original URL:** https://docs.livekit.io/reference/components/react/component/mediadeviceselect  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/mediadeviceselect.md

LiveKit docs › React components › Components › MediaDeviceSelect

---

# MediaDeviceSelect

The `MediaDeviceSelect` list all media devices of one kind. Clicking on one of the listed devices make it the active media device.

## Import

```typescript
import { MediaDeviceSelect } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom>
  <MediaDeviceSelect kind="audioinput" />
</LiveKitRoom>

```

## Properties

- **`kind`** _(MediaDeviceKind)_: 

- **`exactMatch`** _(boolean)_ (optional): _(Optional)_ will force the browser to only return the specified device will call `onDeviceSelectError` with the error in case this fails

- **`initialSelection`** _(string)_ (optional): _(Optional)_

- **`onActiveDeviceChange`** _((deviceId: string) => void)_ (optional): _(Optional)_

- **`onDeviceListChange`** _((devices: MediaDeviceInfo[]) => void)_ (optional): _(Optional)_

- **`onDeviceSelectError`** _((e: Error) => void)_ (optional): _(Optional)_

- **`onError`** _((e: Error) => void)_ (optional): _(Optional)_

- **`requestPermissions`** _(boolean)_ (optional): _(Optional)_ this will call getUserMedia if the permissions are not yet given to enumerate the devices with device labels. in some browsers multiple calls to getUserMedia result in multiple permission prompts. It's generally advised only flip this to true, once a (preview) track has been acquired successfully with the appropriate permissions.

- **`track`** _(LocalAudioTrack | LocalVideoTrack)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.349Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/mediadeviceselect.md](https://docs.livekit.io/reference/components/react/component/mediadeviceselect.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-136"></a>
## Page 136: reference/components/react/component/participantaudiotile
**Original URL:** https://docs.livekit.io/reference/components/react/component/participantaudiotile  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/participantaudiotile.md

LiveKit docs › React components › Components › ParticipantAudioTile

---

# ParticipantAudioTile

The `ParticipantAudioTile` component is the base utility wrapper for displaying a visual representation of a participant. This component can be used as a child of the `TileLoop` or independently if a participant is passed as a property.

## Import

```typescript
import { ParticipantAudioTile } from "@livekit/components-react";

```

## Usage

```tsx
<ParticipantAudioTile />

```

## Properties

- **`disableSpeakingIndicator`** _(boolean)_ (optional): _(Optional)_

- **`onParticipantClick`** _((event: ParticipantClickEvent) => void)_ (optional): _(Optional)_

- **`trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): _(Optional)_ The track reference to display.

---

This document was rendered at 2026-08-28T04:22:15.598Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/participantaudiotile.md](https://docs.livekit.io/reference/components/react/component/participantaudiotile.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-137"></a>
## Page 137: reference/components/react/component/participantcontext
**Original URL:** https://docs.livekit.io/reference/components/react/component/participantcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/participantcontext.md

LiveKit docs › React components › Components › ParticipantContext

---

# ParticipantContext

## Import

```typescript
import { ParticipantContext } from "@livekit/components-react";

```

---

This document was rendered at 2026-08-28T04:22:15.369Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/participantcontext.md](https://docs.livekit.io/reference/components/react/component/participantcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-138"></a>
## Page 138: reference/components/react/component/participantcontextifneeded
**Original URL:** https://docs.livekit.io/reference/components/react/component/participantcontextifneeded  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/participantcontextifneeded.md

LiveKit docs › React components › Components › ParticipantContextIfNeeded

---

# ParticipantContextIfNeeded

The `ParticipantContextIfNeeded` component only creates a `ParticipantContext` if there is no `ParticipantContext` already.

## Import

```typescript
import { ParticipantContextIfNeeded } from "@livekit/components-react";

```

## Usage

```tsx
<ParticipantContextIfNeeded participant={trackReference.participant}>
  ...
</ParticipantContextIfNeeded>

```

---

This document was rendered at 2026-08-28T04:22:15.371Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/participantcontextifneeded.md](https://docs.livekit.io/reference/components/react/component/participantcontextifneeded.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-139"></a>
## Page 139: reference/components/react/component/participantloop
**Original URL:** https://docs.livekit.io/reference/components/react/component/participantloop  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/participantloop.md

LiveKit docs › React components › Components › ParticipantLoop

---

# ParticipantLoop

The `ParticipantLoop` component loops over an array of participants to create a context for every participant. This component takes exactly one child component as a template. By providing your own template as a child you have full control over the look and feel of your participant representations.

## Import

```typescript
import { ParticipantLoop } from "@livekit/components-react";

```

## Remarks

If you want to loop over individual tracks instead of participants, you can use the `TrackLoop` component.

## Usage

```tsx
const participants = useParticipants();
<ParticipantLoop participants={participants}>
  <ParticipantName />
</ParticipantLoop>;

```

## Properties

- **`children`** _(React.ReactNode)_: The template component to be used in the loop.

- **`participants`** _(Participant[])_: The participants to loop over. Use `useParticipants()` hook to get participants.

---

This document was rendered at 2026-08-28T04:22:15.395Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/participantloop.md](https://docs.livekit.io/reference/components/react/component/participantloop.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-140"></a>
## Page 140: reference/components/react/component/participantname
**Original URL:** https://docs.livekit.io/reference/components/react/component/participantname  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/participantname.md

LiveKit docs › React components › Components › ParticipantName

---

# ParticipantName

The `ParticipantName` component displays the name of the participant as a string within an HTML span element. If no participant name is undefined the participant identity string is displayed.

## Import

```typescript
import { ParticipantName } from "@livekit/components-react";

```

## Usage

```tsx
<ParticipantName />

```

---

This document was rendered at 2026-08-28T04:22:15.367Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/participantname.md](https://docs.livekit.io/reference/components/react/component/participantname.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-141"></a>
## Page 141: reference/components/react/component/participanttile
**Original URL:** https://docs.livekit.io/reference/components/react/component/participanttile  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/participanttile.md

LiveKit docs › React components › Components › ParticipantTile

---

# ParticipantTile

The `ParticipantTile` component is the base utility wrapper for displaying a visual representation of a participant. This component can be used as a child of the `TrackLoop` component or by passing a track reference as property.

## Import

```typescript
import { ParticipantTile } from "@livekit/components-react";

```

## Usage

### Using the

`ParticipantTile` component with a track reference:

```tsx
<ParticipantTile trackRef={trackRef} />

```

### Using the

`ParticipantTile` component as a child of the `TrackLoop` component:

```tsx
<TrackLoop>
  <ParticipantTile />
</TrackLoop>

```

## Properties

- **`disableSpeakingIndicator`** _(boolean)_ (optional): _(Optional)_

- **`onParticipantClick`** _((event: ParticipantClickEvent) => void)_ (optional): _(Optional)_

- **`trackRef`** _(TrackReferenceOrPlaceholder)_ (optional): _(Optional)_ The track reference to display.

---

This document was rendered at 2026-08-28T04:22:15.369Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/participanttile.md](https://docs.livekit.io/reference/components/react/component/participanttile.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-142"></a>
## Page 142: reference/components/react/component/prejoin
**Original URL:** https://docs.livekit.io/reference/components/react/component/prejoin  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/prejoin.md

LiveKit docs › React components › Components › PreJoin

---

# PreJoin

The `PreJoin` prefab component is normally presented to the user before he enters a room. This component allows the user to check and select the preferred media device (camera and microphone). On submit the user decisions are returned, which can then be passed on to the `LiveKitRoom` so that the user enters the room with the correct media devices.

## Import

```typescript
import { PreJoin } from "@livekit/components-react";

```

## Remarks

This component is independent of the `LiveKitRoom` component and should not be nested within it. Because it only accesses the local media tracks this component is self-contained and works without connection to the LiveKit server.

## Usage

```tsx
<PreJoin />

```

## Properties

- **`camLabel`** _(string)_ (optional): _(Optional)_

- **`debug`** _(boolean)_ (optional): _(Optional)_ Display a debug window for your convenience.

- **`defaults`** _(Partial<LocalUserChoices>)_ (optional): _(Optional)_ Prefill the input form with initial values.

- **`joinLabel`** _(string)_ (optional): _(Optional)_

- **`micLabel`** _(string)_ (optional): _(Optional)_

- **`onError`** _((error: Error) => void)_ (optional): _(Optional)_

- **`onSubmit`** _((values: LocalUserChoices) => void)_ (optional): _(Optional)_ This function is called with the `LocalUserChoices` if validation is passed.

- **`onValidate`** _((values: LocalUserChoices) => boolean)_ (optional): _(Optional)_ Provide your custom validation function. Only if validation is successful the user choices are passed to the onSubmit callback.

- **`persistUserChoices`** _(boolean)_ (optional): _(Optional)_ If true, user choices are persisted across sessions.

- **`userLabel`** _(string)_ (optional): _(Optional)_

- **`videoProcessor`** _(TrackProcessor<Track.Kind.Video>)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.395Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/prejoin.md](https://docs.livekit.io/reference/components/react/component/prejoin.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-143"></a>
## Page 143: reference/components/react/component/roomaudiorenderer
**Original URL:** https://docs.livekit.io/reference/components/react/component/roomaudiorenderer  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/roomaudiorenderer.md

LiveKit docs › React components › Components › RoomAudioRenderer

---

# RoomAudioRenderer

The `RoomAudioRenderer` component is a drop-in solution for adding audio to your LiveKit app. It takes care of handling remote participants’ audio tracks and makes sure that microphones and screen share are audible.

## Import

```typescript
import { RoomAudioRenderer } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom>
  <RoomAudioRenderer />
</LiveKitRoom>

```

## Properties

- **`muted`** _(boolean)_ (optional): _(Optional)_ If set to `true`, mutes all audio tracks rendered by the component.

- **`room`** _(Room)_ (optional): _(Optional)_

- **`volume`** _(number)_ (optional): _(Optional)_ Sets the volume for all audio tracks rendered by this component. By default, the range is between `0.0` and `1.0`.

---

This document was rendered at 2026-08-28T04:22:15.391Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/roomaudiorenderer.md](https://docs.livekit.io/reference/components/react/component/roomaudiorenderer.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-144"></a>
## Page 144: reference/components/react/component/roomcontext
**Original URL:** https://docs.livekit.io/reference/components/react/component/roomcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/roomcontext.md

LiveKit docs › React components › Components › RoomContext

---

# RoomContext

## Import

```typescript
import { RoomContext } from "@livekit/components-react";

```

---

This document was rendered at 2026-08-28T04:22:15.422Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/roomcontext.md](https://docs.livekit.io/reference/components/react/component/roomcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-145"></a>
## Page 145: reference/components/react/component/roomname
**Original URL:** https://docs.livekit.io/reference/components/react/component/roomname  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/roomname.md

LiveKit docs › React components › Components › RoomName

---

# RoomName

The `RoomName` component renders the name of the connected LiveKit room inside a span tag.

## Import

```typescript
import { RoomName } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom>
  <RoomName />
</LiveKitRoom>

```

---

This document was rendered at 2026-08-28T04:22:15.427Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/roomname.md](https://docs.livekit.io/reference/components/react/component/roomname.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-146"></a>
## Page 146: reference/components/react/component/sessionprovider
**Original URL:** https://docs.livekit.io/reference/components/react/component/sessionprovider  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/sessionprovider.md

LiveKit docs › React components › Components › SessionProvider

---

# SessionProvider

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

The `SessionProvider` component instantiates a SessionContext from the return of useSession

## Import

```typescript
import { SessionProvider } from "@livekit/components-react";

```

---

This document was rendered at 2026-08-28T04:22:15.417Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/sessionprovider.md](https://docs.livekit.io/reference/components/react/component/sessionprovider.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-147"></a>
## Page 147: reference/components/react/component/startaudio
**Original URL:** https://docs.livekit.io/reference/components/react/component/startaudio  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/startaudio.md

LiveKit docs › React components › Components › StartAudio

---

# StartAudio

The `StartAudio` component is only visible when the browser blocks audio playback. This is due to some browser implemented autoplay policies. To start audio playback, the user must perform a user-initiated event such as clicking this button. As soon as audio playback starts, the button hides itself again.

## Import

```typescript
import { StartAudio } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom>
  <StartAudio label="Click to allow audio playback" />
</LiveKitRoom>

```

## Properties

- **`label`** _(string)_: 

- **`room`** _(Room)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.414Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/startaudio.md](https://docs.livekit.io/reference/components/react/component/startaudio.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-148"></a>
## Page 148: reference/components/react/component/startmediabutton
**Original URL:** https://docs.livekit.io/reference/components/react/component/startmediabutton  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/startmediabutton.md

LiveKit docs › React components › Components › StartMediaButton

---

# StartMediaButton

The `StartMediaButton` component is only visible when the browser blocks media playback. This is due to some browser implemented autoplay policies. To start media playback, the user must perform a user-initiated event such as clicking this button. As soon as media playback starts, the button hides itself again.

## Import

```typescript
import { StartMediaButton } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom>
  <StartMediaButton label="Click to allow media playback" />
</LiveKitRoom>

```

## Properties

- **`label`** _(string)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.423Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/startmediabutton.md](https://docs.livekit.io/reference/components/react/component/startmediabutton.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-149"></a>
## Page 149: reference/components/react/component/toast
**Original URL:** https://docs.livekit.io/reference/components/react/component/toast  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/toast.md

LiveKit docs › React components › Components › Toast

---

# Toast

The `Toast` component is a rudimentary way to display a message to the user. This message should be short lived and not require user interaction. For example, displaying the current connection state like `ConnectionStateToast` does.

## Import

```typescript
import { Toast } from "@livekit/components-react";

```

## Usage

```tsx
<Toast>Connecting...</Toast>

```

---

This document was rendered at 2026-08-28T04:22:15.461Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/toast.md](https://docs.livekit.io/reference/components/react/component/toast.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-150"></a>
## Page 150: reference/components/react/component/trackloop
**Original URL:** https://docs.livekit.io/reference/components/react/component/trackloop  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/trackloop.md

LiveKit docs › React components › Components › TrackLoop

---

# TrackLoop

The `TrackLoop` component loops over tracks. It is for example a easy way to loop over all participant camera and screen share tracks. `TrackLoop` creates a `TrackRefContext` for each track that you can use to e.g. render the track.

## Import

```typescript
import { TrackLoop } from "@livekit/components-react";

```

## Usage

```tsx
const trackRefs = useTracks([Track.Source.Camera]);
<TrackLoop tracks={trackRefs}>
  <TrackRefContext.Consumer>
    {(trackRef) => trackRef && <VideoTrack trackRef={trackRef} />}
  </TrackRefContext.Consumer>
</TrackLoop>;

```

## Properties

- **`children`** _(React.ReactNode)_: The template component to be used in the loop.

- **`tracks`** _(TrackReference[] | TrackReferenceOrPlaceholder[])_: Track references to loop over. You can the use `useTracks()` hook to get TrackReferences.

---

This document was rendered at 2026-08-28T04:22:15.760Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/trackloop.md](https://docs.livekit.io/reference/components/react/component/trackloop.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-151"></a>
## Page 151: reference/components/react/component/trackmutedindicator
**Original URL:** https://docs.livekit.io/reference/components/react/component/trackmutedindicator  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/trackmutedindicator.md

LiveKit docs › React components › Components › TrackMutedIndicator

---

# TrackMutedIndicator

The `TrackMutedIndicator` shows whether the participant's camera or microphone is muted or not. By default, a muted/unmuted icon is displayed for a camera, microphone, and screen sharing track.

## Import

```typescript
import { TrackMutedIndicator } from "@livekit/components-react";

```

## Usage

```tsx
<TrackMutedIndicator trackRef={trackRef} />

```

## Properties

- **`trackRef`** _(TrackReferenceOrPlaceholder)_: 

- **`show`** _('always' | 'muted' | 'unmuted')_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.456Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/trackmutedindicator.md](https://docs.livekit.io/reference/components/react/component/trackmutedindicator.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-152"></a>
## Page 152: reference/components/react/component/trackrefcontext
**Original URL:** https://docs.livekit.io/reference/components/react/component/trackrefcontext  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/trackrefcontext.md

LiveKit docs › React components › Components › TrackRefContext

---

# TrackRefContext

This context provides a `TrackReferenceOrPlaceholder` to all child components.

## Import

```typescript
import { TrackRefContext } from "@livekit/components-react";

```

---

This document was rendered at 2026-08-28T04:22:15.468Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/trackrefcontext.md](https://docs.livekit.io/reference/components/react/component/trackrefcontext.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-153"></a>
## Page 153: reference/components/react/component/tracktoggle
**Original URL:** https://docs.livekit.io/reference/components/react/component/tracktoggle  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/tracktoggle.md

LiveKit docs › React components › Components › TrackToggle

---

# TrackToggle

With the `TrackToggle` component it is possible to mute and unmute your camera and microphone. The component uses an html button element under the hood so you can treat it like a button.

## Import

```typescript
import { TrackToggle } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom>
  <TrackToggle source={Track.Source.Microphone} />
  <TrackToggle source={Track.Source.Camera} />
</LiveKitRoom>

```

## Properties

- **`source`** _(T)_: 

- **`captureOptions`** _(CaptureOptionsBySource<T>)_ (optional): _(Optional)_

- **`initialState`** _(boolean)_ (optional): _(Optional)_

- **`onChange`** _((enabled: boolean, isUserInitiated: boolean) => void)_ (optional): _(Optional)_ Function that is called when the enabled state of the toggle changes. The second function argument `isUserInitiated` is `true` if the change was initiated by a user interaction, such as a click.

- **`onDeviceError`** _((error: Error) => void)_ (optional): _(Optional)_

- **`publishOptions`** _(TrackPublishOptions)_ (optional): _(Optional)_

- **`showIcon`** _(boolean)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.458Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/tracktoggle.md](https://docs.livekit.io/reference/components/react/component/tracktoggle.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-154"></a>
## Page 154: reference/components/react/component/videoconference
**Original URL:** https://docs.livekit.io/reference/components/react/component/videoconference  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/videoconference.md

LiveKit docs › React components › Components › VideoConference

---

# VideoConference

The `VideoConference` ready-made component is your drop-in solution for a classic video conferencing application. It provides functionality such as focusing on one participant, grid view with pagination to handle large numbers of participants, basic non-persistent chat, screen sharing, and more.

## Import

```typescript
import { VideoConference } from "@livekit/components-react";

```

## Remarks

The component is implemented with other LiveKit components like `FocusContextProvider`, `GridLayout`, `ControlBar`, `FocusLayoutContainer` and `FocusLayout`. You can use these components as a starting point for your own custom video conferencing application.

## Usage

```tsx
<LiveKitRoom>
  <VideoConference />
<LiveKitRoom>

```

## Properties

- **`chatMessageDecoder`** _(MessageDecoder)_ (optional): _(Optional)_

- **`chatMessageEncoder`** _(MessageEncoder)_ (optional): _(Optional)_

- **`chatMessageFormatter`** _(MessageFormatter)_ (optional): _(Optional)_

- **`SettingsComponent`** _(React.ComponentType)_ (optional): _(Optional)_

---

This document was rendered at 2026-08-28T04:22:15.461Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/videoconference.md](https://docs.livekit.io/reference/components/react/component/videoconference.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-155"></a>
## Page 155: reference/components/react/component/videotrack
**Original URL:** https://docs.livekit.io/reference/components/react/component/videotrack  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/videotrack.md

LiveKit docs › React components › Components › VideoTrack

---

# VideoTrack

The `VideoTrack` component is responsible for rendering participant video tracks like `camera` and `screen_share`. This component must have access to the participant's context, or alternatively pass it a `Participant` as a property.

## Import

```typescript
import { VideoTrack } from "@livekit/components-react";

```

## Usage

```tsx
<VideoTrack trackRef={trackRef} />

```

## Properties

- **`manageSubscription`** _(boolean)_ (optional): _(Optional)_

- **`onSubscriptionStatusChanged`** _((subscribed: boolean) => void)_ (optional): _(Optional)_

- **`onTrackClick`** _((evt: ParticipantClickEvent) => void)_ (optional): _(Optional)_

- **`trackRef`** _(TrackReference)_ (optional): _(Optional)_ The track reference of the track to render.

---

This document was rendered at 2026-08-28T04:22:15.486Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/videotrack.md](https://docs.livekit.io/reference/components/react/component/videotrack.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

<a name="page-156"></a>
## Page 156: reference/components/react/component/voiceassistantcontrolbar
**Original URL:** https://docs.livekit.io/reference/components/react/component/voiceassistantcontrolbar  
**Source MD URL:** https://docs.livekit.io/reference/components/react/component/voiceassistantcontrolbar.md

LiveKit docs › React components › Components › VoiceAssistantControlBar

---

# VoiceAssistantControlBar

> ℹ️ **Note**
> 
> This feature is under active development and may change based on developer feedback and real-world usage.

## Import

```typescript
import { VoiceAssistantControlBar } from "@livekit/components-react";

```

## Usage

```tsx
<LiveKitRoom ... >
  <VoiceAssistantControlBar />
</LiveKitRoom>

```

## Properties

- **`controls`** _(VoiceAssistantControlBarControls)_ (optional): **_(BETA)_** _(Optional)_

**_(BETA)_** _(Optional)_

- **`undefined`** _(undefined)_: 

- **`saveUserChoices`** _(boolean)_ (optional): **_(BETA)_** _(Optional)_ If `true`, the user's device choices will be persisted. This will enables the user to have the same device choices when they rejoin the room.

---

This document was rendered at 2026-08-28T04:22:15.523Z.
For the latest version of this document, see [https://docs.livekit.io/reference/components/react/component/voiceassistantcontrolbar.md](https://docs.livekit.io/reference/components/react/component/voiceassistantcontrolbar.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).

---

