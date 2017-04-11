console.log("test");
get_tweet();

function render_tweet(tweet_object) {
    console.log("render_tweet");
    $('#most_retweets').text(tweet_object['tweet']);
    $('#1').text('Tax Amnesty + Demonetization = Reset of Past problems. Future everything linked to Adhaar...big Black money generation difficult Deepak Singh added');
    $('#2').text('36');
    $('#3').text('41');
    $('#4').text('2 Mar');
}
function get_tweet() {
    tweet_object = ['sample tweet'];
    render_tweet(tweet_object);
    return tweet_object;
}