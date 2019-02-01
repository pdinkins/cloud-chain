function fetchIssues () {
    var issues = JSON.parse(localStorage.getItem('issues'));
    var issuesList = document.getElementById('issuesList');
    
    issuesList.innerHTML = '';
    
    for (var i = 0; i < issues.length; i++) {
      var id = issues[i].id;
      var desc = issues[i].description;
      var assignedTo = issues[i].assignedTo;
      var status = issues[i].status;
      
      issuesList.innerHTML +=   '<div class="well">'+
                                '<h3>' + desc + '</h3>'+
                                '<a href="#" class="btn btn-warning" onclick="setStatusClosed(\''+id+'\')">Close</a> '+
                                '<a href="#" class="btn btn-danger" onclick="deleteIssue(\''+id+'\')">Delete</a>'+
                                '</div>';
    }
  }

  document.getElementById('issueInputForm').addEventListener('submit', saveIssue);

function saveIssue(e) {
    var issueDesc = document.getElementById('issueDescInput').value;
    var issue = {

      description: issueDesc,
    }
    
    if (localStorage.getItem('issues') === null) {
      var issues = [];
      issues.push(issue);
      localStorage.setItem('issues', JSON.stringify(issues));
    } else {
      var issues = JSON.parse(localStorage.getItem('issues'));
      issues.push(issue);
      localStorage.setItem('issues', JSON.stringify(issues));
    }
    
    document.getElementById('issueInputForm').reset();
   
    fetchIssues();
    
    e.preventDefault(); 
  }

function setStatusClosed (id) {
    var issues = JSON.parse(localStorage.getItem('issues'));
    
    for(var i = 0; i < issues.length; i++) {
      if (issues[i].id == id) {
        issues[i].status = "Closed";
      }
    }
      
    localStorage.setItem('issues', JSON.stringify(issues));
    
    fetchIssues();
  }

function deleteIssue (id) {
    var issues = JSON.parse(localStorage.getItem('issues'));
    
    for(var i = 0; i < issues.length; i++) {
      if (issues[i].id == id) {
        issues.splice(i, 1);
      }
    }
    
    localStorage.setItem('issues', JSON.stringify(issues));
    
    fetchIssues();
  }