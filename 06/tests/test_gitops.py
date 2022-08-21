from kubernetes import client, config
import pytest
import yaml

config.load_kube_config(context="kind-cluster1")

class TestGitOps:
    def setup_class(self):
        self.core_v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()
        self.networking_v1beta1 = client.NetworkingV1beta1Api()

    def test_flask_application_namespace(self):
        namespace = self.core_v1.read_namespace(name="test-namespace")
        assert "test-namespace" == namespace.metadata.name

    def test_flask_application_deployment(self):
        deployment = self.apps_v1.read_namespaced_deployment(name="flask", namespace="test-namespace")
        assert "flask" == deployment.metadata.name
        assert "test-namespace" == deployment.metadata.namespace

    def test_flask_application_service(self):
        service = self.core_v1.read_namespaced_service(name="flask", namespace="test-namespace")
        assert "flask" == service.metadata.name
        assert "test-namespace" == service.metadata.namespace

    def test_flask_application_ingress(self):
        ingress = self.networking_v1beta1.read_namespaced_ingress(name="flask", namespace="test-namespace")
        assert "flask" == ingress.metadata.name
        assert "test-namespace" == ingress.metadata.namespace
