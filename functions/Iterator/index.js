//Iterator
//IteratorFunction

exports.handler = function iterator (event, context, callback) {
    let index = event.iterator.index
    let step = event.iterator.step
    let count = event.iterator.count
    let src = event.iterator.src
   
    index = index + step
    src = event.src
    
    
    callback(null, {
      index,
      step,
      count,
      // src,
      continue: index < count
    })
  }