# gitops-flask-kubernetes/tests/test_smoke.py

import yaml
from kubernetes import client, config

config.load_kube_config(context="kind-cluster1")


class TestSmoke:
    def setup_class(self):
        self.core_v1 = client.CoreV1Api()

    def test_create_namespace(self):
        with open("namespace.yaml") as f:
            namespace = yaml.safe_load(f)
        response = self.core_v1.create_namespace(body=namespace)
        result = self.core_v1.read_namespace(name="test-namespace")
        assert "test-namespace" == result.metadata.name

def teardown_class(self):
        self.core_v1.delete_namespace(name="test-namespace")
