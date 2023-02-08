class Paxos:
  def __init__(self, acceptors):
    self.acceptors = acceptors

  def propose(self, value):
    # Phase 1: Proposal
    proposal_id = self.get_unique_proposal_id()
    for acceptor in self.acceptors:
      acceptor.receive_proposal(proposal_id, value)
    
    # Phase 2: Acceptance
    acceptances = []
    for acceptor in self.acceptors:
      acceptance = acceptor.get_acceptance(proposal_id)
      if acceptance:
        acceptances.append(acceptance)
    
    # Phase 3: Learn
    if self.has_majority(acceptances):
      self.learn(value)

  def get_unique_proposal_id(self):
    # logic to generate a unique proposal id

  def has_majority(self, acceptances):
    # logic to check if acceptances have reached a majority

  def learn(self, value):
    # logic to update the value of the accepted proposal

class Acceptor:
  def receive_proposal(self, proposal_id, value):
    # logic to receive a proposal from a proposer

  def get_acceptance(self, proposal_id):
    # logic to get the acceptance for a specific proposal id
