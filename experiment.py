"""Tournament play experiment."""
from __future__ import absolute_import
import net_builder
import gp
import cPickle
# Use cuda ?
CUDA_ = True

if __name__=='__main__':
    # setup a tournament!
    nb_evolution_steps = 3
    tournament = \
        gp.TournamentOptimizer(
            population_sz=10,
            init_fn=net_builder.randomize_network,
            mutate_fn=net_builder.mutate_net,
            eval_fn=None,
            nb_workers=2)

    for i in range(nb_evolution_steps):
        print('\nEvolution step:{}'.format(i))
        print('================')
        tournament.step()
        # keep track of the experiment results & corresponding architectures
        name = "tourney_{}".format(i)
        cPickle.dump(tournament.stats, open(name + '.stats','wb'))
        cPickle.dump(tournament.history, open(name +'.pop','wb'))