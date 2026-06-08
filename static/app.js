async function getRecommendations() {

    const movie =
    document.getElementById(
        "movieInput"
    ).value.trim();

    if (!movie) {

        alert(
            "Please enter a movie name"
        );

        return;
    }

    const loading =
    document.getElementById(
        "loading"
    );

    const results =
    document.getElementById(
        "results"
    );

    results.innerHTML = "";

    loading.style.display =
    "block";

    try {

        const response =
        await fetch(
            `/recommend?title=${encodeURIComponent(movie)}`
        );

        const data =
        await response.json();

        loading.style.display =
        "none";

        if (!response.ok) {

            alert(
                data.detail
            );

            return;
        }

        let html = "";

        data.forEach(item => {

            let poster =
            item.movie?.poster;

            if (
                !poster ||
                poster === "N/A"
            ) {

                poster =
                "https://via.placeholder.com/300x450?text=No+Poster";
            }

            html += `

            <div class="col-lg-3 col-md-4 col-sm-6 mb-4">

                <div class="movie-card">

                    <img
                    src="${poster}"
                    alt="${item.title}">

                    <div class="card-content">

                        <h5>
                            ${item.title}
                        </h5>

                        <p class="rating">
                            ⭐ ${item.movie?.rating || "N/A"}
                        </p>

                        <p>
                            📅 ${item.movie?.year || "N/A"}
                        </p>

                        <p>
                            Similarity:
                            ${(item.score * 100).toFixed(2)}%
                        </p>

                    </div>

                </div>

            </div>

            `;
        });

        results.innerHTML = html;

    }
    catch (error) {

        console.error(error);

        loading.style.display =
        "none";

        alert(
            "Something went wrong"
        );
    }
}

document
.getElementById("movieInput")
.addEventListener(
    "keypress",
    function(event){

        if(
            event.key === "Enter"
        ){

            getRecommendations();
        }
    }
);