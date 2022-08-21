from kubernetes import client, config
import pytest
import yaml
from conftest import option

config.load_kube_config(context=option.context)


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


# new
@pytest.mark.skipif(option.context in ("kind-cluster2", "kind-cluster3"), reason="only deployed on development")
class TestGitOpsConditional:
    def setup_class(self):
        self.core_v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()
  
    def test_flask_internal_application_deployment(self):
        deployment = self.apps_v1.read_namespaced_deployment(name="flask-internal", namespace="test-namespace")
        assert "flask-internal" == deployment.metadata.name
        assert "test-namespace" == deployment.metadata.namespace
    
    def test_flask_internal_application_service(self):
        service = self.core_v1.read_namespaced_service(name="flask-internal", namespace="test-namespace")
        assert "flask-internal" == service.metadata.name
        assert "test-namespace" == service.metadata.namespace

    def test_flask_service2_application_namespace(self):
        namespace = self.core_v1.read_namespace(name="service2")
        assert "service2" == namespace.metadata.name

    def test_flask_service2_application_deployment(self):
        deployment = self.apps_v1.read_namespaced_deployment(name="flask-different-namespace", namespace="service2")
        assert "flask-different-namespace" == deployment.metadata.name
        assert "service2" == deployment.metadata.namespace

    def test_flask_service2_application_service(self):
        service = self.core_v1.read_namespaced_service(name="flask-different-namespace", namespace="service2")
        assert "flask-different-namespace" == service.metadata.name
        assert "service2" == service.metadata.namespace
