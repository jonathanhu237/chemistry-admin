# Manual Phone / WeChat WebView Checklist

Use this checklist before a student H5 release or after changes to overlays, inputs, fixed actions, or safe-area spacing.

## Devices / Containers

- Android Chrome or Chromium-based mobile browser.
- iOS Safari when available.
- WeChat in-app browser / WebView when available.

## Viewports And Orientation

- Test in portrait orientation.
- Confirm the app stays a centered phone layout on wide desktop preview.
- Confirm no page-level horizontal scroll appears on login, password, learning home, point detail, AI chat, feedback, and assessment/summary flows.

## Keyboard Checks

- Login: focus student id and password fields; submit remains reachable.
- Initial password: focus both password fields; submit remains reachable.
- AI chat: open the panel, focus the input, send button remains reachable.
- Feedback: open the panel, focus textarea, submit button remains reachable.
- Assessment fill answer: focus input; sticky submit remains reachable.

## Safe-Area Checks

- Bottom fixed/floating entries are not cut off by browser chrome or rounded corners.
- AI and feedback entries do not overlap each other.
- Completion and submit actions can scroll above floating entries.
- Close/back/logout buttons are reachable by touch without hover.

## Known Limit

Desktop automation cannot fully emulate WeChat keyboard and browser chrome behavior. Treat this manual checklist as the release gate for keyboard and safe-area confidence.
