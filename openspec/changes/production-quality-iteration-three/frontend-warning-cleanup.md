# Frontend Warning And 404 Cleanup

Date: 2026-06-17

## Changes

- Replaced deprecated Ant Design `Space.direction` usage with `Space.orientation`.
- Replaced deprecated `Alert.message` usage with `Alert.title`.
- Replaced deprecated `Spin.tip` usage with `Spin.description`.
- Replaced deprecated `Tooltip.overlayClassName` usage with `Tooltip.classNames.root`.
- Replaced deprecated `Drawer.width` usage with `Drawer.size` for existing fixed-width drawers.
- Added an explicit SVG favicon link to `apps/admin-web/index.html` using the existing `public/sysu-logo.svg`.

## 404 Diagnosis

The generic browser-smoke 404 was traced to `http://localhost:5174/favicon.ico`.
After declaring the existing SVG logo as the page icon, representative browser smoke produced no console messages, no 404 responses, and no failed requests.

## Verification

- `rg` found no remaining `direction=`, `overlayClassName=`, `tip=`, `message=`, or Drawer `width=` usage in `apps/admin-web/src`.
- `npm run typecheck`: PASS
- `npm test`: PASS, 7 tests
- `npm run build`: PASS
- Browser smoke against `http://localhost:5174` loaded overview, videos, learning assistant, question banks, and analytics with no console warnings/errors, no 404s, and no failed requests.
