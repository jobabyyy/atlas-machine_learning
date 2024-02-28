-- list all bands w/ Glam rock as their main style
SELECT band_name, IFNULL((spilt - formed), (2020 - formed)) AS lifespan
FROM metal_bands
WHERE style LIKE %Glam rock%
ORDER BY lifespan DESC;