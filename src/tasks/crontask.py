import luigi


class CronTask(luigi.Task):
    def run(self):
        print("123")
