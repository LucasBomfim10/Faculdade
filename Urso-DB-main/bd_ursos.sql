create database ursos;
use ursos;


CREATE TABLE Clima (
 id_clima INT PRIMARY KEY AUTO_INCREMENT,
 tipo_clima VARCHAR(255) NOT NULL
);


CREATE TABLE Vegetacao (
 id_vegetacao INT PRIMARY KEY AUTO_INCREMENT,
 tipo_vegetacao VARCHAR(255) NOT NULL,
 caracteristicas_vegetacao TEXT NOT NULL
);


CREATE TABLE Risco_Extincao (
 id_risco_extincao INT PRIMARY KEY AUTO_INCREMENT,
 nome_categoria VARCHAR(255) NOT NULL,
 criterios TEXT NOT NULL,
 acoes_conservacao TEXT NOT NULL
);


CREATE TABLE Habitat (
 id_habitat INT PRIMARY KEY AUTO_INCREMENT,
 nome_habitat VARCHAR(255) NOT NULL,
 id_clima INT NOT NULL,
 id_vegetacao INT NOT NULL,
 ameacas TEXT,
 CONSTRAINT FOREIGN KEY (id_clima) REFERENCES Clima(id_clima),
 CONSTRAINT FOREIGN KEY (id_vegetacao) REFERENCES Vegetacao(id_vegetacao)
);


CREATE TABLE Ameacas_Habitat (
 id_ameaca_habitat INT PRIMARY KEY AUTO_INCREMENT,
 id_habitat INT NOT NULL,
 descricao_ameaca TEXT NOT NULL,
 CONSTRAINT FOREIGN KEY (id_habitat) REFERENCES Habitat(id_habitat)
);


CREATE TABLE urso (
 id_urso INT PRIMARY KEY AUTO_INCREMENT,
 id_habitat INT NOT NULL,
 id_risco_extincao INT NOT NULL,
 nome_cientifico VARCHAR(255) NOT NULL,
 nome_comum VARCHAR(255) NOT NULL,
 status_conservacao VARCHAR(255) NOT NULL,
 foto VARCHAR(255),
 CONSTRAINT FOREIGN KEY (id_habitat) REFERENCES Habitat(id_habitat),
 CONSTRAINT FOREIGN KEY (id_risco_extincao) REFERENCES Risco_Extincao(id_risco_extincao)
);


CREATE TABLE Detalhes_Especie (
 id_detalhes_especie INT PRIMARY KEY AUTO_INCREMENT,
 id_urso INT NOT NULL,
 alimentacao VARCHAR(255) NOT NULL,
 distribuicao_geografica VARCHAR(255) NOT NULL,
 populacao_estimada INT,
 CONSTRAINT FOREIGN KEY (id_urso) REFERENCES urso(id_urso)
);


CREATE TABLE Observacoes_Extras (
 id_observacao_extra INT PRIMARY KEY AUTO_INCREMENT,
 id_urso INT NOT NULL,
 data_observacao DATE NOT NULL,
 observacao TEXT NOT NULL,
 CONSTRAINT FOREIGN KEY (id_urso) REFERENCES urso(id_urso)
);


CREATE TABLE Estatisticas_Populacao (
 id_estatisticas_populacao INT PRIMARY KEY AUTO_INCREMENT,
 id_urso INT NOT NULL,
 ano_estatisticas YEAR NOT NULL,
 tamanho_populacao INT NOT NULL,
 tendencia_populacao VARCHAR(255) NOT NULL,
 CONSTRAINT FOREIGN KEY (id_urso) REFERENCES urso(id_urso)
);


CREATE TABLE Imagens (
 id_imagem INT PRIMARY KEY AUTO_INCREMENT,
 id_urso INT NOT NULL,
 caminho_imagem VARCHAR(255) NOT NULL,
 legenda VARCHAR(255),
 CONSTRAINT FOREIGN KEY (id_urso) REFERENCES urso(id_urso)
);




-- inserts ficticios


