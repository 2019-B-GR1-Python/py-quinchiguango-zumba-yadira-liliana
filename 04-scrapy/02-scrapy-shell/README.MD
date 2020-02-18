# Scrapy
## Instalación

Ejecutar dentro de `Anaconda Prompt`.

```
$ pip install scrapy 
```

o una alternativa es

```
$ conda install -c conda-forge scrapy 
```

## Comandos Generales
- `scrapy bench` : Da las caracteristicas para poder hacer web scraping o web crawling de ese computador
- `scrapy settings` : Visualizar las configuraciones extra
- `scrapy version` : Visualizar la version de Scrapy


### scrapy view 'url'
Permite interatuar con la respuesta de scrapy mediante un shell. Se abre una nueva ventana del navegador. Antes de hacer scrapy es necesario comprobar con este comando si el contenudo de la pagina web es accesible (esté en HTML5)

- Ejem bien: Pagina Authors Pluralsight
- Ejem mal: Pagina SRI


### scrapy shell 'url'
Trabajar con la ventana, permite interactuar con la respuesta del scrapy mediante un shell

```
$ response.css('title')
$ response.css('title').extract()
$ response.css('title::text').extract()
$ response.css('.author::text').extract()
$ response.css('.author::text')[0].extract()
```

o se utiliza el metodo `extract_first()`

- Extraer texto de un etiqueta con una clase
- Extraer texto de una clase dentro de otra clase
- Extraer texto de una propiedad de una etiqueta

### XPATH
Las etiquetas de un archivo HTML tiene una xpath en el navegador por el cual pueden ser buscadas.

Una vez copiado el xpath de la etiqueta utilizamos el siguiente comando:

```
$ response.xpath("/html/head/title").extract()
```
Doble slash antes del title indica que debe seleccionar todas las etiquetas que tengan xpath title

Si utilizamos el xpath de otra etiqueta dentro del documento html utilizamos el mismo comando

```
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
```

Para extraer solo el texto de la etiqueta utilizamos la funcion text() al final de el xpath precedido por un /

```
$ response.xpath('/html/body/div/div[2]/div[2]/h2/text()').extract()
```

Para filtrar por atributos de una etiqueta se utiliza el @, se utiliza un doble // al comienzo para extraer todas las etiquetas que coincidan con ese xpath

```
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ response.xpath("//div[@class='quote']/span/a/@href").extract_first()
$ xpath-filtro-href.PNG
```

scrapy startproject 'projectname'
Iniciamos un nuevo proyecto con el comandos

```
$ scrapy startproject arania_basica
```
Para iniciar la araña nos dirigimos al directorio donde se encuentra un archivo de extension .cfg y ejecutamos el siguiente comando

```
scrapy crawl nombre_araña
scrapy-crawl-aranita.PNG