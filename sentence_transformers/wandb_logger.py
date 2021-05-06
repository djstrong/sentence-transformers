from pathlib import Path

try:
    import wandb
    from wandb import init, finish
except ImportError:
    wandb = None


class WandbLogger:
    def __init__(self, project, name=None, config={}, entity=None):
        self.wandb_run = None
        self.log_dict = {}
        if wandb:
            self.wandb_run = (
                wandb.init(project=project, name=name, config=config, entity=entity)
                if not wandb.run
                else wandb.run
            )

    def log(self, log_dict, prefix=""):
        if not isinstance(log_dict, dict):
            return
        for key, value in log_dict.items():
            self.log_dict[f"{prefix}{key}"] = value

    def flush(self):
        self.wandb_run.log(self.log_dict)
        self.log_dict = {}

    def log_config(self, config_dict):
        self.wandb_run.config.update(config_dict)

    def finish(self):
        self.wandb_run.finish()