
from dataclasses import dataclass, asdict

@dataclass
class ModelResult:
    "A custom struct for storing model evaluation results."
    name: None

    
from metaflow import FlowSpec, step

class SimpleBranchingFlow(FlowSpec):

    @step
    def start(self):
        self.next(self.a, self.b)

    @step
    def a(self):
        self.from_a = 5
        self.result_a = ModelResult("1")

        self.next(self.join)

    @step
    def b(self):
        self.from_b = 7
        self.result_b = ModelResult("2")

        self.next(self.join)


    def join_old(self, inputs):

        # print('from_a is %d' % self.from_a)
        print('result from a is: %d' % inputs.a.result_a)
        print('results from b is: ' + str(inputs.b.results_a))

        print('from_a is %d' % inputs.a.from_a)
        print('y from b is %d' % inputs.b.y)
        # print('from_a is %d' % self.from_a)

        self.x = inputs.a.x
        self.merge_artifacts(inputs, exclude=['y'])
        print('x is %s' % self.x)
        print('pass_down is %s' % self.pass_down)
        print('common is %d' % self.common)
        print('from_a is %d' % self.from_a)
        print('from_a is %d' % self.from_a)
        self.next(self.end)


    @step
    def join(self, inputs):
        self.merge_artifacts(inputs)
        print(self.from_a)
        print(self.result_a.name)
        print(self.from_b)
        print(self.result_b.name)

        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    SimpleBranchingFlow()
