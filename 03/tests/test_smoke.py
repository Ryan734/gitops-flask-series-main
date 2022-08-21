from kubernetes import client, config
import pytest
import yaml

config.load_kube_config(context="kind-cluster1")

class TestSmoke:
    def setup_class(self):
        self.core_v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()

    def test_create_namespace(self):
        with open("namespace.yaml") as f:
            namespace = yaml.safe_load(f)
        response = self.core_v1.create_namespace(body=namespace)
        result = self.core_v1.read_namespace(name="test-namespace")
        assert "test-namespace" == result.metadata.name

    def test_create_deployment(self):
        with open("deployment.yaml") as f:
            deployment = yaml.safe_load(f)
        response = self.apps_v1.create_namespaced_deployment(body=deployment, namespace="test-namespace")
        result = self.apps_v1.read_namespaced_deployment(name="flask", namespace="test-namespace")
        assert "flask" == result.metadata.name
        assert "test-namespace" == result.metadata.namespace

    def teardown_class(self):
        self.core_v1.delete_namespace(name="test-namespace")
