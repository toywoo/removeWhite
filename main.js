var start = new Date();

var imgs = document.getElementsByTagName("img")

var i = 0;

for (i = 0; i < imgs.length; i++) {
  sour = imgs[i].src
  console.log("url: " + sour)

	fetch(sour)
  	.then(function(res){
  	return res.body.getReader().read()
	}).then(function(data) {
		console.log(data.value)
	})
}

var end = new Date()

console.log("length: " + imgs.length, "time: " + (end - start)/1000)