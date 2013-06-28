# USE_SPECIFIERS { _num_source_neurons, _num_target_neurons, _synaptic_pre, _synaptic_post, _pre_synaptic, _post_synaptic }

import numpy as np

for i in xrange(_num_source_neurons):
    j = np.arange(_num_target_neurons)
    
    {% for line in code_lines %}
    {{line}}
    {% endfor %}
    
    _cond_nonzero = _cond.nonzero()[0]
    _cur_num_synapses = len(_synaptic_pre)
    _numnew = len(_cond_nonzero)
    _new_num_synapses = _cur_num_synapses + _numnew
    _synaptic_pre.resize(_new_num_synapses)
    _synaptic_post.resize(_new_num_synapses)
    _synaptic_pre[_cur_num_synapses:] = i
    _synaptic_post[_cur_num_synapses:] = _cond_nonzero

    _new_synapses = np.arange(_cur_num_synapses, _new_num_synapses)
    _source_synapses = _pre_synaptic[i]
    _cur_num_source_synapses = len(_source_synapses)
    _source_synapses.resize(_cur_num_source_synapses + _numnew)
    _source_synapses[_cur_num_source_synapses:] = _new_synapses
    for _new_synapse, _target in zip(_new_synapses, _cond_nonzero):
        _target_synapses = _post_synaptic[_target]
        _cur_num_target_synapses = len(_target_synapses)
        _target_synapses.resize(_cur_num_target_synapses + 1)
        _target_synapses[_cur_num_target_synapses] = _new_synapse