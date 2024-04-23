window.onload = async function() {await main();};

async function main() {
    await build_gallery()
}

async function build_gallery() {
    let response = await fetch("/photo_paths");
    let paths = await response.json()
    let gallery = document.getElementById("gallery")

    let col_heights = [0, 0, 0]

    let col_1 = document.createElement("div")
    col_1.id = "gallery_column_1"
    col_1.className = "gallery"
    let col_2 = document.createElement("div")
    col_2.id = "gallery_column_2"
    col_2.className = "gallery"
    let col_3 = document.createElement("div")
    col_3.id = "gallery_column_3"
    col_3.className = "gallery"
    gallery.append(col_1, col_2, col_3)

    paths.forEach((path)=>{
        // get the shortest column and add image to that
        let image= create_image(path)
        let image_height = image.height
        let shortest_col = col_heights.indexOf(Math.min(...col_heights))
        console.log(col_heights)
        switch (shortest_col) {
            case 0:
                col_1.appendChild(image)

                break;
            case 1:
                col_2.appendChild(image)
                break;
            case 2:
                col_3.appendChild(image)
                break;
            default:
                console.log("something went wrong getting shortest column")
        }
        col_heights[shortest_col] += image_height
    })
}

function create_image(path){
    let image = document.createElement("img")
    image.className = "gallery_image"
    image.src = path
    return image
}