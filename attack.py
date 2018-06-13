import mosaik_api

meta = {
    'models': {
        'Attack': {
            'public': True,
            'params': ['target_attr'],
            'attrs': ['P_out_val'],
        },
    },
}

class Attack(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(meta)
        self.units = {}

    def init(self, sid, step_size=15*60):
        self.sid = sid
        self.step_size = step_size

        return self.meta

    def create(self, num, model, **model_params):
        n_units = len(self.units)
        entities = []
        for i in range(n_units, n_units + num):
            eid = 'Attack-%d' % i
            self.units[eid] = model_params
            entities.append({'eid': eid, 'type': model  })
        return entities

    def step(self, time, inputs):
        commands = {}
        for eid, attrs in inputs.items():
            # measure = 0
            for attr, vals in attrs.items():
                if attr == 'P_out_val':
                    for src_id, val in vals.items():
                        target_id = src_id
                        values = val
            if eid not in commands:
                commands[eid] = {}
            target_attr = self.units[eid]['target_attr']

            if target_id not in commands[eid]:
                commands[eid][target_id] = {}
            commands[eid][target_id][target_attr] = 0
        print("COMMANDS", commands)
        yield self.mosaik.set_data(commands)

        return time + self.step_size

def main(self):
    return mosaik_api.start_simulation(Attack(), 'example attack')

if __name__ == '__main__':
    main()