const express = require('express')
const mongoose = require('mongoose')
const ShortUrl = require('./models/shortUrl')
const app = express()

//TODO fill in with unique mongoURI
mongoose.connect('', {
  useNewUrlParser: true, useUnifiedTopology: true
})

app.set('view engine', 'ejs')
app.use(express.urlencoded({ extended: false }))

app.get('/', async (req, res) => {
  const shortUrls = await ShortUrl.find()
  res.render('index', {shortUrls: shortUrls })
  return res.json(shortUrls)
})

app.post('/shortUrls', async (req, res) => {
  await ShortUrl.create({full: req.body.fullUrl })
  const shortUrls = await ShortUrl.find()
  res.render('index', {shortUrls: shortUrls })
  res.setHeader('Content-Type', 'application/json');
  return res.json(shortUrls)
})

app.get('/:shortUrl', async (req, res) => {
  const shortUrl = await ShortUrl.findOne({short: req.params.shortUrl })
  if (shortUrl == null) return res.sendStatus(404)
  shortUrl.clicks++
  shortUrl.save()
  res.redirect(shortUrl.full)
  res.setHeader('Content-Type', 'application/json');
  return res.json(shortUrl)
})

app.listen(process.env.PORT || 5000);