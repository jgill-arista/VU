pip3 install pyavd
pip3 install pyavd[ansible]
pip3 install pyyaml
pip3 install pyeapi

./pyavd_backup_studio_inputs.py --token-file token.tok --apiserver www.cv-prod-us-central1-c.arista.io
./pyavd_push_configlet.py --token-file token.tok --apiserver www.cv-prod-us-central1-c.arista.io
