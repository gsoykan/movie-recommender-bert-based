<script>
    import * as _ from 'lodash';
    import 'chota';
    import {
        Card,
        Row,
        Col,
        Container,
        Tag
    } from 'svelte-chota';

    const imageSrc = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/best-movies-1614634680.jpg?crop=1.00xw:1.00xh;0,0&resize=980:*"
    const tmdbApiKey = ""

    let recommendationsTriple = [];
    let movieTitleQuery;

    function getRecommendations() {
        fetch(`./getRecommendation/${movieTitleQuery}`)
            .then(async response => {
                const responseJSON = await response.json()
                recommendationsTriple = _.chunk(responseJSON.data, 3)
                console.log(recommendationsTriple)
            })
            .catch(e => {
                console.log(e)
                alert("Unknown Movie")
            })
    }

    async function getMovieImage(imdbId) {
        const url = `https://api.themoviedb.org/3/movie/${imdbId}/images?api_key=${tmdbApiKey}`
        const response = await fetch(url)
        const tmdbResponse = await response.json()
        const imageFilePath = tmdbResponse.backdrops[0].file_path
        return `https://image.tmdb.org/t/p/w300/${imageFilePath}`
    }
</script>


<Container>
    <img src={imageSrc}>
    <input bind:value={movieTitleQuery}>
    <button on:click={getRecommendations}>Get your recommendations for the movie!</button>
    {#each recommendationsTriple as recommendationTriple}
        <Row>
            {#each recommendationTriple as recommendation}
                <Col>
                    <Card>

                        {#await getMovieImage(recommendation[3])}
                            <p>...poster is being loaded</p>
                        {:then data}
                            <img src={data} alt="Movie Poster"/>
                        {:catch error}
                            <p>Poster could not be fetched :/!</p>
                        {/await}

                        <h4 slot="header">{recommendation[0]}</h4>
                        <Tag>{recommendation[2]}</Tag>
                        {recommendation[1]}
                    </Card>
                </Col>
            {/each}
        </Row>
    {/each}
</Container>

<style>
</style>
