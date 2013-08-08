program define main
  insheet using %(csv)s
  %(cmdline)s
  model2json , path(%(json)s)
end

program define mat2json, rclass
  syntax , mat(name)

  local nrows = rowsof(`mat')
  local ncols = colsof(`mat')

  local result = "["

  forvalues i = 1/`nrows' {
    local result = "`result'["
    forvalues j = 1/`ncols' {
      local value = string(`mat'[`i', `j'])
      local result = "`result'`value'"
      if `j' < `ncols' local result = "`result',"
    }
    local result = "`result']"
    if `i' < `nrows' local result = "`result',"
  }
  local result = "`result']"
  return local json = "`result'"
end

program define model2json
  syntax , path(str)

  tempname f
  file open `f' using "`path'", write text replace
  file write `f' "{"

  local first = 1
  foreach key in %(scalars)s {
    if !`first' {
      file write `f' ","
    }
    local first = 0
    local value = string(e(`key'), "%(format)s")
    file write `f' `""`key'":`value'"'
  }

  foreach key in %(macros)s {
    file write `f' `","`key'":"`e(`key')'""'
  }

  foreach key in %(matrices)s {
    tempname mat
    matrix `mat' = e(`key')
    mat2json , mat(`mat')
    file write `f' `","`key'":`r(json)'"'
  }

  file write `f' "}"
  file close `f'
end

main
