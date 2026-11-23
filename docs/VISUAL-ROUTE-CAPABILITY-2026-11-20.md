# Remote Desktop visual capability check — 2026-11-20

## Result and scope

Remote Desktop Commander (RDC) provides a tested read-only route from the connected Windows primary screen to a locally decoded PNG. A cloud browser is not required for this capture. No native RDC screenshot or desktop-input tool was exposed in the inspected tool inventory; the tested route uses its documented process capability and existing Windows assemblies.

This was a bounded capability check, not an audit of desktop content or an application acceptance test. The device ID/name, user paths, screenshot contents and other personal metadata are deliberately absent from this document. The configured operating-guide version remains 0.0.6.

## Observed evidence

| Check | Actual result | Boundary |
| --- | --- | --- |
| `list_devices` | One device online; RDC app 0.3.3 | Point-in-time availability, not a permanent connection guarantee |
| `get_config` | Windows (`win32`), default shell `powershell.exe` | Configuration is not screenshot proof |
| `start_process` read-only OS query | Win32NT; PowerShell 5.1; interactive Session 1 | No app/process inventory or user-content scan |
| Existing command presence | Node and Python commands present | Their package sets were not inspected |
| Existing assemblies | `System.Drawing`, `System.Windows.Forms`, `UIAutomationClient`, `UIAutomationTypes` loaded | Availability alone does not prove capture or interaction |
| Screen metadata | One primary screen, 2560 × 1440 | Native desktop pixels; no browser viewport or DPI claim |
| UI Automation metadata | Root element available, `ControlType.Pane`; `FindFirst` method present | No window titles, child elements, app text or control patterns inspected |
| Capture APIs | Four `Graphics.CopyFromScreen` overloads; stream PNG encoder present | Reflection check, followed by a real capture below |
| Real capture | Primary screen copied into an in-memory bitmap; PNG emitted as base64 through RDC process output | One capture; no remote filesystem write |
| Local decode | PNG decoded successfully; 2560 × 1440; 418,436 bytes; nonempty and nonuniform | Image integrity checked; content was not visually audited or shown to the user |
| Desktop input | Not run | No click, key, focus, navigation, resize or app mutation tested |

The process calls finished successfully. No dependencies were installed, configuration changed or user files modified. No browser session was initialized.

## Concrete available route

1. Discover the current RDC tool inventory and call `mcp__codex_apps__remote_desktop_commander_list_devices`. Select the intended online device by the returned ID; keep identifiers in transient execution context rather than shared guidance.
2. Read the selected device configuration and query only needed OS/session/screen capabilities with `mcp__codex_apps__remote_desktop_commander_start_process`. Use that device's shell syntax. In this check the shell was Windows PowerShell.
3. Capture the relevant authorized screen/window to memory using the existing Windows API. Emit a PNG through the process result; do not persist it on the remote device merely to transfer it.
4. Decode the returned bytes in local temporary scratch, verify PNG integrity and dimensions, and inspect the image with the host's image-viewing capability when the requested target and visual-review scope are established. This check exercised decoding only; it did not inspect app content.
5. For an application audit, establish the exact app/build, selected state, viewport and display scale before making layout claims. For interactions, obtain initial visual/scoped UI state, perform only authorized input, then inspect the resulting state. No such input capability was tested here.

The screenshot bridge used the following Windows operations, inside `start_process` with the selected device ID. The snippet is the capture portion, not a new remote dependency or an assertion of a native RDC screenshot tool:

```powershell
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms
$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bitmap = New-Object System.Drawing.Bitmap($bounds.Width, $bounds.Height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
try {
    $graphics.CopyFromScreen(
        $bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
    $stream = New-Object System.IO.MemoryStream
    try {
        $bitmap.Save($stream, [System.Drawing.Imaging.ImageFormat]::Png)
        $bytes = $stream.ToArray()
        Write-Output ('RDC_CAPTURE_METADATA:' + ([ordered]@{
            width = $bounds.Width
            height = $bounds.Height
            pngBytes = $bytes.Length
        } | ConvertTo-Json -Compress))
        Write-Output ('RDC_CAPTURE_BASE64:' +
            [System.Convert]::ToBase64String($bytes))
    } finally { $stream.Dispose() }
} finally {
    $graphics.Dispose()
    $bitmap.Dispose()
}
```

Keep base64 and image data out of chat/status output. Parse marker-delimited capture data from the tool result. If a call is still running, read that same call/process result rather than starting another capture. The tested image was about 558 KB as base64; larger displays/content may need bounded output handling. Output-size limits beyond this capture were not tested.

## Recommended workflow changes

These recommendations are inputs to the parent's integration; this document does not modify the procedures.

| Existing owner | Smallest useful clarification |
| --- | --- |
| `guidance/playbooks/work-cycle.md`, route selection | Establish the intended observation environment and user's preference before selecting tools. Discover relevant connected-device capabilities before choosing another environment or declaring rendering unavailable. A failed local renderer blocks that route, not every available visual route. |
| `guidance/playbooks/work-cycle.md`, verification | Record separately: tool exposed, device online, API/module present, capture obtained, image inspected, interaction exercised. Require the level needed by the claim. |
| `guidance/playbooks/delegation.md` | Pass the target environment, capability results/time, permitted observations/input and desktop owner. Workers verify their own tool exposure; a parent's access is not inherited proof. Keep one writer on a shared desktop and delegate read-only evidence analysis independently. |
| `skills/audit-ui-ux/SKILL.md`, interface inspection | Select the actual authorized surface. For a user's Windows app, prefer the verified RDC observation route when it matches the request. Do not silently substitute a cloud-browser session with a different app, build, account or state. Preserve the source-only/visual/interaction evidence distinctions. |
| `skills/test-user-flows/SKILL.md`, observation surface | Distinguish screenshot transport from native input support. Existing Windows UI Automation is a possible scoped observation route; root availability does not prove target controls or interaction patterns. Verify only the controls needed for the accepted journey. |
| `skills/design-ui-improvements/SKILL.md`, baseline/render checks | Use an inspected baseline from the actual environment when available; keep proposed artifacts and runtime evidence separate. A different rendered mockup cannot close acceptance for the live Windows interface. |

## Remaining limits

- No target application or app state was inspected; no UI findings follow from this capability check.
- No UI input, target control pattern, keyboard/focus behavior, browser DOM/DevTools access or save operation was tested.
- No screenshot was captured at 1280 × 800. The previous synthetic-table render failure remains unresolved for that exact requested surface.
- The connected Windows desktop does not automatically contain or render the scratch HTML fixture. Transferring/opening it would be a separate authorized action.
- Actual screen captures can contain unrelated private content. Scope later captures to the requested app/window when feasible, avoid broad UI-tree scans, and do not publish incidental content.
- Locked/disconnected sessions, additional displays, display scaling, elevated/secure desktops and other devices were not tested.
- The temporary image is evidence of the bridge only; do not commit it, embed it here or attach it to a user-facing report without a concrete need.

## Sources inspected

- Current RDC tool metadata for `list_devices`, `get_config`, `start_process`, `read_file` and the complete RDC tool-name inventory.
- Actual bounded RDC calls and PNG decode described above.
- `guidance/playbooks/work-cycle.md` and `guidance/playbooks/delegation.md`.
- `skills/audit-ui-ux/SKILL.md`, `references/criteria.md` and `references/findings.md`.
- `skills/test-user-flows/SKILL.md` and `references/flow-evidence.md`.
- `skills/design-ui-improvements/SKILL.md`.

No external source lookup was needed to claim these point-in-time tool results. The screenshot operation was tested directly rather than inferred from installation or documentation.
