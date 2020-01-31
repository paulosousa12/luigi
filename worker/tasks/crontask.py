import luigi
from worker.tasks.example import RunExampleTask
from luigi.local_target import LocalTarget


class CronTask(luigi.Task):
    def requires(self):
        for i in range(10):
            yield RunExampleTask(i)

    def run(self):
        with self.output().open('w') as f:
            f.write('All done!')

    def output(self):
        return LocalTarget('tmp/RunAllTasks.txt')
