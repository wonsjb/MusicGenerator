import mido


for i, port_name in enumerate(mido.get_output_names()):
    print(i, port_name)
