import unittest
from unittest.mock import patch
from Pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Gabriel', 'Machado')

    def test_pessoas_attr_nome_tem_o_valo_correto(self):
        self.assertEqual(self.p1.nome, 'Gabriel')

    def test_pessoas_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoas_attr_sobrenomenome_tem_o_valo_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Machado')

    def test_pessoas_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoas_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falho_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERROR 404')
            self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucedido_e_falho_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)