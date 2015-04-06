def map(f, l) {
    if is_pure(f) {
        return parmap(f, l)
    } else {
        ret = []
        for(i in l) {
           ret.append(f(i))
        }
        return ret
    }
}
