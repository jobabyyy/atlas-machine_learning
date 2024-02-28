-- list all bands w/ Glam rock as their main style
SELECT band_name, IF(split='-', 2020 - formed, split - formed) AS lifespan_until_2020
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY ifespan_until_2020 DESC;