-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 16-Jul-2019 às 15:28
-- Versão do servidor: 5.7.25
-- versão do PHP: 7.1.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `escola`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos`
--

CREATE TABLE `alunos` (
  `id_aluno` int(11) NOT NULL,
  `cpf` varchar(15) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `nascimento` varchar(10) NOT NULL,
  `endereco` varchar(200) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `estado` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `alunos`
--

INSERT INTO `alunos` (`id_aluno`, `cpf`, `nome`, `nascimento`, `endereco`, `cidade`, `estado`) VALUES
(1, '111.222.333-44', 'Lucas Maia', '1111-22-33', 'R. Icebom, 123', 'Pouso Alegre', 'MG'),
(2, '222.333.444-55', 'Deidata Naruto', '1997-02-12', 'FAI', 'Aldeia da Folha', 'MG'),
(4, '444.555.666-77', 'Victória Oliveira', '1926-12-21', 'morro', 'Campos do Jordão', 'SP'),
(6, '666.777.888-99', 'Izis de Cássia', '1995-01-01', 'Narnia', 'Cachoeira de Minas', 'MG'),
(7, '12345678911', 'joão pedro', '2019-03-05', 'R teste BD', 'python', 'ND'),
(8, '12345678956', 'karem rodrigues', '2019-03-05', 'R teste BD', 'python', 'ND');

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunoscursos`
--

CREATE TABLE `alunoscursos` (
  `id_alunosCursos` int(11) NOT NULL,
  `curso` int(11) DEFAULT NULL,
  `aluno` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `alunoscursos`
--

INSERT INTO `alunoscursos` (`id_alunosCursos`, `curso`, `aluno`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 4, 2),
(4, 7, 2),
(7, 6, 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `cursos`
--

CREATE TABLE `cursos` (
  `id_curso` int(11) NOT NULL,
  `nome` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `cursos`
--

INSERT INTO `cursos` (`id_curso`, `nome`) VALUES
(1, 'Matemática'),
(2, 'Sistemas Operacionais'),
(3, 'Algoritmos'),
(4, 'Fundamentos da Administração'),
(5, 'Comunicação e Expressão'),
(6, 'Ferramentas Computacionais'),
(7, 'Empreendedorismo e Inovação'),
(8, 'Matemática');

-- --------------------------------------------------------

--
-- Estrutura da tabela `notas`
--

CREATE TABLE `notas` (
  `idnotas` int(11) NOT NULL,
  `nota` decimal(5,2) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `aluno_curso` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `notas`
--

INSERT INTO `notas` (`idnotas`, `nota`, `descricao`, `aluno_curso`) VALUES
(14, '25.75', 'Prova 1', 1),
(15, '50.25', 'Prova 2', 1),
(16, '40.00', 'Prova 1', 2),
(17, '70.00', 'Reposicao de Prova', 2),
(18, '20.50', 'Atividade Complementar', 3),
(19, '40.85', 'Atividade Complementar', 3),
(20, '52.00', 'Prova 1', 4),
(21, '10.00', 'Atividade Complementar', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`id_aluno`);

--
-- Indexes for table `alunoscursos`
--
ALTER TABLE `alunoscursos`
  ADD PRIMARY KEY (`id_alunosCursos`),
  ADD KEY `fk_alunos` (`aluno`),
  ADD KEY `fk_cursos` (`curso`);

--
-- Indexes for table `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id_curso`);

--
-- Indexes for table `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`idnotas`),
  ADD KEY `fk_materia` (`aluno_curso`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alunos`
--
ALTER TABLE `alunos`
  MODIFY `id_aluno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `alunoscursos`
--
ALTER TABLE `alunoscursos`
  MODIFY `id_alunosCursos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `notas`
--
ALTER TABLE `notas`
  MODIFY `idnotas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `alunoscursos`
--
ALTER TABLE `alunoscursos`
  ADD CONSTRAINT `fk_alunos` FOREIGN KEY (`aluno`) REFERENCES `alunos` (`id_aluno`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_cursos` FOREIGN KEY (`curso`) REFERENCES `cursos` (`id_curso`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `fk_materia` FOREIGN KEY (`aluno_curso`) REFERENCES `alunoscursos` (`id_alunosCursos`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
