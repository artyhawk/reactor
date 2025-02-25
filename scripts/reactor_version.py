app_title = "ReActor"
version_flag = "v0.6.0-a4"

from scripts.reactor_logger import logger, get_Run, set_Run

is_run = get_Run()

if not is_run:
    logger.status(f"Running {version_flag}")
    set_Run(True)
