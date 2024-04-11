from talon import Context, Module, actions

# App definition
mod = Module()
mod.apps.xfce_terminal = """
os: linux
and app.exe: xfce4-terminal
os: linux
and app.name: Xfce4-terminal
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: xfce_terminal
app.name: xfce-terminal
"""
