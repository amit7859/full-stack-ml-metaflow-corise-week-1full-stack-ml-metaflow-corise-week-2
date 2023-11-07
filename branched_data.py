from metaflow import FlowSpec, step

class MergeArtifactsFlow(FlowSpec):

    @step
    def start(self):
        self.pass_down = 'a'
        self.next(self.a, self.b)

    @step
    def a(self):
        self.common = 5
        self.x = 1
        self.y = 3
        self.from_a = 6
        self.result_a = 9
        self.next(self.join)

    @step
    def b(self):
        self.common = 5
        self.x = 2
        self.y = 4
        self.results_a = [4, 5]
        self.next(self.join)

    @step
    def join(self, inputs):

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
    def end(self):
        pass

if __name__ == '__main__':
    MergeArtifactsFlow()