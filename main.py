from modules.logger import Logger

# Logger start
logger: Logger = Logger(debug=True)

logger.log("First log", level="info")
logger.log("Second log", level="info")
logger.log("Third log", level="error")
logger.log("Fourth log", level="fatal")
logger.log("Fifth log", level="debug")

logger.exit_logger()

print("Total logs collected:", logger.get_log_count())

for level in logger.get_log_levels():
    print(f"Total {level} logs: {logger.level.get(level)['count']}")