INSERT INTO Vegetacao (tipo_vegetacao, caracteristicas_vegetacao)
VALUES
('Floresta Boreal', 'Coníferas predominantes (pinheiros, abetos), clima frio, solo úmido'),
('Tundra Alpina', 'Plantas baixas (líquens, musgos), solo congelado, permafrost'),
('Floresta Temperada', 'Folhas caducas (carvalho, nogueira), clima ameno, solo fértil'),
('Savana', 'Gramíneas predominantes, árvores esparsas, clima quente e seco'),
('Floresta Tropical Úmida', 'Grande diversidade de plantas, clima quente e úmido, solo rico em nutrientes');


INSERT INTO Clima (tipo_clima)
VALUES
('Frio e Seco'),
('Frio e Úmido'),
('Temperado'),
('Quente e Seco'),
('Quente e Úmido');


INSERT INTO Habitat (nome_habitat, id_clima, id_vegetacao, ameacas)
VALUES
('Floresta Boreal', 1, 1, 'Desmatamento, mudança climática, exploração madeireira'),
('Tundra Alpina', 2, 2, 'Mudanças climáticas, atividades humanas, derretimento do permafrost'),
('Floresta Temperada', 1, 3, 'Desmatamento, agricultura, urbanização'),
('Savana', 3, 4, 'Conversão para pastagens, expansão agrícola, caça'),
('Floresta Tropical Úmida', 4, 5, 'Desmatamento, mineração, construção de barragens');




INSERT INTO Risco_Extincao (nome_categoria, criterios, acoes_conservacao)
VALUES
('Criticamente Ameaçado', 'População extremamente pequena, declínio rápido, alto risco de extinção', 'Proteção de habitat emergencial, reprodução assistida, reintrodução em áreas selvagens'),
('Em Perigo', 'População pequena e em declínio, ameaças graves, alto risco de extinção', 'Pesquisa e monitoramento intensivos, manejo populacional, educação ambiental'),
('Vulnerável', 'População suscetível a declínio, ameaças moderadas, risco moderado de extinção', 'Proteção de habitat, manejo sustentável, pesquisa e monitoramento'),
('Quase Ameaçado', 'População próxima dos critérios de ameaça, declínio potencial, risco baixo de extinção', 'Monitoramento contínuo, pesquisa e manejo populacional'),
('Menos Preocupante', 'População estável ou em crescimento, ampla distribuição, baixo risco de extinção', 'Monitoramento regular, pesquisa e manejo populacional sustentável');




