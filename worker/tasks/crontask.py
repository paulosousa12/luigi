import luigi
import datetime
from luigi.local_target import LocalTarget


class CronTask(luigi.Task):
    def run(self):
        with self.output().open('w') as f:
            f.write("{}\n".format(datetime.datetime.now()))

    def output(self):
        return LocalTarget('tmp/RunAllTasks.txt')
