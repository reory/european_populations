"""
Post-processes the Altair-saved HTML to wire up scroll-to-zoom and
click-drag-to-pan directly against the Vega view's signals.

Key fix: vega-embed 7 renders SVG by default, not canvas.
Attach events to the #vis container div instead, which always exists.
"""

import re
from loguru import logger

# ----------------------------------------------------------------------------
# JavaScript for zoom + pan controls
MOUSE_CONTROLS_JS = """
  .then(function(result) {
    var view = result.view;

    console.log('zoom_scale:', view.signal('zoom_scale'));
    console.log('pan_x:',     view.signal('pan_x'));
    console.log('pan_y:',     view.signal('pan_y'));

    // Attach to the #vis div — works for both SVG and canvas renderers
    var container = document.getElementById('vis');
    container.style.cursor = 'grab';

    // ── Scroll to zoom ────────────────────────────────────────────────────
    container.addEventListener('wheel', function(e) {
      e.preventDefault();
      var current  = view.signal('zoom_scale');
      var factor   = e.deltaY < 0 ? 1.12 : 0.89;
      var newScale = Math.max(150, Math.min(6000, current * factor));
      console.log('zoom:', current, '->', newScale);
      view.signal('zoom_scale', newScale);
      view.runAsync();
    }, { passive: false });

    // ── Click & drag to pan ───────────────────────────────────────────────
    var dragging = false, startX, startY, originPanX, originPanY;

    container.addEventListener('mousedown', function(e) {
      dragging   = true;
      startX     = e.clientX;
      startY     = e.clientY;
      originPanX = view.signal('pan_x');
      originPanY = view.signal('pan_y');
      container.style.cursor = 'grabbing';
    });

    window.addEventListener('mousemove', function(e) {
      if (!dragging) return;
      view.signal('pan_x', originPanX + (e.clientX - startX));
      view.signal('pan_y', originPanY + (e.clientY - startY));
      view.runAsync();
    });

    window.addEventListener('mouseup', function() {
      dragging = false;
      container.style.cursor = 'grab';
    });
  })"""
# -----------------------------------------------------------------------------


def inject_mouse_controls(html_path: str) -> None:
    """Add A mouse-interaction script into an HTML file"""

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Matches a JS .catch(...) error handler
    pattern = r"(\s*\.catch\(error\s*=>\s*showError\(el,\s*error\)\);)"
    replacement = MOUSE_CONTROLS_JS + r"\1"

    # Apply regex replacement once and return updated HTML plus number of substitutions
    new_html, count = re.subn(pattern, replacement, html, count=1)

    # Warn and exit early if no matching .catch() block was found to patch
    if count == 0:
        logger.info(
            "inject_controls WARNING: could not find .catch() block — "
            "HTML was not modified."
        )
        return

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    logger.info(f"inject_controls: mouse zoom/pan injected into {html_path}")