INSERT INTO urso (nome_cientifico, nome_comum, status_conservacao, foto, id_habitat, id_risco_extincao)
VALUES
('Ursus arctos', 'Urso-pardo', 'Vulnerável', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Ursus_arctos_001.jpg/1200px-Ursus_arctos_001.jpg', 1, 1),
('Ursus maritimus', 'Urso-polar', 'Em perigo', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Ursus_maritimus_female_and_cub_at_Churchill_Manitoba_Canada.jpg/1200px-Ursus_maritimus_female_and_cub_at_Churchill_Manitoba_Canada.jpg', 3, 3),
('Ursus thibetanus', 'Urso-de-colar-preto', 'Vulnerável', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Ursus_thibetanus_male_in_Nepal.jpg/1200px-Ursus_thibetanus_male_in_Nepal.jpg', 2, 2),
('Ailuropoda melanoleuca', 'Panda-gigante', 'Em perigo de extinção', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Ailuropoda_melanoleuca_sitting.jpg/1200px-Ailuropoda_melanoleuca_sitting.jpg', 5, 4),
('Ursus americanus', 'Urso-negro', 'Menos preocupante', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Ursus_americanus_Glacier_National_Park.jpg/1200px-Ursus_americanus_Glacier_National_Park.jpg', 1, 1);






INSERT INTO Detalhes_Especie (id_urso, alimentacao, distribuicao_geografica, populacao_estimada)
VALUES
( 1,'Carnívoro (onívoro oportunista)', 'América do Norte, Europa e Ásia', 200.000),
( 2,'Carnívoro (predador de focas)', 'Ártico', 15.000),
( 3,'Omnívoro (plantas, insetos, carniça)', 'Himalaia e sudoeste da China', 60.000),
( 4,'Herbívoro (bambu)', 'Montanhas do centro da China', 1.800),
( 5,'Omnívoro (bagas, insetos, carniça)', 'América do Norte', 600.000);






INSERT INTO Estatisticas_Populacao (id_urso, ano_estatisticas, tamanho_populacao, tendencia_populacao)
VALUES
(1, 2020, 180.000, 'Decrescente'),
(2, 2020, 13.000, 'Estável'),
(3, 2020, 55.000, 'Crescente'),
(4, 2020, 1.600, 'Estável'),
(5, 2020, 550.000, 'Crescente');


INSERT INTO Imagens (id_urso, caminho_imagem, legenda)
VALUES
(1, 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Ursus_arctos_001.jpg/1200px-Ursus_arctos_001.jpg', 'Urso-pardo em seu habitat natural'),
(2, 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Ursus_maritimus_female_and_cub_at_Churchill_Manitoba_Canada.jpg/1200px-Ursus_maritimus_female_and_cub_at_Churchill_Manitoba_Canada.jpg', 'Urso-polar com seu filhote'),
(3, 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Ursus_thibetanus_male_in_Nepal.jpg/1200px-Ursus_thibetanus_male_in_Nepal.jpg', 'Urso-de-colar-preto na floresta temperada'),
(4, 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Ailuropoda_melanoleuca_sitting.jpg/1200px-Ailuropoda_melanoleuca_sitting.jpg', 'Panda-gigante em seu habitat natural'),
(5, 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Ursus_americanus_Glacier_National_Park.jpg/1200px-Ursus_americanus_Glacier_National_Park.jpg', 'Urso-negro em um parque nacional');


INSERT INTO Ameacas_Habitat (id_habitat, descricao_ameaca)
VALUES
(1, 'Desmatamento: Perda de habitat florestal para agricultura e pecuária'),
(2, 'Mudanças climáticas : Aumento das temperaturas e alterações nos padrões de precipitação'),
(3, 'Exploração madeireira: Corte excessivo de árvores para produção de madeira'),
(4, 'Conversão para pastagens: Transformação de áreas naturais em pastagens para gado'),
(5, 'Caça e pesca ilegal: Matança ilegal de ursos e outros animais selvagens');


INSERT INTO Observacoes_Extras (id_urso, data_observacao, observacao)
VALUES
(1, '2023-10-04', 'Um urso-pardo foi observado interagindo com turistas em um parque nacional.'),
(2, '2023-05-12', 'Um urso-polar foi avistado nadando em águas abertas, possivelmente devido às mudanças climáticas.'),
(3, '2024-02-01', 'Um urso-de-colar-preto foi encontrado ferido por caçadores ilegais.'),
(4, '2023-11-15', 'Um panda-gigante foi observado forrageando em áreas com bambu escasso, possivelmente devido à fragmentação do habitat.'),
(5, '2023-08-20', 'Um urso-negro foi visto vasculhando lixeiras em uma área urbana, buscando comida.');


-- Criar a view
CREATE VIEW view_ursos AS
SELECT * FROM urso WHERE status_conservacao = 'ex';


-- Criar a stored procedure
DELIMITER //
CREATE PROCEDURE insert_urso(
   IN nome_cientifico VARCHAR(100),
   IN nome_comum VARCHAR(100),
   IN status_conservacao VARCHAR(100),
   IN foto VARCHAR(255),
   IN id_habitat INT,
   IN id_risco_extincao INT
)
BEGIN
   INSERT INTO urso (nome_cientifico, nome_comum, status_conservacao, foto, id_habitat, id_risco_extincao)
   VALUES (nome_cientifico, nome_comum, status_conservacao, foto, id_habitat, id_risco_extincao);
END //
DELIMITER ;


-- Criar a tabela de logs para o trigger
CREATE TABLE log_insert_urso (
   id INT AUTO_INCREMENT PRIMARY KEY,
   nome_cientifico VARCHAR(100),
   nome_comum VARCHAR(100),
   data_insercao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Criar o trigger
DELIMITER //
CREATE TRIGGER after_insert_urso
AFTER INSERT ON urso
FOR EACH ROW
BEGIN
   INSERT INTO log_insert_urso (nome_cientifico, nome_comum)
   VALUES (NEW.nome_cientifico, NEW.nome_comum);
END //
DELIMITER ;


